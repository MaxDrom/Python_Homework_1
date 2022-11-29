
def Calculate(s):
    (a, op, b) = s.split(" ")
    a = float(a)
    b = float(b)

    operations = {}
    operations["+"] = lambda x, y: x+y
    operations["-"] = lambda x, y: x-y
    operations["*"] = lambda x, y: x*y
    operations["/"] = lambda x, y: print("Деление на ноль") if y==0 else x/y
    return operations[op](a,b)

res = Calculate(input())
if res != None:
    print(res)
    