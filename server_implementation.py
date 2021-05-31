import server


class ServerImplementaion(server.Server):

    def create_tasks(self):
        pass


ServerImplementaion().run("localhost", 8765, "data.txt")
