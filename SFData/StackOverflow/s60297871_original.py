classifier = Sequential()
classifier.add(Dense(6,kernel_initializer='random_uniform',activation='relu',input_dim=11))
classifier.add(Dense(6,kernel_initializer='random_uniform',activation='relu'))
classifier.add(Dense(1,activation='sigmoid'))
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
classifier.fit(x_train, y_train, batch_size = 10, epochs = 100)