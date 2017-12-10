import threading

nums_list = [[2, 6],[1,8],[7,16]]

def count_print(start, end, name):
    for i in range(start,end):
        print("\n%d by thread %s\n" % (i, name))

def run_threads():
    thread_list = []
    count=1
    for nums in nums_list:
        create_thread = threading.Thread(target=count_print, args=(nums[0],nums[1],"thread%s"%count))
        count+=1
        thread_list.append(create_thread)
    for thread in thread_list:
        thread.start()

if __name__=="__main__":
    run_threads()
