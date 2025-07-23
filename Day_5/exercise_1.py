def return_distincts(first, second, third):

    num_list = [first,second,third]
    num_list.sort()

    total = sum(num_list)

    if total > 15:
        return num_list[2]
    elif total < 10:
        return num_list[0]
    else:
        return num_list[1]
    
print(return_distincts(1,20,2))