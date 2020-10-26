n = int(input())

parking = set()

for _ in range(n):
    direction, regnum = input().split(", ")
    if direction == "IN":
        parking.add(regnum)
    elif direction == "OUT":
        if regnum in parking:
            parking.remove(regnum)

if parking:
    print("\n".join(parking))
else:
    print("Parking Lot is Empty")