import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Generate synthetic training data
def generate_training_data(n=300):
    X = []
    y = []
    for _ in range(n):
        v = round(random.uniform(1.5, 9.0), 2)
        if v <= 5.0:
            label = 0  # Normal
        elif v <= 7.0:
            label = 1  # Minor Damage
        else:
            label = 2  # Major Damage
        X.append([v])
        y.append(label)
    return X, y

# Step 2: Train a Random Forest model
X, y = generate_training_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 3: Test accuracy
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred) * 100, "%")

# Step 4: Predict on new user data
print("\n=== AI STRUCTURAL HEALTH MONITORING ===\n")
new_data = input("Enter vibration values separated by commas (e.g., 2.3,6.8,8.1): ")
values = [float(x.strip()) for x in new_data.split(',')]

predictions = model.predict([[v] for v in values])

labels = {0: "Normal", 1: "Minor Damage", 2: "Major Damage"}

for i, (v, p) in enumerate(zip(values, predictions)):
    print(f"Point {i+1}: Vibration = {v} → {labels[p]}")

# Step 5: Summary
total = len(predictions)
minor = sum(1 for p in predictions if p == 1)
major = sum(1 for p in predictions if p == 2)

print("\n--- SYSTEM SUMMARY ---")
print("Total Points Monitored:", total)
print("Minor Damage Cases:", minor)
print("Major Damage Cases:", major)

if major > 0:
    print("Status: CRITICAL – Immediate Inspection Needed.")
elif minor > 0:
    print("Status: MINOR ISSUES – Inspection Advised.")
else:
    print("Status: STRUCTURE IS HEALTHY.")