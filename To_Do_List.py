goals = []

def add_goal(goal_text):
    goals.append ({"goal": goal_text, "completed":False})
    print("Your goal is added!")

def mark_as_completed(goal_index):
    if 0 <= goal_index < len (goals):
        goals[goal_index]["completed"] = True
        print("Goal is completed")
    else:
        print("Invalid goal index.")

def list_goals():
    print("Goals:")
    for index, goal in enumerate(goals):
        status = "✓" if goal["completed"] else " "
        print(f"{index}: [{status}] {goal['goal']}")

def remove_goal(goal_index):
    if 0 <= goal_index < len(goals):
        remove_goal == goals.pop(goal_index)
        print(f"Goal '{remove_goal['goal']}' removed from your list!")
    else:
        print("Invalid goal.")

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
            goal =input("Write your goal: ")
            add_goal(goal)
        elif choice == "2":
            list_goals()   
            goal_index = int(input("Write the goal index to mark as completed: "))
            mark_as_completed(goal_index) 
        elif choice == "3":
            list_goals()
        elif choice == "4":
            list_goals()
            goal_index = int(input("Write the goal index to remove it: " ))
            remove_goal(goal_index)
        elif choice == "5":
            print("Thank you for using TO DO LIST!")
            break
        else:
            print("Invalid choice. Please write valid choice.")   

if __name__ == "__main__":
    main()
        

        

        





    





