assignments = ["Assignment 1", "Assignment 2", "Assignment 3"]

print("Initial list of assignments:",assignments)


assignments.append("assignment4")
print("Added Assignment4 to the list of assignments.")


completed_assignment=input("Enter completed assignment to remove: ")
if completed_assignment in assignments:
    assignments.remove(completed_assignment)
    print(f"Removed '{completed_assignment}' from the list of assignments (completed).")
    print("updated list: ",assignments)

else:

    print(f"'{completed_assignment}' is not found in the list of assignments.")

    print("\nUpdated list of assignments:")
    print(assignments)