def delet():
    element = []
    n = int(input())
    for i in range(n):
        element.append(int(input()))
    final_list = []
    for num in element:
        if num not in final_list:
            final_list.append(num)
    return final_list


print(delet())
