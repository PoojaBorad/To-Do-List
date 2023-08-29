goals = []

def add_goal(goal_text):
    goals_list =goal_text.split(";") 
    for goal in goals_list:
        goals.append({"goal":goal.strip(), "completed": False})
        print("Your goal is added!\n")


def mark_as_completed(goal_positions):
    for goal_index in goal_positions:

        if 0 <= goal_index < len (goals):
           goals[goal_index]["completed"] = True
           print(f"Goal{goal_index} is completed\n")
        else:
           print(f"Invalid goal index {goal_index}.\n")

def list_goals():
    print("Goals:")
    for index, goal in enumerate(goals):
        status = "✓" if goal["completed"] else " "
        print(f"{index}: [{status}] {goal['goal']}\n")

def removed_goal(goal_index):
    if 0 <= goal_index < len(goals):
        removed_goal == goals.pop(goal_index)
        print(f"Goal '{removed_goal['goal']}' removed from your list!\n")
    else:
        print("Invalid goal index.\n")

def main():
    while True:
        print(" Select Number From Menu:")
        print("1. Add New Goal")
        print("2. Marked Goal as Completed")
        print("3. List Goal")       
        print("4. Remove Goal From List")
        print("5. Exit")

        choice = input("Select your choice: ")

        if choice == "1":
            goal_text =input("Write your goals : ")
            add_goal(goal_text)
        elif choice == "2":
            list_goals()   
            goal_positions = input("Write goal numbers (comma-separated) to mark as completed: ")
            goal_positions = [int(position.strip()) for position in goal_positions.split(",")]
            mark_as_completed(goal_positions) 
        elif choice == "3":
            list_goals()
        elif choice == "4":
            list_goals()
            goal_index = int(input("Write the goal index to remove it: " ))
            removed_goal(goal_index)
        elif choice == "5":
            print("Thank you for using TO DO LIST!")
            break
        else:
            print("Invalid choice. Please write valid choice.")   

if __name__ == "__main__":
    main()            


    
        

        

        





    





