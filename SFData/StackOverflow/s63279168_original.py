import tensorflow as tf

(xtrain, ytrain), (xtest, ytest) = tf.keras.datasets.mnist.load_data()

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(16, kernel_size=3, activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=2),
    tf.keras.layers.Conv2D(32, kernel_size=3, activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
    ])

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics='accuracy')

history = model.fit(xtrain, ytrain,
                    validation_data=(xtest, ytest),
                    epochs=10, batch_size=8)