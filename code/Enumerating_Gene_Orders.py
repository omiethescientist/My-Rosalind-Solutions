import sys
n = int(sys.argv[1])
fo = "../rosalind_perm_output.txt"
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
        with open(fo, "r") as file: 
            print(len(array))
            for x in array:
                print(*x, sep = " ")
            file.close()

recursive_loop(array, n)
