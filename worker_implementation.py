from time import sleep
import datetime
from worker import Worker


def do_work(task):
    a = task[0]
    b = task[1]
    result = []
    for index, line in enumerate(a):
        line_result = []
        for i in range(len(b[0])):
            suma = 0
            for j, element in enumerate(line):
                suma += element * b[j][i]
            line_result.append(suma)
        result.append(line_result)
    #print(result)
    return result

#2 - 0.67; 3:4 - 68; 5:6 - 69
sleep(0.69)
Worker("ws://localhost:8765", do_work).run()
