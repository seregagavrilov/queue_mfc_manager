import threading
import inspect
import time
condition = threading.Condition()


tasklist =[]


def put_to_list(cond):
    """
    producer code
    :param cond:
    :return:
    """
    for i in range(10):
        time.sleep(0.01)
        cond.acquire()
        tasklist.append(i)
        cond.notify()
        cond.release()


def take_from_list(cond):
    """
    consumer code
    :param cond:
    :return:
    """

    while True:
        cond.acquire()
        cond.wait()
        item = tasklist.pop()
        print(item)
        cond.release()





if __name__ == "__main__":
    condition = threading.Condition()
    cs1 = threading.Thread(name='consumer1', target=take_from_list, args=(condition,))
    pd = threading.Thread(name='producer', target=put_to_list, args=(condition,))

    cs1.start()
    pd.start()
