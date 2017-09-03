# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:42:23 2017

@author: Tao yun
"""
import re
from collections import defaultdict
from itertools import product
import random
import os ,time , random
import shutil
import pickle
from multiprocessing import Process
from multiprocessing import Pool ,Queue
import threading
#import defs
#n = int(input())
# a = list()
# b = defaultdict(list)
# print(b)

# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = [7,8,9]
# x = [l1]+[l2]+[l3]
# print(x)

# y = 'sirtubggg123425'
# print(sorted(y))

# x= [('a','b','c'),('a','b','c'),('a','b','c')]
# y = [1,1,1]
# print(list(zip(y,x)))
# print('{}'.format('sadf'))

# def fibonacci(n):
# 	"""
# 	n is  positive integer
# 	"""
# 	if n<=2:
# 		return n-1
# 	else:
# 	    return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(10))


# match = re.search(r'<tr>(?P<ha>.*?)</tr>','<tr>132445545g.rgg</tr>')
# print(match.groupdict())

# match = re.findall(r'(\d)(?=\d\1)','12121')
# print(match)

# a = random.randint(0,10)
# print(a)
	
# a = set([1,2,'a','ff','sdf'])
# print(a)
# a.update(['ab',12])	    
# print(a)


# print(os.getcwd())

# print(os.path.getsize(r'E:\python_work\test.py'))

# d = dict(url='index.html',title='首页',content='首页')
# d2 = pickle.dumps(d)
# print(d2)
# d3 = pickle.loads(d2)
# print(d3)

# def run_task(name):
# 	print('Task %s (pid = %s) is running...' %(name,os.getpid()))
# 	time.sleep(random.random()*3)
# 	print('Task %s end.' %name)

# if __name__ == '__main__':

# 	print('Current process %s .'%os.getpid())
# 	p = Pool()
# 	for i in range (5):
# 		p.apply_async(run_task,args=(i,))

# 	print('Waiting for all subprocesses done...')
# 	p.close()
# 	p.join()
# 	print('All subprocesses done.')	

# def thread_run(urls):
# 	print('Current %s is running ...' %threading.current_thread().name)
# 	for url in urls:
# 		print('%s --->%s' %(threading.current_thread().name,url))
# 		time.sleep(random.random())
# 	print('%s ended.' %threading.current_thread().name)
	
# print("%s is running ..." %threading.current_thread().name)		
# t1 = threading.Thread(target=thread_run,name='Thread_1',args=(['url1','url2','url3'],))
# t2 = threading.Thread(target=thread_run,name='Thread_2',args=(['url4','url5','url6'],))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('%s ended.'%threading.current_thread().name)


class S():
	def __init__(self):
		print('正在运行')

	def asdf(self):
		print('a')

s = S()
