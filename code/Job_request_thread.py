import PCB
import FileOperation
import ProcessList
import clock
import window
import CPU
class Job_request_thread():
    def __init__(self):
        self.PCB_list=[]*10  # 初始化PCB表
        self.i=0  # 作业请求数量

    def run(self):
        while clock.Clock.num_stop != clock.Clock.num_start:  # 判断是否所有作业请求都被处理
            if clock.Clock.current % 10 == 0:    #  每10s判断是否有新增作业请求
                self.EnReady(self.i)  # 读取作业请求
        CPU.cpu.pc = 0
        CPU.cpu.ir = 0  # 清空CPU
        clock.Clock.pause = 1  # 结束时钟

    def PCBqueue(self):  # 创建PCB表
        job_num = f"../input{FileOperation.file_num}/jobs-input.txt"
        jobs = FileOperation.read_jobs(job_num)
        clock.Clock.num_start = len(jobs)  # 记录作业请求数量
        for i in range(len(jobs)):
            p=PCB.PCB(jobs[i][0], jobs[i][1], jobs[i][2])  # 创建PCB
            p.data = FileOperation.get_instruc_data(p.ProID)  # 读取作业请求的指令
            self.PCB_list.append(p)  # 将作业请求放入PCB表

    def new_EnReady(self,t,n,j):  # 新增作业请求
        if len(ProcessList.pro.ready_processes)<10:
            p=PCB.PCB(t,n,j)  # 创建PCB
            p.data=FileOperation.get_instruc_data(p.ProID)  # 读取作业请求的指令
            p.RunTimes=clock.Clock.current  # 记录作业请求入队时间
            p.psw=1  # 标记作业请求已开始
            ProcessList.pro.add_ready_process(p)  # 将作业请求放入就绪队列
            self.PCB_list.append(p)  # 将作业请求放入PCB表
            window.ui.printf(f"{clock.Clock.current}:[新增作业请求:{t},{n},{j}]")
            window.ui.printf(f"{clock.Clock.current}:[创建进程:{t}]")
            window.ui.printf(f"{clock.Clock.current}:[进入就绪队列:{t},{n}]")

    def EnReady(self,i):  # 读取作业请求
        # 就绪队列最多只能有10个进程
        if len(ProcessList.pro.ready_processes)<10:
            # 判断是否到达作业请求入队时间并保证只能入队一次
            if self.PCB_list[self.i].InTimes <= clock.Clock.current:
                if self.PCB_list[self.i].psw==0:  # 判断是否是新建进程
                    t=clock.Clock.current  # 记录作业请求入队时间
                    self.PCB_list[self.i].psw=1
                    self.PCB_list[i].RunTimes = t
                    window.ui.printf(f"{t}:[新增作业请求:{self.PCB_list[i].ProID},{self.PCB_list[i].InTimes},{self.PCB_list[i].InstrucNum}]")
                    window.ui.printf(f"{t}:[创建进程:{self.PCB_list[self.i].ProID}]")
                    window.ui.printf(f"{t}:[进入就绪队列:{self.PCB_list[self.i].ProID},{self.PCB_list[self.i].InstrucNum}]")
                    ProcessList.pro.add_ready_process(self.PCB_list[self.i])
                if self.i < len(self.PCB_list) - 1:  # 判断是否还有作业请求
                    self.i += 1

    def Put_PCB_Data(self):  # 输出结果
        window.ui.printf("状态统计信息:")
        self.PCB_list.sort(key=lambda x: x.ProID)  # 按照作业请求的ID排序
        for i in range(len(self.PCB_list)):
            window.ui.printf(f"{self.PCB_list[i].EndTimes}:[{self.PCB_list[i].ProID}:{self.PCB_list[i].InTimes}+{self.PCB_list[i].RunTimes}+{self.PCB_list[i].EndTimes-self.PCB_list[i].InTimes}]")
j=Job_request_thread()