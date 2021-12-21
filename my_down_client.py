
# task_worker.py
import os
import time, sys, queue
from multiprocessing.managers import BaseManager

import subprocess
import sys
import threading


from random import randint
# from pkg.cmdcolor import *   #windows
from termcolor import colored   #linux

client_name = 'S_'
#print(os.environ)
name = os.environ.get("USER")

client_name = client_name + name


# printDarkGreen(f'        客户端启动中.. {client_name}')
print(colored(f'        mydownloader客户端启动中.. {client_name}',"green")  )


class MyException(Exception):
    def __init__(self,message):
        Exception.__init__(self)
        self.message=message    

class MyException2(Exception):
    def __init__(self,message):
        Exception.__init__(self)
        self.message=message        

def build_return_list(str_1,str_2,color_):
    '''
    构建 返回列表
    '''
    list_ = []
    list_.append(str_1)
    list_.append(str_2)
    list_.append(color_)
    return list_


# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_work_queue')
QueueManager.register('get_done_queue')
QueueManager.register('get_shared_value')

# 连接到中继服务器:
server_addr = '192.168.2.31'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5010), authkey=b'abcd')
# 从网络连接:
m.connect()
# 获取Queue的对象:
_work_queue = m.get_work_queue()#接受任务队列
_done_queue = m.get_done_queue()
shared_value = m.get_shared_value()

# 从task队列取任务,并把结果写入result队列:



contents = "/mnt"

def my_worker00__when_error_return_1():
    """ flv文件index修复 """
    try:
        print('获取工作队列中..5s后超时')
        line = _work_queue.get(timeout=5)
        # printDarkYellow(f'        running task... ')
        print(colored(f'        running task... ',"yellow")  )
        
        print(line)
        sys.stdout.flush()
        
        
        time.sleep(0.5)
        #if type(line)== type(""):

    except queue.Empty:
        # printDarkGreen('task queue is empty. exit')
        print(colored(f'task queue is empty. exit after 5 seconds',"green")  )
        shared_value = 0
        time.sleep(5)
        
        #exit()
        return 1
    except MyException:
        #printDarkGreen('exit,try again agter 410s')
        print(colored(f'task queue is MyException. exit',"green")  )
        time.sleep(410)
    except MyException2:
        #printYellow('terminal end, close after 20s')
        print(colored(f'terminal end, close after 20s',"green")  )
        time.sleep(20)
        return 1
    
    if 1 == 1:
        ctime = os.path.getctime(line)
    #except :
    #    print("c time error")
    #    break
    
    salt_ = randint(10000, 90000)
    print(colored("进行meta注入 = "+str(line),"green"))
    if 1 == 1 :
        _pr1 = subprocess.Popen(["/usr/bin/yamdi","-i",line,"-o",contents+"/_temp/output.tmp_"+str(salt_)],stderr=subprocess.STDOUT,
                                stdout = subprocess.PIPE,  encoding = 'utf-8')
        print("         _pr1 pid = ",  _pr1.pid)
        _result_1 ,_result_2 = _pr1.communicate()
        print(f"len_result_1 = {len(_result_1)}")
        if _result_2 == None:
            print(f"_result_2 is null")
        else:
            print('error::::::::::::::::::::::')
            print(_result_2)
            
        _mediate = _result_1.split('\n')
        for _ in _mediate:
            print(_)
        print(f" -- DONE -- _pr1 pid = {_pr1.pid}")
        print("         --------------------")
    
    time.sleep(2)
    
    if 1 == 1 :
        _pr2 = subprocess.Popen(["mv","-f",contents+"/_temp/output.tmp_"+ str(salt_) ,line],stderr=subprocess.STDOUT,
                                stdout = subprocess.PIPE,  encoding = 'utf-8')
        #print(f"_pr2 pid = {_pr2.pid}")
        # print("         _pr2 pid = ",  _pr2.pid)
        #_pr2.wait()    #等待子进程结束，父进程继续
        
        _result_1 ,_result_2 = _pr2.communicate()
        

        #print("===================")
        print(f"len_result_1 = {len(_result_1)}")
        #print(len(_result_1))
        if _result_2 == None:
            print(f"_result_2 is null")
            
        else:
            print('error::::::::::::::::::::::')
            print(_result_2)
            print(f"_result_2 = {_result_2}")
        
        print(f"_pr2.returncode = {_pr2.returncode}")
        
        
        
        #print(test_result)
        #time.sleep(1)
        _mediate = _result_1.split('\n')
        for _ in _mediate:
            print(_)
        # print("     -1 done")
        print(f" -- DONE -- _pr2 pid = {_pr1.pid}")
        if _pr2.returncode == 1:
            
            print(colored("     mv 错误","red"))
            os.remove(contents+"/_temp/output.tmp_"+ str(salt_))
            print(colored("     temp_file deleted","yellow"))
            print("===================")
            return 0 
        print("===================")


        time.sleep(4)
    try:
        os.utime(line, (ctime,ctime))
    except:
        #print("")
        print(colored("write utime 错误","red"))
        return 0 
    
    
    try:
        _done_queue.put(line,block=True,timeout=10)
    except:
        print("put done_queue error")
        return 0
    
    print(colored("meta注入完成 = "+str(line),"green"))
    


