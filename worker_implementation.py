from worker import Worker


class WorkerImplementation(Worker):

    def __init__(self, uri):
        super(WorkerImplementation, self).__init__(uri)

    def do_work(self, task):
        a = task[0]
        b = task[1]
        result = []
        for index, line in enumerate(a):
            line_result = []
            for e in line:
                suma = 0
                for j, element in enumerate(line):
                    suma += element * b[j][index]
                line_result.append(suma)
            result.append(line_result)
        return result


WorkerImplementation("ws://localhost:8765").run()
