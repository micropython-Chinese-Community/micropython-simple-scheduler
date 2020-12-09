from scheduler import Scheduler, Task
import machine

def LED():
    pyb.LED(1).toggle()

def pn(n):
    print(n)

task1 = Task(LED, None, 1000)
task2 = Task(pn, 1, 1000)
task3 = Task(pn, 2, 1500)

sc = Scheduler(machine.Timer(-1))
sc.add(task1)
sc.add(task2)
sc.add(task3)
sc.scheduler()
