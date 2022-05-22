import clock
import time
import ProcessList
import window
class Process_scheduling_thread(clock.Clock):
    def __init__(self):
        super().__init__()

    def run(self):
        self.setpause(0)  # 开始运行
        if self.is_pause():  # 设置停止条件
            return
        while self.is_pause() == 0:
            if ProcessList.idea == 1:
                self.schedule1()  # 时间片轮转法进程调度
            elif ProcessList.idea == 2:
                self.schedule2()  # 多级反馈队列法进程调度
    def ClockInterrupt(self):  # 时钟中断
        time.sleep(clock.Clock.sleep_time)
        self.addtime()

    def schedule1(self):  # 时间片轮转法进程调度
        if len(ProcessList.pro.ready_processes) != 0:  # 如果就绪队列不为空
            if ProcessList.pro.running_processes == None:
                ProcessList.pro.add_running_process()  # 添加运行队列
                return
        self.ClockInterrupt()  # 时钟中断
        if clock.Clock.pause == 0:
            window.ui.printf(f"{clock.Clock.current}:[CPU空闲]")

    def schedule2(self):  # 多级反馈队列进程调度
        # 如果三个就绪队列不为空
        if len(ProcessList.pro.ready_processes) != 0 or len(ProcessList.pro.ready_processes2) != 0 or len(ProcessList.pro.ready_processes3) != 0:
            ProcessList.pro.feedback_queue()  # 进入多级反馈队列
            return
        self.ClockInterrupt()  # 时钟中断
        if clock.Clock.pause == 0:
            window.ui.printf(f"{clock.Clock.current}:[CPU空闲]")
p = Process_scheduling_thread()