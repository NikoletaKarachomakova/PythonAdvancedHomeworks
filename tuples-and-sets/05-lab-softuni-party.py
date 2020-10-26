number = int(input())

invited = set()
guests = set()
for _ in range(number):
    invited.add(input())

command = input()
while command != "END":
    guests.add(command)
    command = input()

not_attended = invited - guests
print(len(not_attended))
print("\n".join(sorted(not_attended)))