# Simple Time Base task scheduler

simple Time Base task scheduler for micropython.



## usage

1. define task, set function, paramters, interval, task state etc.
2. define scheduler, recommend use **machine.Timer(-1)** (soft timer) as time base.
3. add tasks to scheduler.
4. run scheduler. 

## demo

```
from scheduler import Scheduler, Task
import machine

def LED():
    pyb.LED(1).toggle()

def pn(n):
    print(n)

task1 = Task(LED)
task2 = Task(pn, 1, interval = 1000)
task3 = Task(pn, 2, interval = 1500)

sc = Scheduler(machine.Timer(-1))
sc.add(task1)
sc.add(task2)
sc.add(task3)
sc.scheduler()
```

