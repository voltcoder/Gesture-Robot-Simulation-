import numpy as np
import matplotlib.pyplot as plt

# simulate EMG signal
time = np.linspace(0, 1, 100)
signal = np.sin(10 * time) + np.random.normal(0, 0.5, 100)

plt.plot(signal)
plt.title("Simulated EMG Signal")
plt.show()
