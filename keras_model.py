import numpy as np
import pickle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import tensorflow as tf

# put these first for ease when tuning
epoch_size = 20
batch = 512

# tried to use pandas and csv
# but modern problems require modern solutions (right?)
data = pickle.load(open("data.pkl", 'rb'))

x1 = data[0]
x2 = data[1]
y = data[2]

# merge both matrices into one to identify trends - possibly CNN approach
# will have to concatenate test data (i.e. when given two numpy arrays)
X = np.concatenate((x1, x2), axis=1)

# random_state should always be kept the same for model selection
# I picked random_state = 7 ;)
X_train, X_val, y_train, y_val = train_test_split(X, y, random_state=7, test_size=0.2)


model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, input_shape=(6, 3), activation='relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.summary()

# if we see validation loss decreasing, stop training
callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)

history = model.fit(X_train, y_train, epochs=epoch_size, batch_size=batch,
                    validation_data=(X_val, y_val), callbacks=[callback], shuffle=True)


def plot_graphs(history, string):
    plt.plot(history.history[string])
    plt.plot(history.history['val_'+string], '')
    plt.xlabel("Epochs")
    plt.ylabel(string)
    plt.legend([string, 'val_'+string])
    plt.show()


plot_graphs(history, 'acc')
plot_graphs(history, 'loss')

