# from the python mega course
# to run the entire code remove first ''' pair from code

# datetime  module
'''
import datetime
present = datetime.datetime.now()   # grabs computers time
past = datetime.datetime(2018, 6, 13, 20, 34, 45, 126345)
diff = present-past
print(diff)  # timedelta type (store difference)
print(diff.days)

# getting next date
next = present + datetime.timedelta(days=4)
print(next)
'''

# creating file of todays date name
'''
import datetime

name = str(datetime.datetime.now())
name = name[:10]+'.txt'

file = open(name, 'w')

file.write("line 1\n")

file.close()
'''

# time module (sleeping)
''' 
import time
ls = []
for i in range(8):
    print(i)
    time.sleep(.5)
'''

