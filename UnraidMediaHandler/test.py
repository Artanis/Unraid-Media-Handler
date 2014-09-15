import os, re, time
from app.BLL.lcm import LCM



# Testing Least Common Multiple
print ("Testing Least Common Multiple")
print ("LCM of 10, 16, 24", LCM.lcmm ([10, 16, 24]))
print ("LCM of 6, 13, 22, 24", LCM.lcmm ([6, 13, 22, 24]))
print ("LCM of 12, 15, 25", LCM.lcmm ([12, 15, 25]))
time.sleep(1)

#Testing Series Object
print ("Testing Creation of Series Object")
for subdir, dirs, files in os.walk('app\TestFiles\Test\Series'):
	for dir in dirs:
		print (dir)
time.sleep(1)


time.sleep(5)