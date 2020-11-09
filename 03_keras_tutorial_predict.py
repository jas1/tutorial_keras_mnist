import os
from dotenv import load_dotenv

import json
import numpy as np
import mnist

from tensorflow import keras
from tensorflow.keras.models import model_from_json

load_dotenv()

model_weights_file_name=os.getenv("KERAS_TUTORIAL_WEIGHTS_H5")
model_out_name=os.getenv("KERAS_TUTORIAL_MODEL_JSON")

# load model from json
model_json_file_con = open(model_out_name,'r')
model_json_file_text = model_json_file_con.read()
model_json_file_con.close()

model = model_from_json(model_json_file_text)

# load weigths
model.load_weights(model_weights_file_name)


# todo: can be better as it is processed on file 02, this will be reprocessing.
test_images = mnist.test_images()
test_labels = mnist.test_labels()
test_images = (test_images / 255) - 0.5
test_images = np.expand_dims(test_images, axis=3)


# Predict on the first 5 test images.
predictions = model.predict(test_images[:5])

# Print our model's predictions.
print(np.argmax(predictions, axis=1)) # [7, 2, 1, 0, 4]

# Check our predictions against the ground truths.
print(test_labels[:5]) # [7, 2, 1, 0, 4]
