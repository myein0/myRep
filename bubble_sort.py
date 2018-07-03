import random

# list size
#N = random.randint(1, 100)
N = 10

list = [random.randint(1, N) for i in range(N)]
print(list)

def swap(some_list, i, j):
    some_list[i], some_list[j] = some_list[j], some_list[i]

i = N
while i >= 2:
    j = 1
    while j <= i - 1:
        if list[j - 1] > list[j]:
            swap(list, j - 1, j)
        j += 1
    i -= 1

print(list)
