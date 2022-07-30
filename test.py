a = int(input("입력:"))

for i in range(a):
    b = '+'
    if(not i%2):
         b = "+"
    else:
        b = "-"
    print(b,end='')
