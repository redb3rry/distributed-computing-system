from worker import Worker


class WorkerImplementation(Worker):

    def __init__(self, uri):
        super(WorkerImplementation, self).__init__(uri)

    def do_work(self, task):
        return 0


WorkerImplementation("ws://localhost:8765").run()
