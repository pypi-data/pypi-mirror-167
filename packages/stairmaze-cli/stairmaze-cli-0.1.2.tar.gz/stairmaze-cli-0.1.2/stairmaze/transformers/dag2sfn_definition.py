import json
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .tools.dag_reducer import DagReducer


class Dag2SFNDefintionTransformer:
    @classmethod
    def transform(self, dag, dag_reducer=DagReducer):
        template_folder = os.path.join(os.path.dirname(__file__), "templates")
        env = Environment(
            loader=FileSystemLoader(template_folder), autoescape=select_autoescape()
        )

        levels = dag_reducer.reduce(dag)

        state_machine = {"States": {}}
        states = state_machine["States"]
        for level, task_names in enumerate(levels):
            state_name = f"Level_{level}"
            if level == 0:
                state_machine["StartAt"] = state_name
            if len(task_names) > 1:
                state = {"Type": "Parallel", "Branches": []}
                for task_name in task_names:
                    template = env.get_template("task.json.template")
                    rendered = json.loads(
                        template.render(
                            job_definition=f"job-name-{task_name}",
                            job_queue="${job_queue}",
                        )
                    )
                    rendered["End"] = True
                    state["Branches"].append(
                        {"StartAt": task_name, "States": {task_name: rendered}}
                    )
            else:
                task_name = task_names[0]
                template = env.get_template("task.json.template")
                rendered = json.loads(
                    template.render(
                        job_definition=f"job-name-{task_name}", job_queue="${job_queue}"
                    )
                )
                state = rendered
            if level == len(levels) - 1:
                state["End"] = True
            else:
                state["Next"] = f"Level_{level+1}"
            states[state_name] = state
        return state_machine
