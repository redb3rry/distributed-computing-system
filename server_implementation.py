import server
import math
import ast


class ServerImplementation(server.Server):
    divider = 0
    num_of_workers = 0
    result_rows = 0
    result_cols = 0

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
        self.result_rows = len(A)
        self.result_cols = len(A[0])
        divider = math.ceil(self.result_rows / num_of_workers)
        self.divider = divider
        self.num_of_workers = num_of_workers
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

    def add_to_results(self, result, connection_number, results):
        result_arr = ast.literal_eval(result)
        if results == []:
            results = [[0 for i in range(self.result_cols)] for j in range(self.result_rows)]
        results[connection_number * self.divider:(connection_number + 1) * self.divider] = result_arr
        return results


ServerImplementation().run("localhost", 8765, ["A.txt", "B.txt"])
