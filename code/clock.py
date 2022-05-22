class Clock:
    current = 0  # 当前时间
    num_stop= 0  # 已完成的任务数，控制程序的退出
    num_start=0  # 记录任务总数
    sleep_time= 1  # 时间刻
    pause=1  # 暂停
    def addtime(self):  # 添加时间
        if Clock.pause == 0:
            Clock.current += 1
    def gettime(self):  # 获取当前时间
        return Clock.current
    def is_pause(self):  # 判断是否停止
        return Clock.pause
    def setpause(self, pause):  # 设置停止
        Clock.pause = pause
    def start(self):  # 开始
        Clock.pause = 0