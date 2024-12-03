import copy

input = '''2 5 6 8 6
87 89 90 93 96 99 99
13 14 15 18 19 23
67 69 71 72 73 76 82
29 32 30 31 34 35 37'''

split_input = input.split("\n")


list_of_lists = []
def split_lists(list):
    for item in list:
        list_of_lists.append(item.split(" "))

split_lists(split_input)

def make_numbers(list):
    new_list = []
    for item in list:
        line_item_list = []
        for digit in item:
            line_item_list.append(int(digit))
        new_list.append(line_item_list)
    return new_list 

list_of_lists = make_numbers(list_of_lists)
print(list_of_lists)

safe_count = 0

def is_line_safe(line):
    sorted_line = copy.deepcopy(line)
    if sorted_line[0] <= sorted_line[1]:
        sorted_line.sort()
    else:
        sorted_line.sort(reverse = True)
    if line != sorted_line:
        return False
    
    correct_dif = 0
    for index, digit in enumerate(line):
        if len(line) -1 != index:
            dif = abs(digit - line[index + 1])
            if dif >= 1 and dif <=3:
                correct_dif += 1
    if correct_dif != len(line) - 1:
        return False

    return True

for line in list_of_lists:
    if is_line_safe(line):
        safe_count += 1
    else:
        for index, item in enumerate(line):
            line_copy = copy.deepcopy(line)
            line_copy.pop(index)
            if is_line_safe(line_copy):
                safe_count +=1
                break

print(safe_count)
