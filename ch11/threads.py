#!/usr/bin/python3

import threading
import time

exitFlag = 0

# creating a new subclass of the thread class
class timeThread(threading.Thread):
	def __init__(self,threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run(self):
		print("Starting:", self.name)
		self.print_time(self.name, self.counter)
		print("Exiting:", self.name)

	def print_time(self, threadName, counter):
		while counter:
			if exitFlag:
				return
			time.sleep(1)
			print("%s: %s" % (threadName, time.ctime(time.time())))
			counter -= 1

thread1 = timeThread(1, "Thread-1", 5)
thread2 = timeThread(2, "Thread-2", 4)
thread3 = timeThread(3, "Thread-3", 3)

thread1.start()
thread2.start()
thread3.start()

# wait for all threads to complete
thread1.join()
thread2.join()
thread3.join()

print("Exiting Main Thread")

