# from datetime import datetime, timedelta


import time





# def time_in():

#     time_in = datetime.datetime.now()
#     return time_in
    
# print(time_in())



# # 可以用但是精确到毫秒
# time_in = datetime.now()
# print("%0.2d:%0.2d:%0.2d" % (time_in.hour, time_in.minute, time_in.second))
# time.sleep(3)
# time_out = datetime.now()
# total_time = time_out - time_in

# print(time_in)
# print(time_out)
# print(total_time)




# def start_time():
#     time_in = datetime.now()
#     print("%0.2d:%0.2d:%0.2d" % (time_in.hour, time_in.minute, time_in.second))
#     return time_in

# def finish_time():
#     time.sleep(3)
#     time_out = datetime.now()
#     print("%0.2d:%0.2d:%0.2d" % (time_out.hour, time_out.minute, time_out.second))
#     return time_out

# # app start
# entry_time = start_time() #9am 0900
# # stuff happens
# exit_time = finish_time() #9:02am 0902




# def total_seconds(entry_time, exit_time):
#     total_time =  exit_time - entry_time
    # # total_time = start_time() - finish_time()
    # try:
    #     print(total_time.hours)
    # except:
    #     print("no hours")
    
    # try:
    #     print(total_time.minutes)
    # except:
    #     print("no minutes")
    # try:
    #     print(total_time.seconds)
    # except:
    #     print("no seconds")
    # seconds = timedelta.seconds
    # minutes = (seconds//60)%60
    # hours = seconds//3600
    # print("%0.2d:%0.2d:%0.2d" % (hours, minutes, seconds))
#     print(total_time)
#     print(total_time * 4)

# total_seconds(entry_time, exit_time)

# start_time = datetime.strptime("2:13:57", "%H:%M:%S")


# 可以用
# start_time = time.time()
# time.sleep(3)
# done_time = time.time()
# total_time = done_time - start_time

# print(total_time)





# a= datetime.now()
# b= datetime.now(time.sleep(3))
# c = b - a 


# print(a)
# print(str(b))
# print(c.total_seconds())



def start_time():
    # time_in = datetime.now()
    time_in = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print("%0.2d:%0.2d:%0.2d" % (time_in.hour, time_in.minute, time_in.second))
    return time_in
print(start_time())

def finish_time():
    # time.sleep(3)
    # time_out = datetime.now()
    time_out = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print("%0.2d:%0.2d:%0.2d" % (time_out.hour, time_out.minute, time_out.second))
    return time_out
print(type(finish_time()))

entry_time = start_time() 
exit_time = finish_time() 

# def total_times(entry_time, exit_time):
#     total_time =  exit_time - entry_time
#     return total_time


def total_times():
    total_time =  exit_time - entry_time
    return total_time
print(total_times())



