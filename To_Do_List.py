goals = []

def add_goal(goal):
    goal.append ({"goal": goal, "completed":False})
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
        print(f"{index}: [{status}] {goal['description']}")
        
                


