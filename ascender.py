inp = input().split()

if len(inp) < 3:
    print("Too few inputs")
    exit()
elif len(inp) > 3:
    print("Too many inputs")
    exit()

if inp[0].isnumeric() and inp[1].isnumeric() and inp[2].isnumeric():
    print(inp[0] < inp[1] < inp[2])
else:
    print("Invalid inputs.")
