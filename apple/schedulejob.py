import schedule
import time

count = 0
def job():
    global count
    count += 1
    print("I'm working...",count)
    return

schedule.every(5).seconds.do(job)

while True:
    start_time=time.time()
    schedule.run_pending()
    time.sleep(1)
    end_time=time.time()
    print('Time:', round(end_time-start_time,1))
