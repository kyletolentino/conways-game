import numpy as np
import pickle
import matplotlib.pyplot as plt
import tensorflow as tf

# put these first for ease when tuning
epoch_size = 50
batch = 128

# tried to use pandas and csv
# but modern problems require modern solutions (right?)
data = pickle.load(open("data.pkl", 'rb'))

x1 = data[0]
x2 = data[1]
y = data[2]

x1 = np.array([m for m in x1])
x2 = np.array([m for m in x2])
y = np.array(y)

# doing a shared layer, then will concatenate dual inputs
x_input = tf.keras.Input(shape=(3, 3))

layer1 = tf.keras.layers.Dense(64, activation='relu')
x1_layer = layer1(x_input)
x2_layer = layer1(x_input)

merged_vector = tf.keras.layers.concatenate([x1_layer, x2_layer], axis=-1)
flat_layer = tf.keras.layers.Flatten()(merged_vector)
dense2 = tf.keras.layers.Dense(32, activation='relu')(flat_layer)
predictions = tf.keras.layers.Dense(1, activation='sigmoid')(dense2)

model = tf.keras.Model(inputs=x_input, outputs=predictions)

# SGD + momentum optimizer for shallow networks
model.compile(loss='binary_crossentropy',
              optimizer=tf.keras.optimizers.SGD(lr=0.01, nesterov=True),
              metrics=['accuracy'])

model.summary()

# if we see validation loss decreasing, stop training
callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)

history = model.fit(x1+x2, y, epochs=epoch_size, batch_size=batch,
                    validation_split=0.2, callbacks=[callback], shuffle=True)

model.save('keras_MLP.h5')
