available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive"]
print("Enter 0 to exit")
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
current_choice = "-"
computer_parts = []  # create an empty list
while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print(" your list now contains {}".format(computer_parts))
        # if current_choice == "1":
        #     computer_parts.append("computer")
        # elif current_choice == "2":
        #     computer_parts.append("monitor")
        # elif current_choice == "3":
        #     computer_parts.append("keyboard")
        # elif current_choice == "4":
        #     computer_parts.append("mouse")
        # elif current_choice == "5":
        #     computer_parts.append("mouse mat")
        # elif current_choice == "6":
        #     computer_parts.append("hdmi cable")
        # or
    else:
        print("please add options from the list")
        # for part in available_parts:
        #     print("{0}: {1}" .format(available_parts.index(part)+1 , part))
        # +1 kuki 0 se start hta h n we dnt want 0 to get listed
        # or
        for number, part in enumerate(available_parts):  # enumrate function is more efficient
            print("{0}: {1}".format(number + 1, part))
    current_choice = input()
print(computer_parts)

# eg for enumerate
# for index , character in enumerate("abcdefgh"):
#     print(index , character)
