for i in range(1,101):
    if i % 3 == 0:
        print("Bit")
    elif i % 5 == 0:
        print("Maker")
    elif i % 3 == 0 and i%5==0:
        print("BitMaker")
    else:
        print(i)