def comp_median(list):
    list.sort()
    if len(list) % 2 == 0:
        return (list[len(list)//2] + (list[len(list)//2 + 1])) / 2
    else:
        return list[len(list)//2]

def comp_mode(list):
    list.sort
    counts = {} # type: ignore
    for num in list:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    most_count = max(counts.values())
    most_frequent_number = [num for num, count in counts.items() if count == most_count]
    for num in most_frequent_number:
        return num
            
def comp_mean(list):
    return sum(list) / len(list)

contents_of_list = input("Enter numbers to be put in the list separated by space: ").strip().split()
num_list = [float(num) for num in contents_of_list]
print(f"The median of the list is {comp_median(num_list):.3f}.")
print(f"The mode of the list is {comp_mode(num_list):.3f}.")
print(f"The mean of the list is {comp_mean(num_list):.3f}.")