import numpy as np
import matplotlib.pyplot as plt

# dataset settings
data_length = 100
max_offset = 30
max_m = 10
max_q = 20 

# dataset compiling
ideal_m = np.random.random() * np.random.randint(0, max_m)
ideal_q = np.random.randint(0, max_q) + np.random.random()
random_offset = np.random.randint(0, max_offset, size=data_length) + np.random.random(data_length)
data_y = np.array( [ ideal_m * x + ideal_q for x in range(data_length) ] ) + random_offset
data_x = np.array( [x for x in range(data_length)] )

# linear regression
x_mean = np.mean(data_x)
y_mean = np.mean(data_y)
SSxy = np.sum(data_x * data_y) - data_length * x_mean * y_mean 
SSxx = np.sum(data_x * data_x) - data_length * x_mean ** 2
m = SSxy / SSxx
q = y_mean - m * x_mean

# logging results
print(f'Original:\n{ideal_m=} {ideal_q=}')
print(f'Predicted:\n{m=} {q=}')

# plotting results
plt.scatter(data_x, data_y, c='w', edgecolors='k', s=10, label='Dataset')
plt.plot(data_x, np.array( [m * x + q for x in range(data_length)] ), c='r', label='Regression line')

# plot aesthetics
plt.grid(c='c', linestyle=':')
plt.title('LINEAR REGRESSION')
plt.xlabel('X axis', c='r')
plt.ylabel('Y axis', c='b')
plt.legend(shadow= True)
plt.show()
