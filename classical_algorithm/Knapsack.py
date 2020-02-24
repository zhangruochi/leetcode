weight = [10,20,15,8]
values = [2,7,4,8]

Max_ = 29
max_value = 0
max_value_path = None



def backpack( path, cur_weight, cur_value, pos):
    global max_value, max_value_path, Max_

    if pos == len(weight):
        if cur_weight <= Max_:
            if max_value < cur_value:
                max_value = cur_value
                max_value_path = path[:]

        return 


    backpack(path, cur_weight, cur_value, pos+1)

    if cur_weight + weight[pos] <= Max_:
        backpack(path + [pos], cur_weight + weight[pos], cur_value + values[pos], pos+1)

    return ;


# backpack([], 0, 0, 0)

# print(max_value_path)
# print(max_value)


def backpack( path, cur_weight, cur_value, pos):
    global max_value, max_value_path, Max_

    if pos == len(weight):
        if cur_weight <= Max_:
            if max_value < cur_value:
                max_value = cur_value
                max_value_path = path[:]

        return 


    for i in range(pos, len(weight)):
        path.append(i)
        backpack(path, cur_weight + weight[i], cur_value + values[i], i+1)
        path.pop()

    return ;


backpack([], 0, 0, 0)

print(max_value_path)
print(max_value)

