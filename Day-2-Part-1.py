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

increasing_dercreasing_list = copy.deepcopy(list_of_lists)

def sort_list(list):
    for item in list:
        if item[0] <= item[1]:
            item.sort()
        else:
            item.sort(reverse = True)

sort_list(increasing_dercreasing_list)

partially_correct_list = []
def remove_unsafe_round1(list1, list2):
    for index, item in enumerate(list1):
        if item == list2[index]:
            partially_correct_list.append(item)
 
remove_unsafe_round1(list_of_lists, increasing_dercreasing_list)
# print(partially_correct_list)

def check_if_safe(list):
    safe_count = 0
    for item in list:
        correct_dif = 0
        for index, digit in enumerate(item):
            if len(item) -1 != index:
                dif = abs(digit - item[index + 1])
                if dif >= 1 and dif <=3:
                    correct_dif += 1
        if correct_dif == len(item) - 1:
            safe_count +=1
    return safe_count
                
print(check_if_safe(partially_correct_list))