arrray = [7,3,9,2,8,10]

def second(arr):
    first  = 0
    second  = 0
    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first  = arr[i]
        elif second<first and second != first:
            second = arr[i]
    return first,second

# print(second(arrray))

k = [5,7,8,3,7,8,9,2,3]


def security(j):
    k = {}
    for i in j:
        if i not in k:
            k[i] =0
        else:
            k[i] +=1
    answer = len([x for x in k.values() if x >= 1])
    return k,answer

# print(security(k))


# l = [1,2,3,4,5,6,7,8,9]
# l[::2] = 10,20,30,40,50
# print(l)



# a = [1,2,3,4,5,6,7,8,9]
# print(a[3:0:-1])

# arr  = [[1,2,3,4],
#         [4,5,6,7],
#         [8,9,10,11],
#         [12,13,14,15,16],

# ]
# for i in range(0,4):
#     print(arr[i].pop(),end=" ")


# def f(i,va= []):
#     va.append(i)
#     return va

# f(1)
# f(2)
# f(3)
# print(f(4))

# k = 9
# for i in range(1,k):
#     print(i,k-i)



def distance(li):
    gap = []
    for i in range(1,len(li)):
        gap.append(abs(li[i]-abs(li[i-1])))
        print(gap)
    return sum(gap)

print(distance([10,11,7,12,14]))
