def dist(x, y, old_x, old_y):
    if (old_x == x and old_y == y):
        return 0
    if (abs(old_x - x) == 2 or abs(old_y - y) == 2):
        return 2
    return 1

def entryTime(s, keypad):
    total = 0
    i = 0
    cur_pos = keypad.find(s[i])
    cur_line = cur_pos / 3
    cur_row = cur_pos % 3
    i += 1
    while i < len(s):
        new_pos = keypad.find(s[i])
        new_line = new_pos / 3
        new_row = new_pos % 3
        total += dist(new_row, new_line, cur_row, cur_line)
        i += 1
    return total

# TEST | usage : python3.py ex1.py 423692 923857614
import sys
print(entryTime(sys.argv[1], sys.argv[2]))
