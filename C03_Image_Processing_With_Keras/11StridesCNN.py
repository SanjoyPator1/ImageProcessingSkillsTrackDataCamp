# Initialize the model
model = Sequential()

# Add the convolutional layer
model.add(Conv2D(10, kernel_size=3, activation='relu', 
              input_shape=(img_rows, img_cols, 1), 
              strides =2))	# 2 to skip every other pixels

# Feed into output layer
model.add(Flatten())
model.add(Dense(3, activation='softmax'))