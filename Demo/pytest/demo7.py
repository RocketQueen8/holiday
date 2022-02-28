# coding:utf-8
import ctypes
import os
import platform
import datetime
import threading


def get_free_space(base_dir):
    '''
    计算磁盘可用空间
    :参数 dirname:相应目录
    :返回:返回磁盘可用空间，单位GB
    '''
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(base_dir), None, None,
                                                   ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024 / 1024
    else:
        st = os.statvfs(base_dir)
        return st.f_bavail * st.f_frsize / 1024 / 1024 / 1024


def disk_use_percent(base_dir, total_space):
    '''
    计算磁盘使用率
    :参数 dirname: 相应目录
    :参数 totalspace: 磁盘总容量
    :返回:返回磁盘使用占比
    '''
    free_space = get_free_space(base_dir)#获取磁盘可用空间
    use_space = total_space - free_space  # 计算已使用的空间，单位GB
    use_space_percent = use_space * 100 / total_space  # 计算使用空间占比，此处没有取百分数，取的是百分数乘以100后的值，方便后续判断
    return use_space_percent


def delete_file(base_dir, suffix, total_space, threshold, expiration_date):
    '''
    根据过滤后的文件名和创建时间删除文件
    :参数 base_dir:被处理目录
    :参数 suffix:文件名白名单，即不属于处理文件范围
    :参数 total_space:磁盘总容量
    :参数 threshold:磁盘空间警戒值，取值范围0--100的正整数
    :返回值:无
    '''
    now_time = datetime.datetime.now()  # 获取当前时间
    use_space_percent = disk_use_percent(base_dir, total_space)  # 获取磁盘使用率
    new_files = file_filter(base_dir, suffix)
    if use_space_percent > threshold:
        if new_files != []:
            for new_file in new_files:
                timestamp = os.path.getctime(new_file)  # 得到文件的修改时间
                date = datetime.datetime.fromtimestamp(timestamp)  # 时间格式化
                time_difference = (now_time - date).days#获取文件创建时间和当前时间的时间差
                print time_difference
    #             if time_difference < expiration_date:
    #                 os.remove(new_file)  # 删除文件
    #                 print  new_file + '已被删除！'
    #             else:
    #                 print '暂无过期文件！'
    #                 break
    #     else:
    #         print '暂无需要清理的文件！'
    # else:
    #     print '当前磁盘空间充裕，无需清理！'


def file_filter(base_dir, suffixs):
    '''
    过滤掉不需要处理的文件名，筛选出需要处理的文件
    :参数 base_dir:被处理目录
    :参数 suffixs:文件名白名单，即不属于处理文件范围
    :返回值:返回一个文件名列表，该列表已经过滤掉白名单中的文件
    '''
    os.chdir(base_dir)  # 切换到此目录
    cwd = os.getcwd()  # 得到当前目录
    files = os.listdir(cwd)  # 列出目录中文件
    new_files = []
    if files != []:
        for file in files:
            if os.path.isfile(file):
                file_name = os.path.basename(file)#获取目录下的所有文件
                file_suffix = os.path.splitext(file_name)[1]#提取文件后缀名
                if file_suffix not in suffixs:#过滤白名单文件
                    new_files.append(file)
    else:
        print '该目录暂无文件！'
    return new_files


base_dir = "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Jenkins\\.jenkins\\workspace\\application_interface_test\\jtl"
expiration_date = 2
total_space = 100
threshold = 40
suffixs = ['.csv', '.log', '.doc', '.c', '.java']
delete_file(base_dir, suffixs, total_space, threshold, expiration_date)
# print threshold
t=file_filter(base_dir,suffixs)
print t

# if __name__ == "__main__":
#
#     # 从命令行取参数，如命令行未传参数使用默认参数
#     if len(sys.argv) > 3:
#         base_dir = sys.argv[1]
#         file_ype = sys.argv[2]
#         days = int(sys.argv[3])
#         deleteFile(base_dir, file_ype, days)
#     else:
#         deleteFile(base_dir, file_ype, days)
