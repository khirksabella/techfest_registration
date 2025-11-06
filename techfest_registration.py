# Tech Fest Midterm Exam
# TASK 1
from enum import unique

print("Welcome to SMIT TechFest!")
print("Event organized by Khirk of APPDAET BTCS2")
print("\n")

parti = int(input("How many participants will register? "))
if parti <= 0:
    print("Invalid number of participants.")
    exit()

# TASK 2
participants = []
for i in range(parti):
    name = (input(f"Enter participant #{i+1} name: "))
    track = (input("Enter chosen track: "))
    participants.append({"name": name,  "track": track})

print("\n")
print("Registered Participants:")
for i in range(len(participants)):
    print(f"{i + 1}. {participants[i]['name']} - {participants[i]['track']}")

# TASK 3
unique = {i ["track"] for i in participants}
print("\n")
print("Tracks Offered: ")
if len(unique) < 2:
    print("Not enough variety in tracks.")
else:
    print(" ".join(unique))

# TASK 4
print("\n")

name_checker = set()
duplicate_found = False
for i in range(len(participants)):
    if participants[i]['name'] in name_checker:
        print("Duplicate name found: " + participants[i]['name'])
        duplicate_found = True
    else:
        name_checker.add(participants[i]['name'])

if not duplicate_found:
    print("No duplicate names.")





