def checker(func, *args, **kwargs):
    try:
        result = func(*args, **kwargs)
    except Exception as exc:
        print(f"We have problems {exc}")
    else:
        print(f"No problems. Result = {result}")


def calculate(expression):
    return eval(expression)


checker(calculate, "2+2")
