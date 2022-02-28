# # -*-coding:utf-8-*-
# import os
#
# paths = "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Jenkins\\.jenkins\\workspace\\application_interface_test\\html"
# for root, dirs, files in os.walk(paths):
#     for dir in dirs:
#         print os.path.join(root, dir).decode('gbk').encode('utf-8')
#     for file in files:
#         print os.path.join(root, file).decode('gbk').encode('utf-8')

# ! /usr/bin/env python
# coding:utf-8

# import os, datetime,glob
#
# paths = "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Jenkins\\.jenkins\\workspace\\application_interface_test\html"

# def get_create_time(dirname):
#     list = os.listdir(dirname)
#     filelist = []
#     for i in range(0, len(list)):
#         path = os.path.join(dirname, list[i])
#         if os.path.isfile(path):
#             filelist.append(list[i])
#     # print filelist
#     time_lists=[]
#     for i in range(0, len(filelist)):
#         path = os.path.join(dirname, filelist[i])
#         # print path
#         if os.path.isdir(path):
#             continue
#         timestamp = os.path.getctime(path)
#         # print timestamp
#         # ts1 = os.stat(path).st_mtime
#         # print ts1
#
#         date = datetime.datetime.fromtimestamp(timestamp)
#         real_time=date.strftime('%Y-%m-%d %H:%M:%S')
#         time_lists.append(real_time)
#     return time_lists
# t=get_create_time(paths)
# print t
# x='fdfdfd.log'
# path = "test_user_info.py"
# h=os.path.splitext(x)[1]
# suffixs=['csv','log','doc']
# if h in suffixs:
#     print 'hello world'
# else:
#     print 'no match'

#-*-coding:utf-8 -*-
import os,threading,time,datetime
# curTime=time.strftime("%Y-%M-%D",time.localtime())#记录当前时间
curTime = datetime.datetime.now()  # 获取当前时间
print curTime
execF=False
ncount=0
def execTask():
  #具体任务执行内容
  print "execTask executed!"
def timerTask():
  global execF
  global curTime
  global ncount
  if execF is False:
    execTask()#判断任务是否执行过，没有执行就执行
    execF=True
  else:#任务执行过，判断时间是否新的一天。如果是就执行任务
    # desTime=time.strftime("%Y-%M-%D",time.localtime())
    desTime = datetime.datetime.now()  # 获取当前时间
    print desTime
    if desTime > curTime:
      execF = False#任务执行执行置值为
      curTime=desTime
  ncount = ncount+1
  timer = threading.Timer(5,timerTask)
  timer.start()
  print "定时器执行"+str(ncount)+"次"
if __name__=="__main__":
  timer = threading.Timer(5,timerTask)
  timer.start()