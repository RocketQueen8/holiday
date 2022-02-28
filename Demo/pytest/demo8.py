# coding:utf-8
import ctypes
import os
import platform
import datetime
import re


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
    free_space = get_free_space(base_dir)
    use_space = total_space - free_space  # 计算已使用的空间，单位GB
    use_space_percent = use_space * 100 / total_space  # 计算使用空间占比，此处没有取百分数，取的是百分数乘以100后的值，方便后续判断
    return use_space_percent


def deleteFile(base_dir, file_type, total_space, threshold, expiration_date):
    now_time = datetime.datetime.now()  # 获取当前时间
    os.chdir(base_dir)  # 切换到此目录
    cwd = os.getcwd()  # 得到当前目录
    files = os.listdir(cwd)  # 列出目录中文件
    use_space_percent = disk_use_percent(base_dir, total_space)
    # print use_space_percent
    # print type(use_space_percent)
    # print files
    if use_space_percent > threshold:
        # print threshold
        if files != []:
            for file in files:
                if os.path.isfile(file):
                    file_name = os.path.basename(file)  # 获得文件名称
                    pattern = re.compile(file_type)
                    match = len(pattern.findall(file_name))  # 查找文件类型
                    print file_name
                    # print pattern
                    # print match

                    if match > 0:
                        timestamp = os.path.getctime(file)  # 得到文件的修改时间
                        date = datetime.datetime.fromtimestamp(timestamp)  # 时间格式化
                        time_difference = (now_time - date).days
                        # print time_difference
                        # print timestamp
                        # print date
                        if time_difference < expiration_date:  # now_time - date).days 计算时间差，相差天数
                            os.remove(file)  # 删除文件
                            print "文件删除成功,删除文件名称为： " + file
                        else:
                            print '暂无过期文件！'
                            break
                    else:
                        print '该目录下暂无需要处理的文件！'

                else:
                    print '该目录下存在子目录:' + file + ',暂时无法删除该目录，如有需要请手动处理！'
        else:
            print '该目录下暂无文件！'
    else:
        print '当前磁盘空间充裕，无需清理！'


base_dir = "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Jenkins\\.jenkins\\workspace\\application_interface_test\\html1"
file_ype = ('.log')
expiration_date = 1
total_space = 100
threshold = 40
deleteFile(base_dir, file_ype, total_space, threshold, expiration_date)
# print threshold

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
