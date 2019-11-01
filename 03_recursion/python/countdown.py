# slightly different from demo code
def countdown(start):
    if start == 0:
        print("0")
        return
    else:
        print(start)
        countdown(start-1)

countdown(5)
