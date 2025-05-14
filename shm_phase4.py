# Ground truth and predictions
actual = [1, 0, 1, 1, 0, 0, 1, 0]
predicted = [1, 0, 1, 0, 0, 0, 1, 1]

# 1. Accuracy
correct = 0
for i in range(len(actual)):
    if actual[i] == predicted[i]:
        correct += 1

accuracy = correct / len(actual)
print("Accuracy:", accuracy)

# 2. Confusion Matrix and Other Metrics
TP = TN = FP = FN = 0

for i in range(len(actual)):
    if actual[i] == 1 and predicted[i] == 1:
        TP += 1
    elif actual[i] == 0 and predicted[i] == 0:
        TN += 1
    elif actual[i] == 0 and predicted[i] == 1:
        FP += 1
    elif actual[i] == 1 and predicted[i] == 0:
        FN += 1

print("True Positives:", TP)
print("True Negatives:", TN)
print("False Positives:", FP)
print("False Negatives:", FN)

# Metrics
precision = TP / (TP + FP) if (TP + FP) != 0 else 0
recall = TP / (TP + FN) if (TP + FN) != 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0

print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# 3. Signal Data Metrics
signal = [0.2, 0.5, 0.3, 0.8, 0.6]

mean_value = sum(signal) / len(signal)
max_value = max(signal)
rms_value = (sum(x**2 for x in signal) / len(signal)) ** 0.5

print("Signal Mean Value:", mean_value)
print("Signal Max Value:", max_value)
print("Signal RMS Value:", rms_value)
