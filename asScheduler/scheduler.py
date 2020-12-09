import uasyncio
from micropython import const

TASK_STOP = const(0)
TASK_RUN = const(1)

class Task():

    def __init__(self, task, param = None, interval = 1000, stat = TASK_RUN):
        self._task = task
        self._param = param
        self._stat = stat
        self._interval = interval

    def pause(self):
        self._stat = TASK_STOP

    def resume(self):
        self._stat = TASK_RUN

    def interval(self, interval):
        self._interval = interval

    async def run(self):
        while True:
            if self._stat == TASK_RUN:
                if self._param == None:
                    self._task()
                else:
                    self._task(self._param)
            await uasyncio.sleep_ms(self._interval)

class Scheduler:

    def __init__(self):
        self.loop = uasyncio.get_event_loop()

    def scheduler(self):
        self.loop.run_forever()

    def add(self, task):
        self.loop.create_task(task.run())

    def pause(self, task):
        task.pause()

    def resume(self, task):
        task.resume()

    def delete(self, task):
        task.pause()
