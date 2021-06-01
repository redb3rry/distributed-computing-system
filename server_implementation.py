import server
import math


class ServerImplementation(server.Server):

    def read_matrix(self, filename):
        f = open(filename, "r")
        nr = int(f.readline())
        nc = int(f.readline())

        A = [[0] * nc for x in range(nr)]
        r = 0
        c = 0
        for i in range(0, nr * nc):
            A[r][c] = float(f.readline())
            c += 1
            if c == nc:
                c = 0
                r += 1

        return A

    def create_tasks(self, data, num_of_workers):
        A = data[0]
        B = data[1]
        result_rows = len(A)
        result_cols = len(B[0])
        divider = math.ceil(result_rows / num_of_workers)
        tasks = []
        for i in range(num_of_workers):
            start = i * divider
            end = ((i + 1) * divider)
            task_A = A[start:end]
            task_B = B
            task = [task_A, task_B]
            tasks.append(task)
        return tasks

    def read_data(self, filename):
        A = self.read_matrix(filename[0])
        B = self.read_matrix(filename[1])
        return [A, B]

    def add_to_results(self, result, connection_number):
        pass


ServerImplementation().run("localhost", 8765, ["A.txt", "B.txt"])
