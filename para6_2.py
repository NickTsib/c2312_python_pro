try:
    print("start code")
    print(10/0)
    print("no error")
except NameError:
    print("We have an problem with name")
except ZeroDivisionError:
    print("We have an problem with division by 0")

print("code after capsule")