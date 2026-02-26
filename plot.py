import matplotlib.pyplot as plt
import numpy as np

# x = [1,2,3,4,5]
# y = [1,4,9,16,25]

# plt.plot(x,y)
# plt.xlabel("Numbers")
# plt.ylabel("Square")
# plt.title("Square of numbers")
# plt.grid()
# plt.show()

# fig1,axes1 = plt.subplots()

# axes1.plot(y,x)
# axes1.set_title("New Plot")
# axes1.set_xlabel("X-axis")
# axes1.set_ylabel("Y-axis")
# plt.show()

x = np.linspace(0,10,100)
y = np.sin(x)

plt.figure(figsize=(8,5))
plt.plot(x,y,label="SIN")
plt.xlabel("X values")
plt.ylabel("Sin values")
plt.title("Sine wave")
plt.grid()
plt.show()
