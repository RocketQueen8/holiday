# coding:utf-8
import ctypes
import os
import platform
import sys
import time
import datetime
import shutil
paths="C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Jenkins\\.jenkins\\workspace\\application_interface_test\html"
path_d="D:\\"

def get_free_space(dirname):
    # 计算磁盘可用空间，返回磁盘的剩余空间，单位GB
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024 / 1024
    else:
        st = os.statvfs(dirname)
        return st.f_bavail * st.f_frsize / 1024 / 1024 / 1024




def get_create_time(dirname):
    #计算某一目录下所有文件（不包含文件夹）的创建时间，返回目录下所有文件的创建时间列表
    list = os.listdir(dirname)
    filelist = []
    for i in range(0, len(list)):
        path = os.path.join(dirname, list[i])
        if os.path.isfile(path):
            filelist.append(list[i])
    # print filelist
    time_lists=[]
    for i in range(0, len(filelist)):
        path = os.path.join(dirname, filelist[i])
        # print path
        if os.path.isdir(path):
            continue
        timestamp = os.path.getctime(path)
        # print timestamp
        # ts1 = os.stat(path).st_mtime
        # print ts1

        date = datetime.datetime.fromtimestamp(timestamp)
        real_time=date.strftime('%Y-%m-%d %H:%M:%S')
        # return real_time
        time_lists.append(real_time)
    return time_lists
t=get_create_time(paths)
print t

# def remove_file(dirname,total):
#     d_percent = disk_use_percent(dirname,total)
#     print d_percent
#     # if d_percent>80:
#     #     pass
# remove_file(paths,100)

def disk_use_percent(dirname, totalspace):
    # 计算磁盘使用率，返回一个整型
    free_space = get_free_space(dirname)
    # print free_space
    use_space = totalspace - free_space
    use_space_percent = int(use_space * 100 / totalspace)
    time_lists = get_create_time(dirname)
    curtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    day1 = datetime.datetime.strptime(curtime, '%Y-%m-%d %H:%M:%S')
    # print day1
    # print type(day1)
    if use_space_percent > 10:
        for times in time_lists:
            day2=datetime.datetime.strptime(times,'%Y-%m-%d %H:%M:%S')
            # print day2
            # print type(day2)
            day3=day1-day2
            #
            if day3.days<1:
                os.remove()

# disk_use_percent(paths,100)


# return use_space_percent
#     print use_space_percent
#     print type(use_space_percent)
#
# disk_use_percent(paths,100)