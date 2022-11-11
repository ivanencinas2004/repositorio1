# This is a sample Python script.
import pandas as pd
import matplotlib.pyplot as plt

z1 = ['sudadera', 20]
z2 = ['camiseta', 10]
z3 = ['calcetines', 5]
z4 = ['chaqueta', 30]
z5 = ['zapatos', 35]
listaropa= [z1,z2,z3,z4,z5]
ropa = pd.DataFrame(listaropa,columns=['precio', 'color'])
print(ropa)

plt.scatter(ropa['precio'], ropa['color'])
plt.show()

plt.plot(ropa['precio'], ropa['color'])
plt.show()

plt.barh(ropa['precio'], ropa['color'])
plt.show()

plt.bar(ropa['precio'], ropa['color'])
plt.show()