def my_worker01__when_error_return_1():
    """ youtube 单任务多线程下载 """
    try:
        print('获取工作队列中..30s后超时',end= "\r")
        line = _work_queue.get(timeout=30)
        # printDarkYellow(f'        running task... ')
        
        print(colored(f'              running task... ',"yellow")  )
        
        print(line)
        sys.stdout.flush()
        
        
        time.sleep(0.5)
        #if type(line)== type(""):

    except queue.Empty:
        # printDarkGreen('task queue is empty. exit')
        print(colored(f'task queue is empty. retry after 30 seconds',"green") ,end = '\r' )
        shared_value = 0
        time.sleep(30)
        
        #exit()
        return 0
    except MyException:
        #printDarkGreen('exit,try again agter 410s')
        print(colored(f'task queue is MyException. exit',"green")  )
        time.sleep(410)
    except MyException2:
        #printYellow('terminal end, close after 20s')
        print(colored(f'terminal end, close after 20s',"green")  )
        time.sleep(20)
        return 1
    


    
    salt_ = randint(10000, 90000)
    print(colored("开始下载 = "+str(line),"green"))
    if 1 == 1 :
        
        """  
        youtube-dl -o '/mnt/youtube//%(title)s.%(ext)s' -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'   --proxy "socks5://192.168.2.27:2099" 'https://www.youtube.com/watch?v=3PcIJKd1PKU&ab_channel=xmdi'  --cookies /mnt/youtube.com_cookies.txt 
        """
        _directory = r'/mnt/youtube/test/%(title)s.%(ext)s'
        _format = r'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        _proxy = r'https://192.168.2.27:3334'
        _address = 'https://www.youtube.com/watch?v=3PcIJKd1PKU&ab_channel=xmdi'
        _cookies = r"/mnt/youtube.com_cookies.txt"
        
        _pr1 = subprocess.Popen(["/usr/local/bin/youtube-dl","-o",_directory,
                                "-f",_format,
                                "--proxy",_proxy,
                                line,
                                "--cookies", _cookies,
                                "--external-downloader","aria2c",
                                "--external-downloader-args","-x16 -k 1M"
                                ],
                                stderr=subprocess.STDOUT,stdout = subprocess.PIPE,  encoding = 'utf-8')
        print("         _pr1 pid = ",  _pr1.pid)
        #实时显示输出
        for _inst_print in iter(_pr1.stdout.readline, b'\r'):
            print(_inst_print,end = "")
            if not subprocess.Popen.poll(_pr1) is None:
                if _inst_print == "":
                    break


        #print(subprocess.Popen.poll(_pr1))



        _result_1 ,_result_2 = _pr1.communicate()
        print(f"len_result_1 = {len(_result_1)}")
        if _result_2 == None:
            print(f"_result_2 is null")
        else:
            print('error::::::::::::::::::::::')
            print(_result_2)
            
        _mediate = _result_1.split('\n')
        for _ in _mediate:
            print(_)

            
        print(f" -- DONE -- _pr1 pid = {_pr1.pid}")
        print("         --------------------")
    
    time.sleep(2)
    """ 不执行后续操作  """
    if 1 == 0 :#
        _pr2 = subprocess.Popen(["mv","-f",contents+"/_temp/output.tmp_"+ str(salt_) ,line],stderr=subprocess.STDOUT,
                                stdout = subprocess.PIPE,  encoding = 'utf-8')
        #print(f"_pr2 pid = {_pr2.pid}")
        # print("         _pr2 pid = ",  _pr2.pid)
        #_pr2.wait()    #等待子进程结束，父进程继续
        
        _result_1 ,_result_2 = _pr2.communicate()
        

        #print("===================")
        print(f"len_result_1 = {len(_result_1)}")
        #print(len(_result_1))
        if _result_2 == None:
            print(f"_result_2 is null")
            
        else:
            print('error::::::::::::::::::::::')
            print(_result_2)
            print(f"_result_2 = {_result_2}")
        
        print(f"_pr2.returncode = {_pr2.returncode}")
        
        
        
        #print(test_result)
        #time.sleep(1)
        _mediate = _result_1.split('\n')
        for _ in _mediate:
            print(_)
        # print("     -1 done")
        print(f" -- DONE -- _pr2 pid = {_pr1.pid}")
        if _pr2.returncode == 1:
            
            print(colored("     mv 错误","red"))
            os.remove(contents+"/_temp/output.tmp_"+ str(salt_))
            print(colored("     temp_file deleted","yellow"))
            print("===================")
            return 0 
        print("===================")


        time.sleep(4)

    
    
    try:
        _done_queue.put(line,block=True,timeout=10)
    except:
        print("put done_queue error")
        return 0
    
    
    
    print(colored("下载完成 = "+str(line),"green"))
    


# exit()
while 1:
    if my_worker01__when_error_return_1() :
        break
    
# 处理结束:


print('worker exit. exit after 10 seconds')
time.sleep(10)
exit()