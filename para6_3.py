try:
    print("start code")
    print(10/0)
    print("no error")
except (NameError, ZeroDivisionError):
    print("We have an problem")

print("code after capsule")
