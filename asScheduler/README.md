# Simple asyncio task scheduler

simple asyncio task scheduler for micropython.


## usage

1. define task, set function, paramters, interval, task state etc.
2. define scheduler.
3. add tasks to scheduler.
4. run scheduler. 

## demo

```
from scheduler import Scheduler, Task

def LED():
    pyb.LED(1).toggle()

def pn(n):
    print(n)

task1 = Task(LED, None, 1000)
task2 = Task(pn, 1, 1000)
task3 = Task(pn, 2, 1500)

sc = Scheduler()
sc.add(task1)
sc.add(task2)
sc.add(task3)
sc.scheduler()
```

