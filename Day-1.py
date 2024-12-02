raw_list = '''84283   63343
35360   98209
17841   84541
22035   44413
43645   22440'''

raw_list = raw_list.replace("\n", "   ")
combined_list = raw_list.split("   ")

combined_number_list = []
def convert_to_numbers(list):
    for item in list:
        combined_number_list.append(int(item))

convert_to_numbers(combined_list)

list_1 = []
list_2 = []
def separate_lists(list):
    for index, item in enumerate(list):
        if index % 2 == 0:
            list_1.append(item)
        else:
            list_2.append(item)

separate_lists(combined_number_list)

list_1.sort()
list_2.sort()

def compare_lists(list1, list2):
    difference = 0
    for index, item in enumerate(list1):
        difference += abs(item - list2[index])
    return difference

print(compare_lists(list_1, list_2))

def similarity(list1, list2):
    score = 0
    for item in list1:
        score += item * list2.count(item)
    return score

print(similarity(list_1, list_2))