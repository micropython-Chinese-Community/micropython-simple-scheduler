'''
    simple Time base Task Scheduler

    Author: shaoziyang
    Date:   2021.2
    Ver:    1.2

    https://www.micropython.org.cn

'''

from micropython import const

TASK_STOP = const(0)
TASK_RUN = const(1)

class Task():

    def __init__(self, callback, *param, interval = 1000, state = TASK_RUN):
        self._callback = callback
        self._param = param
        self._intv = interval
        self._state = state
        self._cnt = 10
        self._rt = 0

    def pause(self):
        self._state = TASK_STOP

    def resume(self):
        self._state = TASK_RUN

    def run(self):
        self._callback(*self._param)

class Scheduler():
    def __init__(self, tm, interval = 100, task_idle = None, task_err = None):
        self._tasks = []
        self._task_idle = task_idle
        self._task_err = task_err
        self._interval = interval
        self._tmr = tm
        self._tmr.init(period = interval, callback=self._tmrirq)

    def _tmrirq(self, t):
         for i in range(len(self._tasks)):
            if self._tasks[i]._state == TASK_RUN:
                self._tasks[i]._rt += 1

    def _run(self, task):
        if task._state == TASK_RUN:
            try:
                if task._rt >= task._cnt:
                    task._rt = 0
                    task.run()
            except:
                if self._task_err:
                    self._task_err()

    def scheduler(self):
        while True:
            try:
                for i in range(len(self._tasks)):
                    task = self._tasks[i]
                    self._run(task)
                if self._task_idle:
                    self._task_idle()
            except KeyboardInterrupt:
                return
            except Exception as e:
                print('except {}'.format(e))
            
    def find(self, task):
        try:
            return self._tasks.index(task)
        except:
            return None

    def clear(self):
        self._tasks.clear()

    def add(self, task, stat = TASK_RUN):
        if self.find(task) == None:
            self._tasks.append(task)
            task._cnt = task._intv // self._interval
            print('add task:', task._callback.__name__)
        if stat == TASK_STOP:
            self.pause(task)

    def delete(self, task):
        try:
            self._tasks.remove(task)
        except:
            print('del task <', task, '> error')

    def pause(self, task):
        if self.find(task) != None:
            self._tasks[self.find(task)].pause()

    def resume(self, task):
        if self.find(task) != None:
            self._tasks[self.find(task)].resume()

    def run(self, task):
        if self.find(task) != None:
            task._rt = task._cnt
            self._run(task)

