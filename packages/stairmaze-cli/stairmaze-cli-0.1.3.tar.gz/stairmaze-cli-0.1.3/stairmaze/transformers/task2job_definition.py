import os

from jinja2 import Environment, FileSystemLoader, select_autoescape


class Task2JobDefinitionTransformer:
    @classmethod
    def transform(self, task):

        template_folder = os.path.join(os.path.dirname(__file__), "templates")
        env = Environment(
            loader=FileSystemLoader(template_folder), autoescape=select_autoescape()
        )

        if task.type == "docker":
            template = env.get_template("job.json.template")
            rendered = template.render(
                command=list(task.command),
                image=task.image,
                vpcu=task.cpu,
                memory=task.memory,
            )
            return rendered
