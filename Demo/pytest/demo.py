# coding:utf-8
import ctypes
import os
import platform
import sys
import time
import datetime
import glob

def get_free_space(dirname):
    # 计算磁盘可用空间
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024 / 1024
    else:
        st = os.statvfs(dirname)
        return st.f_bavail * st.f_frsize / 1024 / 1024 / 1024


# size=get_free_space("C:\\")
# # freespace=size/1024
# t=Decimal(size).quantize(Decimal('0.0'))
# print size
# print "C盘的可用空间还有"+str(t)+"G"

def disk_use_percent(dirname, totalspace):
    # 计算磁盘使用率
    free_space = get_free_space(dirname)
    use_space = totalspace - free_space
    use_space_percent = str(use_space * 100 / totalspace) + "%"
    return use_space_percent

paths="C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Jenkins\\.jenkins\\workspace\\application_interface_test\html"
# percent = disk_use_percent(paths, 100)
# print percent

# def dir_files_list(dirname):
#     #列出指定文件夹的文件或目录
#     file_list=os.listdir(dirname)
#     return file_list
# list1 =dir_files_list(paths)
# print list1

def file_path_lists(dirname):
    file_paths=[]
    for root, dirs, files in os.walk(dirname):
        # for dir in dirs:
        #     print os.path.join(root, dir).decode('gbk').encode('utf-8')
        for file in files:
            # real_file=os.chdir(file)
            file_path=os.path.join(root, file).decode('gbk').encode('utf-8')
            # real_path=os.chdir(file_path)
            file_paths.append(file_path)
    return file_paths

# l=file_path_lists(paths)
# print l

# def get_create_time(dirname):
#     # file_paths=file_path_lists(dirname)
#     # print type(file_paths)
#     # for file in file_paths:
#     ctime=os.path.getctime(dirname)
#         # print ctime
#     timeArray = time.localtime(ctime)
#         # print timeArray
#     otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
#         # print otherStyleTime
#     return otherStyleTime
#
# t=get_create_time(paths)
# print t

def get_create_time(dirname):
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
        time_lists.append(real_time)
    return time_lists
t=get_create_time(paths)
print t

# p=file_path_lists(paths)
# print p

# def get_file_creattime(dirname):
#     file_paths=file_path_lists(dirname)
#     ctimes=[]
#     for i in range(len(file_paths)):
#         ctime = os.path.getctime(file_paths[2])
#         ctimes.append(ctime)
#     return ctimes
# t = get_file_creattime(paths)
# print t



# get_file_creattime(paths)


