from concurrent.futures import process
from process import Process as p




try:
    p()
except Exception as e_p:
    print(f"this is something worry with" + {e_p})
else:
    print("all good")


try:
    p.getusername()
except Exception as e_getusername:
    print(f"this is something worry with" + {e_getusername})
else:
    print("all good")

