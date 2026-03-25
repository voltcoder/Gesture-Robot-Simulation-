threshold = 0.5

if np.mean(filtered_signal) > threshold:
    gesture = "Strong Flex (Close Hand)"
else:
    gesture = "Relax (Open Hand)"

print("Detected Gesture:", gesture)
