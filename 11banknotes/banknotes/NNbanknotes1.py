import csv
import tensorflow as tf

from sklearn.model_selection import train_test_split

# Read data in from file
with open("banknotes.csv") as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": "Authentic" if row[4] == "0" else "Counterfeit"
        })

# Separate data into training and testing groups
evidence = [row["evidence"] for row in data]
labels = [row["label"] for row in data]

X_training, X_testing, y_training, y_testing = train_test_split(
    evidence, labels, test_size=0.4
)

# Create neural network, sequential, layer after another
model = tf.keras.models.Sequential()

# Add hidden layer with 8 units, RELU activation, Dense = each node connected to previous layer
model.add(tf.keras.layers.Dense(8, input_shape=(4,), activation="relu"))

# Add output layer with 1 unit, sigmoid activation
model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

# train Neural network
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]    
)

# Train how many epochs
model.fit(X_training, y_training, epochs=10)

# Evaluate how well model performs
model.evaluate(X_testing, y_testing, verbose=2)