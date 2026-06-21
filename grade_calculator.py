for i in range(1, 3):
    print(f"\nStudent {i}")

    name = input("Enter student name: ")

    print(f"\nEnter marks for {name}")

    marks = []

    for j in range(4):
        mark = int(input(f"Enter mark for Subject {j+1}: "))
        marks.append(mark)

    average = sum(marks) / len(marks)

    print(f"\nStudent: {name}")
    print(f"Average Marks: {average:.2f}")

    if average >= 90:
        print("Excellent")
    elif average >= 80:
        print("Good")
    elif average >= 70:
        print("Decent")
    elif average >= 60:
        print("Improvement is needed")
    else:
        print("You have failed")