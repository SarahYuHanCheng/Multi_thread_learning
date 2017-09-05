import threading

threads = []                 

def client_thread():

    print('This is client_thread')


''' main thread task: server '''
def server():

        global threads 
        global j

        # 產生第一支子執行緒
        childThread_client_thread = threading.Thread(target=client_thread, args=())
        childThread_client_thread.start()
        threads.append(childThread_client_thread)
        j = 0
        for t in threads:
        	print(threads[j]) # 印出目前陣列裡的所有執行緒
        	j +=1


        # 產生第二支子執行緒
        childThread_client_thread = threading.Thread(target=client_thread, args=())
        childThread_client_thread.start()
        threads.append(childThread_client_thread)
        j = 0
        for t in threads:
        	print(threads[j])
        	j +=1

        # 產生第三支子執行緒
        childThread_client_thread = threading.Thread(target=client_thread, args=())
        childThread_client_thread.start()
        threads.append(childThread_client_thread)
        j = 0
        for t in threads:
        	print(threads[j])
        	j +=1




'''程式從這裡開始跑，產生一支主執行緒main thread'''
# target is the callable object to be invoked by the run() method.
mainThread_server = threading.Thread(target=server, args=())
# calling the thread’s start() method invokes the run() method in a separate thread of control.
mainThread_server.start()

# enumerate() return a list, include所有alive的thread objects 以及 main thread.
# (alive thread includes daemon and dummy threads)
alives = threading.enumerate()
print(alives)

mainThread_server.join()

