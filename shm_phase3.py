import random

# Simulate vibration data from 10 sensors
num_sensors = 10
data = [random.uniform(0, 2) for _ in range(num_sensors)]

# Introduce damage at sensor 5
data[4] += 5

# Set vibration threshold
threshold = 3.0

# Check for damage
for i, value in enumerate(data, 1):
    status = "DAMAGED" if value > threshold else "Healthy"
    print(f"Sensor {i}: {status} (Value: {value:.2f})")
