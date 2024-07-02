

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list) - 1
    steps = 1

    while(start <= end):
        print("Step", steps, ":", str(list[start : end+1]))

        steps = steps + 1
        middle = (start + end)//2

        if element == list[middle]:
            return print(list[middle])
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return print(-1)

myL = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
target = 8

binary_search(myL, target)