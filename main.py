import matplotlib.pyplot as plt


# =========================
# STUDENT DATA
# =========================

student = ["Aman", "Rahul", "Pulkit", "Rohit", "Vikas"]
marks = [60, 85, 95, 75, 64]

study_hours = [1, 4, 5, 3, 2]

subject = ["Python", "Maths", "English", "Computer"]
subject_marks = [85, 72, 78, 90]

months = ["Jan", "Feb", "Mar", "Apr", "May"]
avg_marks = [60, 65, 56, 64, 70]

pass_fail = ["Pass", "Fail"]
pass_fail_count = [4, 1]


# =========================
# 1. STUDY HOURS VS MARKS
# =========================

plt.figure(figsize=(7, 5))

plt.scatter(study_hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid()

plt.show()


# =========================
# 2. SUBJECT MARKS COMPARISON
# =========================

plt.figure(figsize=(7, 5))

plt.barh(subject, subject_marks)

plt.title("Subject Marks Comparison")
plt.xlabel("Marks")
plt.ylabel("Subject")

plt.show()


# =========================
# 3. MARKS DISTRIBUTION
# =========================

plt.figure(figsize=(7, 5))

plt.hist(marks, bins=5)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.grid()

plt.show()


# =========================
# 4. PASS AND FAIL
# =========================

plt.figure(figsize=(7, 7))

plt.pie(
    pass_fail_count,
    labels=pass_fail,
    autopct="%0.1f%%"
)

plt.title("Pass and Fail Students")

plt.show()


# =========================
# 5. MONTHLY PERFORMANCE
# =========================

plt.figure(figsize=(7, 5))

plt.plot(
    months,
    avg_marks,
    marker="o"
)

plt.title("Monthly Performance")
plt.xlabel("Months")
plt.ylabel("Average Marks")
plt.grid()

plt.show()


# =========================
# 6. STUDENT MARKS
# =========================

plt.figure(figsize=(7, 5))

plt.bar(student, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()


# =========================
# 7. FINAL DASHBOARD
# =========================

plt.figure(figsize=(12, 8))


plt.subplot(2, 2, 1)
plt.bar(student, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")


plt.subplot(2, 2, 2)
plt.scatter(study_hours, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid()


plt.subplot(2, 2, 3)
plt.plot(months, avg_marks, marker="o")
plt.title("Monthly Performance")
plt.xlabel("Months")
plt.ylabel("Average Marks")
plt.grid()


plt.subplot(2, 2, 4)
plt.hist(marks, bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.grid()


plt.tight_layout()
plt.show()