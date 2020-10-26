from _collections import deque

start_qnt = int(input())
name = input()
queue_name = deque()

while name != "Start":
    queue_name.append(name)
    name = input()

command = input()
while command != "End":
    tokens = command.split()
    # isnumeric  - samo za polojitelni chisla - po-dobre s isnumeric, zashtoto eliminira bug-ovete s otricatelni chisla
    # naj-dobre s isdigit, po-dobyr i po-konservativen nachin, isnumeric razbira i ietoglifni chisla
    # command.startswith
    if tokens[0] != "refill":
        wanted_water = int(tokens[0])
        index_first_person = 0
        if start_qnt >= wanted_water:
            start_qnt -= wanted_water
            print(f"{queue_name[index_first_person]} got water")
            queue_name.popleft()

        else:
            print(f"{queue_name[index_first_person]} must wait")
            queue_name.popleft()
    else:
        start_qnt += int(tokens[1])

    command = input()

print(f"{start_qnt} liters left")