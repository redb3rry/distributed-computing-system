from server import Server
import math
import ast


# class ServerImplementation(server.Server):
#     divider = 0
#     num_of_workers = 0
#     result_rows = 0
#     result_cols = 0


def create_tasks(data, num_of_workers):
    A = data[0]
    B = data[1]
    divider = math.ceil(len(A) / num_of_workers)
    tasks = []
    for i in range(num_of_workers):
        start = i * divider
        end = ((i + 1) * divider)
        task_A = A[start:end]
        task_B = B
        task = [task_A, task_B]
        tasks.append(task)
    return tasks


def read_data(filename):
    def read_matrix(file):
        f = open(file, "r")
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

    A = read_matrix(filename[0])
    B = read_matrix(filename[1])
    return [A, B, len(A), len(A[0])]


def add_to_results(result, connection_number, results, num_of_workers):
    result_arr = ast.literal_eval(result)
    divider = math.ceil(len(result) / num_of_workers)
    results[connection_number * divider:(connection_number + 1) * divider] = result_arr
    return results


Server(create_tasks, read_data, add_to_results).run("localhost", 8765, ["A.txt", "B.txt"])
