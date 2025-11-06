# Tech Fest Midterm Exam
# TASK 1
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

