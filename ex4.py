def max_diff(int_array):
    if len(int_array) < 2:
        raise ValueError
    max = int_array[1] - int_array[0]
    i = 0
    while i < len(int_array) - 1:
        j = i + 1
        while j < len(int_array):
            if int_array[j] - int_array[i] > max:
                max = int_array[j] - int_array[i]
            j += 1
        i += 1
    return max

#TEST | usage : python3 ex4.py 100 10 5 10 1 8 16 21
import sys
array = []
for value in sys.argv[1:]:
    array.append(int(value))

try:
    print(max_diff(array))
except ValueError:
    print("Wrong arguments")
