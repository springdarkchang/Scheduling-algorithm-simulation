import clock
import time
import CPU
import window
class ProcessList:
    def __init__(self):
        self.running_processes = None  # 运行的进程
        self.ready_processes = []  # 时间片轮转法的就绪队列和多级反馈队列的就绪队列1
        self.ready_processes2 = []  # 多级反馈队列的就绪队列2
        self.ready_processes3 = []  # 多级反馈队列的就绪队列3
    def add_ready_process(self, process):  # 在就绪队列中添加进程
        self.ready_processes.append(process)
    def add_running_process(self):  # 在运行队列中添加进程
        if len(self.ready_processes) == 0:
            return None
        else:
            CPU.cpu.ir = self.ready_processes[0].ProID  # 设置CPU的ir
            self.running_processes=self.ready_processes[0]  # 进入运行队列
            self.ready_processes.pop(0)  # 从就绪队列中删除
            if len(self.ready_processes)>0:
                CPU.cpu.ProtectSpot(self.ready_processes[0].ProID)  # CPU获取下一个进程
            else:
                CPU.cpu.pc=0
            self.run_time_slice(time_slice)  # 进行时间片轮转
            if self.running_processes.psw == -1:
                self.running_processes = None  # 结束进程
                clock.Clock.num_stop += 1  # 结束进程数量
            else:
                self.add_ready_process(self.running_processes)  # 结束进程后更新就绪队列
                self.running_processes = None  # 清空运行进程

    def run_time_slice(self,ptime):  # 时间片轮转
        st=clock.Clock.current  # 记录开始时间
        while self.running_processes.stime < ptime:  # 时间片用尽之前循环
            self.running_processes.stime += 1  # 记录已用时间片
            if self.running_processes.InstrucNum > self.running_processes.ir:  # 判断是否还有指令
                window.ui.printf(f"{clock.Clock.current}:[运行进程:{self.running_processes.ProID},{self.running_processes.data[self.running_processes.ir][0]},计算]")
                self.running_processes.ir += 1  # 指令指针+1
                self.running_processes.pc=self.running_processes.ir-1  # 获取下一指令
                time.sleep(clock.Clock.sleep_time)
                clock.Clock.current += 1
            else:
                window.ui.printf(f"{clock.Clock.current}:[终止进程:{self.running_processes.ProID}]")
                self.running_processes.psw = -1  # 设置进程状态为终止
                break
        if self.running_processes.psw == -1:
            et=clock.Clock.current  # 记录结束时间
            self.running_processes.TurnTimes.append([st,et])  # 记录进程的运行时间
            self.running_processes.EndTimes = clock.Clock.current  # 记录进程结束时间
        else:
            self.running_processes.stime = 0  # 时间片清零
            et = clock.Clock.current  # 记录结束时间
            self.running_processes.TurnTimes.append([st, et])  # 记录进程的运行时间
            window.ui.printf(f"{clock.Clock.current}:[重新进入就绪队列:{self.running_processes.ProID},{self.running_processes.InstrucNum}]")

    # 多级反馈队列调度算法
    def feedback_queue(self):
        if self.running_processes == None:  # 如果没有运行进程
            if len(self.ready_processes) != 0:  # 如果一级队列不为空
                CPU.cpu.ir = self.ready_processes[0].ProID  # 设置CPU的ir
                self.running_processes = self.ready_processes[0]  # 进入运行队列
                self.ready_processes.pop(0)  # 从就绪队列中删除
                if len(self.ready_processes) > 0:  # 获取下一进程
                    CPU.cpu.ProtectSpot(self.ready_processes[0].ProID)
                elif len(self.ready_processes2) > 0:
                    CPU.cpu.ProtectSpot(self.ready_processes2[0].ProID)
                elif len(self.ready_processes3) > 0:
                    CPU.cpu.ProtectSpot(self.ready_processes3[0].ProID)
                else:
                    CPU.cpu.pc = 0
                self.run_time_slice(3)  # 进行时间片轮转
                if self.running_processes.psw != -1:
                    self.ready_processes2.append(self.running_processes)  # 进入二级队列
                    self.running_processes = None  # 清空运行进程
                else:
                    self.running_processes = None  # 结束进程
                    clock.Clock.num_stop += 1  # 结束进程数量
            elif len(self.ready_processes2) != 0:
                CPU.cpu.ir = self.ready_processes2[0].ProID
                self.running_processes = self.ready_processes2[0]
                self.ready_processes2.pop(0)
                if len(self.ready_processes2) > 0:
                    CPU.cpu.ProtectSpot(self.ready_processes2[0].ProID)
                elif len(self.ready_processes3) > 0:
                    CPU.cpu.ProtectSpot(self.ready_processes3[0].ProID)
                else:
                    CPU.cpu.pc = 0
                self.run_time_slice(4)
                if self.running_processes.psw != -1:
                    self.ready_processes3.append(self.running_processes)  # 进入三级队列
                    self.running_processes = None  # 清空运行进程
                else:
                    self.running_processes = None  # 结束进程
                    clock.Clock.num_stop += 1  # 结束进程数量
            elif len(self.ready_processes3) != 0:
                CPU.cpu.ir = self.ready_processes3[0].ProID
                self.running_processes = self.ready_processes3[0]
                self.ready_processes3.pop(0)
                if len(self.ready_processes3) > 0:
                    CPU.cpu.ProtectSpot(self.ready_processes3[0].ProID)
                else:
                    CPU.cpu.pc = 0
                self.run_time_slice(5)
                if self.running_processes.psw != -1:
                    self.ready_processes3.append(self.running_processes)  # 继续在三级队列运行
                    self.running_processes = None  # 清空运行进程
                else:
                    self.running_processes = None  # 结束进程
                    clock.Clock.num_stop += 1  # 结束进程数量

    def get_ready_process(self):
        return len(self.ready_processes)  # 返回就绪队列长度
pro = ProcessList()
idea = 1
time_slice = 3#时间片轮转法中的时间片