class DagReducer:
    @classmethod
    def reduce(self, dag):
        nexts = {}
        roots = []
        for task in dag.tasks:
            if "depends_on" in task:
                for dependency in task.depends_on:
                    if dependency not in nexts:
                        nexts[dependency] = []
                    nexts[dependency].append(task.name)
            else:
                roots.append(task.name)

        levels = {root: 1 for root in roots}
        queue = list(roots)
        while len(queue):
            element = queue.pop()
            candidates = nexts.get(element, [])
            for candidate in candidates:
                current = levels.get(candidate, 0)
                levels[candidate] = max(current, levels[element] + 1)
                if current != levels[candidate] and candidate in nexts:
                    queue.append(candidate)

        level2tasks = {}
        for task_name, level in levels.items():
            if level not in level2tasks:
                level2tasks[level] = []
            level2tasks[level].append(task_name)

        levels = [level2tasks[level] for level in sorted(level2tasks)]

        return levels
