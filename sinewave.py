# Import
import numpy as np
import matplotlib.pyplot as plt

# Generate x values (time)
x = np.linspace(0, 10, 1000)  # Time values from 0 to 10 seconds

# Generate y values (sine wave)
frequency = 1  # Frequency of the sine wave in Hz
amplitude = 1  # Amplitude of the sine wave
y = amplitude * np.sin(2 * np.pi * frequency * x)

# Plot the sine wave
plt.plot(x, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sine Wave')
plt.grid(True)
plt.show()