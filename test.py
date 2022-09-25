from process import Process as p




try:
    p()
except Exception as e:
    print(f"this is something worry with" + {e})
else:
    print("all good")




