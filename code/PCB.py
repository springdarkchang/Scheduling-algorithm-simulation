import random

class PCB:
    def __init__(self, ProID, InTimes, InstrucNum):  # 进程创建
        self.ProID = ProID  # 进程ID
        self.Priority = random.randint(1,5)  # 进程优先级,为1~5之间的随机数
        self.InTimes = InTimes  # 进程请求时间
        self.EndTimes = -1  # 进程结束时间
        self.psw = 0  # 进程状态
        self.RunTimes = 0  # 进程运转时间
        self.TurnTimes = []  # 进程周转时间统计
        self.InstrucNum = InstrucNum  # 进程指令数
        self.pc = 0  # 程序计数器信息
        self.ir = 0  # 指令寄存器信息
        self.data = []  # 指令内容
        self.stime = 0  # 时间计数器