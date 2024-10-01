def search(key:int, values:list[int])-> int:
    for i in range(9):
        if key == values[i]:
            return i

def move_counter(key:int, lst:list[int])-> int:
    x = search(key, lst)
    if x >= 5:
        x = 9 - x
    return x
n = int(input())
key = input()
c = 0
for i in range(n):
    lst = [int(i) for i in input()]
    c += move_counter(int(key[i]), lst)
print(c)
#Result 100
