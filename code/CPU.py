class CPU:
    def __init__(self):
        self.pc = 0  # 程序计数器，存放下一条指令序号
        self.psw = 0  # 保存当前状态
        self.ir = 0  # 指令寄存器,存放当前指令序号
    def RecoverSpot(self):  # 现场恢复
        self.ir = self.pc
    def ProtectSpot(self,spot):  # 现场保护
        self.pc = spot
    def get_state(self):
        if self.psw == 0:
            return "用户态"
        elif self.psw == 1:
            return "内核态"
cpu = CPU()