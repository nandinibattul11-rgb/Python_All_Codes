#Multiple threads
import threading
import time
def music():
    print("Playing Music")
    time.sleep(3)
def download():
    print("Downloading")
    time.sleep(2)
def chat():
    print("Chatting")
    time.sleep(1)
t1 = threading.Thread(target=music)
t2 = threading.Thread(target=download)
t3 = threading.Thread(target=chat)
t1.start()
t2.start()
t3.start()