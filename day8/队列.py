#!_*_coding:utf-8_*_
#__author__:"Alex huang"
import queue,time,threading
a = queue.Queue(10)

def put(name):

    while True:
        # for i in range(5):
        #    a.put("包子{}".format(i+1))
        a.put(1)
        print("[%s]生产了5个包子" %name)
        #time.sleep(5)
        a.join()

def get(name):
    while True:
        print("[%s]吃了%s" %(name,a.get()))
        time.sleep(1)
        a.task_done()
        # if a.qsize() == 0:
        #     a.task_done()
        #     print("chi wan le")
t1 = threading.Thread(target=put,args=("Alex",))
t1.start()
t11 = threading.Thread(target=put,args=("HHH",))
t11.start()

t2 = threading.Thread(target=get,args=("hong",))
t3 = threading.Thread(target=get,args=("keke",))
t3.start()
t2.start()
