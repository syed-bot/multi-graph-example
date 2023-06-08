import matplotlib.pyplot as plt
import numpy as np

# Generate the x-values (months)
months = np.arange(1, 201)

# Generate the datasets
np.random.seed(42)  # For reproducibility

# Dataset 1: Monthly Electricity Consumption
electricity_consumption = np.random.randint(100, 1000, size=200)  # Random consumption values (kWh)

# Dataset 2: Average Temperature
average_temperature = np.random.normal(25, 5, size=200)  # Random temperature values (°C)

# Dataset 3: Monthly Electricity Prices
electricity_prices = np.random.uniform(0.10, 0.20, size=200)  # Random price values ($/kWh)

# Create the figure and axes objects
fig, ax1 = plt.subplots()

# Plot Monthly Electricity Consumption on the primary y-axis
ax1.plot(months, electricity_consumption, 'g-', label='Electricity Consumption')
ax1.set_xlabel('Months')
ax1.set_ylabel('Electricity Consumption (kWh)', color='g')
ax1.tick_params('y', colors='g')

# Create a secondary y-axis
ax2 = ax1.twinx()

# Plot Average Temperature on the secondary y-axis
ax2.plot(months, average_temperature, 'b--', label='Average Temperature')
ax2.set_ylabel('Average Temperature (°C)', color='b')
ax2.tick_params('y', colors='b')

# Create a third y-axis
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))

# Plot Monthly Electricity Prices on the third y-axis
ax3.plot(months, electricity_prices, 'r-.', label='Electricity Prices')
ax3.set_ylabel('Electricity Prices ($/kWh)', color='r')
ax3.tick_params('y', colors='r')

# Display legends and title
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='lower right')
plt.title('Monthly Electricity Consumption, Average Temperature, and Electricity Prices')

# Show the plot
plt.show()
