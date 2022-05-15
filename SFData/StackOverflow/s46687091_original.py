input_data = tf.placeholder(tf.int32, shape=[batch_size, embedding_size])
labels = tf.placeholder(tf.int32, shape=[batch_size, 1])
dropout_keep_prob = tf.placeholder_with_default(1.0, shape=())

nce_weights = tf.Variable(tf.truncated_normal([vocabulary_size, batch_size], stddev=1.0 / math.sqrt(embedding_size)))

nce_biases = tf.Variable(tf.zeros([vocabulary_size]))
embed = tf.nn.embedding_lookup(tf.convert_to_tensor(glove_embeddings_arr), input_data)

loss = tf.reduce_mean(tf.nn.nce_loss(weights=nce_weights, biases=nce_biases, labels=labels, inputs=tf.reduce_sum(embed, 1), num_sampled=num_sampled, num_classes=vocabulary_size))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=1.0).minimize(loss)

accuracy=0

return input_data, labels, dropout_keep_prob, optimizer, accuracy, loss