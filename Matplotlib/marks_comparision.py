
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

months = ["Jan", "Feb", "Mar", "Apr", "May"]
amit = [20, 25, 30, 28, 35]
sara = [18, 22, 27, 30, 33]
plt.figure(figsize=(9,6))
plt.plot(
    months,
    amit,
    color = "blue",
    marker = "o",
    label = "Amit",
)
plt.plot(
    months,
    sara,
    color = "red",
    marker = "*",
    label = "Sara",
)
plt.legend()
plt.title("Monthly Marks Comparison")
plt.grid(alpha=0.4)
plt.xlabel("Months")
plt.ylabel("Marks")
plt.show()
