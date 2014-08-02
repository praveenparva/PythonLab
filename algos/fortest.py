__author__ = 'praveen'

test_lst = [("CA", "SFO"), ("MA", "BOS"), ("NY", "NYC")]
test1_lst = [10, 12, 4, 1]

for state, city in test_lst:
    print state, city

x = 0
for i in test1_lst:
    if test1_lst[0] > test1_lst[1]:
        x = test1_lst[1]
        test1_lst[1] = test1_lst[0]
        test1_lst[0] = x
