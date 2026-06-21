# 🎓 Student Grade Calculator

## 📌 Project Description

The **Student Grade Calculator** is a Python-based application that processes the marks of multiple students, calculates their average marks, assigns grades based on a predefined grading system, provides personalized comments, and displays class statistics. The program also includes input validation, error handling, student search functionality, and an option to save results to a text file.

---

## 🚀 Features

- Process multiple students
- Calculate average marks
- Assign grades automatically
- Display personalized comments
- Calculate class statistics
  - Class Average
  - Highest Average
  - Lowest Average
- Display results in a formatted table
- Color-coded grades in the terminal
- Validate user inputs
- Handle invalid inputs using exception handling
- Search for a student by name
- Save results to a text file

---

## 📚 Concepts Used

- Variables
- Data Types
- Lists
- Functions
- Conditional Statements (`if`, `elif`, `else`)
- Loops (`for`, `while`)
- Exception Handling (`try-except`)
- File Handling
- String Formatting
- ANSI Escape Codes (Terminal Colors)

---

## 🛠️ Requirements

- Python 3.8 or above

No external libraries are required.

---

## ▶️ How to Run

1. Open a terminal.
2. Navigate to the project folder.

```bash
cd week2-grade-calculator
```

3. Run the program.

```bash
python grade_calculator.py
```

---

## 📊 Grading System

| Average Marks | Grade | Comment |
|--------------|-------|------------------------|
| 90 - 100 | A | Excellent |
| 80 - 89 | B | Very Good |
| 70 - 79 | C | Good |
| 60 - 69 | D | Needs Improvement |
| 0 - 59 | F | Failed |

---

## 📋 Sample Output

```
===========================================
      STUDENT GRADE CALCULATOR
===========================================

Enter number of students: 2

Student 1
Enter Name: John

Enter marks for John
Subject 1: 85
Subject 2: 92
Subject 3: 88

Student 2
Enter Name: Sarah

Enter marks for Sarah
Subject 1: 78
Subject 2: 81
Subject 3: 85

===========================================
RESULTS
===========================================

Name            Average     Grade     Comment
-----------------------------------------------------
John             88.33        B       Very Good
Sarah            81.33        B       Very Good

===========================================
Class Statistics
===========================================
Total Students : 2
Class Average  : 84.83
Highest Average: 88.33
Lowest Average : 81.33
```

---

## 📁 Project Structure

```
week2-grade-calculator/
│
├── grade_calculator.py
├── student_results.txt
├── README.md
└── test_students.txt
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

- How to write reusable functions
- How to validate user input
- How to use loops efficiently
- How to implement conditional logic
- How to store and manipulate data using lists
- How to calculate statistics
- How to handle exceptions gracefully
- How to save data into a text file

---

## 🔍 Challenges Faced

### Challenge 1
Handling invalid user input.

**Solution:** Used `try-except` blocks with `while` loops to repeatedly request valid input.

### Challenge 2
Displaying data in a neat table.

**Solution:** Used formatted strings and alignment specifiers.

### Challenge 3
Managing multiple students' data.

**Solution:** Stored information in lists and dictionaries for easy access.

---

## 📌 Future Improvements

- Add percentage calculation
- Export results to CSV or Excel
- Add graphical user interface (GUI)
- Store student records in a database
- Generate printable report cards

---

## 👨‍💻 Author

**Name:** Your Name

---

## 📄 License

This project is created for educational purposes.
