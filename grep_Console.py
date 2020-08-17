import warnings

for x in range(100):
    r = x
    if r < 2:
        print("console output ",x)

    elif r < 95:
        warnings.showwarning("This is warning", UserWarning, filename="grep_Console.py", lineno=6)
    else:
        raise Exception("error")