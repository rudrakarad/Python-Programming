import matplotlib.pyplot as plt

students = ["Amit", "Sara", "John", "Riya", "Alex"]
marks = [85, 92, 78, 88, 95]

plt.plot(students,
         marks,
         color = "green",
         linewidth = 3,
         marker = "*",
         linestyle = "--",
         )
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()