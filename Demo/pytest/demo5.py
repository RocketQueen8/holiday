# coding:utf-8
import ctypes
import os
import platform
# import sys
# import time
import datetime
# import glob


file_path = "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Jenkins\\.jenkins\\workspace\\application_interface_test\\html"
path_d="D:\\"
def get_free_space(dirname):
    # 计算磁盘可用空间
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024 / 1024
    else:
        st = os.statvfs(dirname)
        return st.f_bavail * st.f_frsize / 1024 / 1024 / 1024


def disk_use_percent(dirname, totalspace):
    # 计算磁盘使用率
    free_space = get_free_space(dirname)
    use_space = totalspace - free_space
    use_space_percent = use_space * 100 / totalspace
    return use_space_percent
u=disk_use_percent(path_d,365)
print u


def remove_overdue_file(dirname,totalspace):
    ds = list(os.walk(dirname))  # 获得所有文件夹的信息列表
    delta = datetime.timedelta(days=3)  # 设定365天前的文件为过期
    now = datetime.datetime.now()  # 获取当前时间
    use_space=disk_use_percent(dirname,totalspace)
    # print ds
    # print delta
    # print now

    for d in ds:  # 遍历该列表
        os.chdir(d[0])  # 进入本级路径，防止找不到文件而报错
        if d[2] != []:  # 如果该路径下有文件
            for x in d[2]:  # 遍历这些文件
                ctime = datetime.datetime.fromtimestamp(os.path.getctime(x))  # 获取文件创建时间
                print ctime
                print x
                if use_space>30:
                    if ctime > (now - delta):  # 若创建于delta天前
                        os.remove(x)  # 则删掉
                        print "删除完毕，磁盘已清理部分空间！"

                else:
                    print "磁盘空间充裕，请勿删除文件！"
                    break

# remove_overdue_file(file_path,100)