import sys
import time
for i in range(1,11,+1):
    time.sleep(1)
    sys.stdout.write(str(i)+' ')
    sys.stdout.flush()