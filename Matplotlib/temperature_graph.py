
import matplotlib.pyplot as plt

Months = ["Jan", "Feb", "Mar", "Apr", "May"]
Temperature = [22, 25, 30, 35, 32]

plt.plot(Months,
         Temperature,
         color = "Blue",
         linestyle = "--",
         marker = "o",
         linewidth = 2
         )
plt.title("Monthly Temperature")
plt.xlabel("Months")
plt.ylabel("Temperature ")
plt.show()