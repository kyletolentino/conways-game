import numpy as np
import pickle
import tensorflow as tf

# put these first for ease when tuning
epoch_size = 20
batch = 128

# tried to use pandas and csv
# but modern problems require modern solutions (right?)
data = pickle.load(open("data.pkl", 'rb'))

x1 = data[0]
x2 = data[1]
y = data[2]

# turn these into numpy arrays
x1 = np.array([m for m in x1])
x2 = np.array([m for m in x2])
y = np.array(y)

# this is a basic, plain MLP neural network

# doing a shared layer, then will concatenate dual inputs
x1_input = tf.keras.Input(shape=(3, 3))
x2_input = tf.keras.Input(shape=(3, 3))

layer1 = tf.keras.layers.Dense(64, activation='relu')
x1_layer = layer1(x1_input)
x2_layer = layer1(x2_input)

# combine the two input layers into 1, then flatten them
merged_vector = tf.keras.layers.concatenate([x1_layer, x2_layer], axis=-1)
flat_layer = tf.keras.layers.Flatten()(merged_vector)

# created another layer so optimizer can learn
# chose 32 because half of input neurons
dense2 = tf.keras.layers.Dense(64, activation='relu')(flat_layer)

# end with 1 neuron b/c binary classification
predictions = tf.keras.layers.Dense(1, activation='sigmoid')(dense2)

model = tf.keras.Model(inputs=[x1_input, x2_input], outputs=predictions)

# SGD + momentum optimizer for shallow networks
# binary_crossentropy b/c binary classification
model.compile(loss='binary_crossentropy',
              optimizer=tf.keras.optimizers.SGD(lr=0.01, nesterov=True),
              metrics=['accuracy'])

model.summary()

# if we see validation loss decreasing for 3 epochs, stop training
callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)

# 20% of training data will be validation
history = model.fit([x1, x2], y, epochs=epoch_size, batch_size=batch,
                    validation_split=0.2, callbacks=[callback], shuffle=True)

# save keras model to test on another file
model.save('keras_MLP.h5')

# NOTE:
# - [0,1] : closer to 1 indicates correct sequence
# - you MUST reshape numpy arrays into (# of samples, 3, 3)
#   i.e. if you want to just compare 2 matrices, it would be:
#   (1, 3, 3)
#
# - to use model.predict, you have to
#   supply two numpy arrays in a list
#   i.e. model.predict([state1, state2])
