task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
   case "high" if time_bound == "yes":
      print(f"{task} is a high priority task that requires immediate attention!")
   case "high" if time_bound == "no":
      print(f"{task} is a high priority task that does not require timely attention")
   case "medium" if time_bound == "yes":
      print(f"{task} is a medium priority task that requires timely attention")
   case "medium" if time_bound == "no":
      print(f"{task} is a medium priority task that does not require timely attention")
   case "low" if time_bound == "high":
      print(f"{task} is a low priority task that requires timely attention")
   case "low" if time_bound == "no":
      print(f"{task} is a low priority task that does not require timely attention")
   case _:
      print("Invalid priority")
