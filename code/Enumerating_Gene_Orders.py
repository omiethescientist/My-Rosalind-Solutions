import sys
n = int(sys.argv[1])
array = [[i] for i in range(1, n+1)]

def recursive_loop(array, n):
    if len(array[0]) < n:
        new_array = []
        for i in range(1,n+1):
            for j in array:
                if i not in j:
                    j2 = j + [i]
                    new_array.append(j2)
        recursive_loop(new_array, n)
    else:
        print(len(array))
        for x in array:
            print(*x, sep = " ")

recursive_loop(array, n)
