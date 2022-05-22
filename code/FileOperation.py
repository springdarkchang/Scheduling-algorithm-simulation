import clock
import os
import ProcessList
file_num=0
def get_data(input):  # 对读取的数据进行处理使之可识别
    for i in range(len(input)):
        if input[i] == "":
            input.pop(i)
            continue
        input[i] = [int(x) for x in input[i].split(',')]
    return input

def read_jobs(job_num):  # 读取进程作业
    with open(job_num, "r") as f:
        jobs = get_data(f.read().splitlines())
    return jobs

def get_instruc_data(num):  # 读取指令
    file=f"../input{file_num}/{num}.txt"
    with open(file, "r") as f:
        instruc = get_data(f.read().splitlines())
    return instruc

def write_new_jobs(sid,t,num):  # 写入新的作业
    with open(f"../input{file_num}/jobs-input.txt", "a") as f:
        f.write(f"\n{sid},{t},{num}")
    with open(f"../input{file_num}/{sid}.txt", "a") as f:
        for i in range(num):
            f.write(f"{i+1},0\n")

def write_result(result):  # 写入结果
    with open(f"../output{file_num}/ProcessResults.txt", "a") as f:
        f.write(f"{result}\n")

def change_result_name():  # 修改结果文件名，使之符合要求
    try:  # 检测是否存在同名文件，如果有，则覆盖
        if ProcessList.idea == 1:
            os.rename(f"../output{file_num}/ProcessResults.txt",
                      f"../output{file_num}/ProcessResults-{clock.Clock.current}-LZ.txt")
        elif ProcessList.idea == 2:
            os.rename(f"../output{file_num}/ProcessResults.txt",
                      f"../output{file_num}/ProcessResults-{clock.Clock.current}-DJ.txt")
    except:
        if ProcessList.idea == 1:
            os.remove(f"../output{file_num}/ProcessResults-{clock.Clock.current}-LZ.txt")
            os.rename(f"../output{file_num}/ProcessResults.txt",
                      f"../output{file_num}/ProcessResults-{clock.Clock.current}-LZ.txt")
        elif ProcessList.idea == 2:
            os.remove(f"../output{file_num}/ProcessResults-{clock.Clock.current}-DJ.txt")
            os.rename(f"../output{file_num}/ProcessResults.txt",
                      f"../output{file_num}/ProcessResults-{clock.Clock.current}-DJ.txt")