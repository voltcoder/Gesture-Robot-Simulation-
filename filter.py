def moving_average(signal, window_size=5):
    return np.convolve(signal, np.ones(window_size)/window_size, mode='valid')

filtered_signal = moving_average(signal)

plt.plot(filtered_signal)
plt.title("Filtered Signal")
plt.show()
