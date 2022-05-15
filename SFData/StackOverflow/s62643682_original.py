inputs = keras.Input(shape=(29,29,1))

x=inputs

x = keras.layers.Conv2D(16, kernel_size=(3,3), name='Conv_1')(x)
x = keras.layers.LeakyReLU(0.1)(x)
x = keras.layers.MaxPool2D((2,2), name='MaxPool_1')(x)

x = keras.layers.Conv2D(16, kernel_size=(3,3), name='Conv_2')(x)
x = keras.layers.LeakyReLU(0.1)(x)
x = keras.layers.MaxPool2D((2,2), name='MaxPool_2')(x)

x = keras.layers.Conv2D(32, kernel_size=(3,3), name='Conv_3')(x)
x = keras.layers.LeakyReLU(0.1)(x)
x = keras.layers.MaxPool2D((2,2), name='MaxPool_3')(x)
x = keras.layers.Flatten(name='Flatten')(x)

x = keras.layers.Dense(64, name='Dense_1')(x)
x = keras.layers.ReLU(name='ReLU_dense_1')(x)
x = keras.layers.Dense(64, name='Dense_2')(x)
x = keras.layers.ReLU(name='ReLU_dense_2')(x)

outputs = keras.layers.Dense(4, activation='softmax', name='Output')(x)

model = keras.Model(inputs=inputs, outputs=outputs, name='VGGlike_CNN')
model.summary()

keras.utils.plot_model(model, show_shapes=True)

OPTIMIZER = tf.keras.optimizers.Adam(learning_rate=LR_ST)

model.compile(optimizer=OPTIMIZER,
              loss='categorical_crossentropy',
              metrics=['accuracy'],
              run_eagerly=False)

def lr_decay(epoch):
  if epoch < 10:
    return LR_ST
  else:
    return LR_ST * tf.math.exp(0.2 * (10 - epoch))

lr_scheduler = keras.callbacks.LearningRateScheduler(lr_decay)


model_checkpoint = keras.callbacks.ModelCheckpoint(
        filepath='mycnn_best',
        monitor='val_accuracy',
        save_weights_only=True,
        save_best_only=True,
        save_freq='epoch')

callbacks = [ lr_scheduler, model_checkpoint ]

print('X_train.shape = ',X_train.shape)

history = model.fit(X_train, Y_train epochs=50,
                    validation_data=X_test, shuffle=True, verbose=1,
                    callbacks=callbacks)