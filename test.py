from concurrent.futures import process
from process import Process as p




try:
    p()
except Exception as e:
    print(e)
else:
    print("all good")



