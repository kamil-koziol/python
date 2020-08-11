import tensorflow as tf
from tensorflow import keras

data = tf.keras.datasets.mnist

(train_x, train_y), (test_x, test_y) = data.load_data()

train_x = train_x / 255
test_x = test_x / 255

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(256, activation=tf.nn.relu),
    tf.keras.layers.Dense(10,activation=tf.nn.softmax)
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(train_x, train_y, epochs=2)

model.save("model.h5")

