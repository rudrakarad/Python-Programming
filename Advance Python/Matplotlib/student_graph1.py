import matplotlib.pyplot as plt

students = ["Rudra", "Manali", "Varad", "Aryan", "Samyak"]
marks = [83, 74, 64, 35, 54]

plt.bar(students, marks)
plt.title("FYIT Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()