# coding:utf-8
import ctypes
import os
import platform
import datetime
import re


class ClearOverdueFiles:

    def get_free_space(self, dirname):
        '''
        计算磁盘可用空间
        :参数 dirname:相应目录
        :返回:返回磁盘可用空间，单位GB
        '''
        if platform.system() == 'Windows':
            free_bytes = ctypes.c_ulonglong(0)
            ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname), None, None,
                                                       ctypes.pointer(free_bytes))
            return free_bytes.value / 1024 / 1024 / 1024
        else:
            st = os.statvfs(dirname)
            return st.f_bavail * st.f_frsize / 1024 / 1024 / 1024

    def disk_use_percent(self, dirname, totalspace):
        '''
        计算磁盘使用率
        :参数 dirname: 相应目录
        :参数 totalspace: 磁盘总容量
        :返回:返回磁盘使用占比
        '''
        free_space = self.get_free_space(dirname)
        use_space = totalspace - free_space  # 计算已使用的空间，单位GB
        use_space_percent = use_space * 100 / totalspace  # 计算使用空间占比，此处没有取百分数，取的是百分数乘以100后的值，方便后续判断
        return use_space_percent

    # def remove_overdue_file(self, dirname, totalspace,Time_difference,threshold,file_type):
    #     '''
    #     当磁盘空间达到某一使用率时，删除指定目录下的指定时间内的文件
    #     :参数 dirname:被处理的目录
    #     :参数 totalspace:磁盘总容量
    #     :参数 Time_difference:文件过期时间值
    #     :参数 threshold:磁盘空间报警阀值
    #     '''
    #
    #     ds = list(os.walk(dirname))  # 获得所有文件夹的信息列表
    #     delta = datetime.timedelta(days=Time_difference)  # 设定3天前的文件为过期,这个天数可以根据需要进行设置，单位是天
    #     now = datetime.datetime.now()  # 获取当前时间
    #     use_space = self.disk_use_percent(dirname, totalspace)
    #     file_type = '.log'
    #     # print ds
    #     # print delta
    #     # print now
    #     for d in ds:  # 遍历该列表
    #         os.chdir(d[0])  # 进入本级路径，防止找不到文件而报错
    #         if d[2] != []:  # 如果该路径下有文件
    #             for x in d[2]:  # 遍历这些文件
    #                 ctime = datetime.datetime.fromtimestamp(os.path.getctime(x))  # 获取文件创建时间
    #                 # print ctime
    #                 # print x
    #                 file_name = os.path.basename(x)  # 获得文件名称
    #                 pattern = re.compile(file_type)
    #                 match = len(pattern.findall(file_name))#匹配文件类型
    #                 print file_name
    #
    #                 if match>0:
    #                     if use_space > threshold:  # 设置磁盘使用警戒值
    #                         if ctime < (now - delta):  # 若创建于delta天前，这里设置是三天内创建的文件，方便本地测试
    #                             os.remove(x)  # 删除文件保留文件夹
    #                             print "删除完毕，删除的文件名称是：！"+x
    #                         else:
    #                             print "当前暂无过期文件！"
    #                             break
    #
    #                     else:
    #                         print "磁盘空间充裕，请勿删除文件！"
    #                         break
    #                 else:
    #                     print "目录下暂无指定类型的文件"
    #                     break
    #
    #         else:
    #             print "文件夹暂无文件，无需清理！"

    def deleteFile(self, base_dir, file_ype, days):
        now_time = datetime.datetime.now()  # 获取当前时间
        os.chdir(base_dir)  # 切换到此目录
        cwd = os.getcwd()  # 得到当前目录
        files = os.listdir(os.getcwd())  # 列出目录中文件
        for file in files:
            if os.path.isfile(file):
                file_name = os.path.basename(file)  # 获得文件名称
                pattern = re.compile(file_ype)
                match = len(pattern.findall(file_name))  # 查找文件类型
                if match > 0:
                    timestamp = os.path.getctime(file)  # 得到文件的修改时间
                    date = datetime.datetime.fromtimestamp(timestamp)  # 时间格式化
                    if (now_time - date).days < days:  # now_time - date).days 计算时间差，相差天数
                        os.remove(file)  # 删除文件
                        print("文件删除成功,删除文件名称为： " + file)
                    else:
                        print('暂无过期文件')


if __name__ == "__main__":
    # 需要删除的目标目录，我使用的是本地目录进行测试，生产环境需要更改此目录
    file_path = "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Jenkins\\.jenkins\\workspace\\application_interface_test\\html1"
    disk_total_space = 100  # 报警磁盘空间的总容量，根据自身磁盘的容量进行配置
    Time_difference = 3  # 设定3天前的文件为过期文件，取值范围为正整数或0
    threshold = 40  # 磁盘空间使用率警戒值，取值范围0--100
    file_type = '.txt'  # 指定一个被删除文件的类型
    c = ClearOverdueFiles()
    space = c.disk_use_percent(file_path, disk_total_space)
    # print space
    c.remove_overdue_file(file_path, disk_total_space, Time_difference, threshold, file_type)
