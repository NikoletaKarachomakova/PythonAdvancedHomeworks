clothes = list(map(int, input().split()))
rack_capacity = int(input())
rack_count = 0
current_capacity = 0

while len(clothes) > 0:
    while current_capacity <= rack_capacity:
        index = len(clothes) - 1
        current_capacity += clothes[index]

        if current_capacity <= rack_capacity:
            clothes.pop()
            if index == 0:
                rack_count +=1
                break
            if current_capacity == rack_capacity:
                rack_count += 1
                current_capacity = 0

        else:
            current_capacity = 0
            rack_count += 1
            if index == 0:
                rack_count += 1
                clothes.pop()
                break
            continue

print(rack_count)


