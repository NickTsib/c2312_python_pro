try:
    try:
        print("start code")
        print(error)
        print("no error")
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)
