from stairmaze.exceptions import CycleDetected, NoRootDag


class Checker:
    @classmethod
    def check_dag(self, dag):
        tasks = dag.tasks
        nexts = {}
        roots = []
        for task in tasks:
            if "depends_on" in task:
                for dependency in task.depends_on:
                    if dependency not in nexts:
                        nexts[dependency] = []
                    nexts[dependency].append(task.name)
            else:
                roots.append(task.name)

        if len(roots) == 0:
            raise NoRootDag("Dag without starting nodes")

        ancestors = {task.name: set() for task in tasks}
        queue = [task.name for task in tasks if "depends_on" not in task]
        while len(queue):
            element = queue.pop()
            if element in ancestors[element]:
                raise CycleDetected(f"Task {element} is in a cycle")
            next_nodes = nexts.get(element, [])
            for next_node in next_nodes:
                ancestors[next_node].update(ancestors[element])
                ancestors[next_node].add(element)
                queue.append(next_node)
        return True
