from turtle import clear
import currentprice
import threading, queue, time

q = queue.Queue()

def getPrice():
    while True:
        q.put(currentprice.quote().getQuote())

priceThread = threading.Thread(target = getPrice)
priceThread.start()

while True:
    print(q.get())
    

