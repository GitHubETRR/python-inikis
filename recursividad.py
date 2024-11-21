def mul(x,y):
    if y == 0:
        print("Y=0")
        return 0
    print(f"X={x} Y={y}")
    return + mul(x, y-1)

mul(5,5)
