__author__ = 'praveen'

# bubble sort implementation

lis = [9, 3, 2, 7]
p = len(lis)
x = 0
def swap(x, y):
    p = y
    x = y
    y = p

while x < len(lis):
    for i in range(len(lis)):
        print i
        if i < (len(lis)-1):
            print lis[i], lis[i+1]
            if lis[i] < lis[i+1]:
                var = lis[i+1]
                var2 = lis[i]
                lis[i+1] = var2
                lis[i] = var
#               swap(lis[i], lis[i+1])
                print lis[i], lis[i+1]

    x += 1
#    print x


print lis

# if lis[x] > lis[x+1]:   # swap if condition is true
#
#             print i, i+1