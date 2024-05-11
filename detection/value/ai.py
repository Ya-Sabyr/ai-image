import tensorflow as tf
from keras.api.models import load_model
from keras.api.applications.resnet50 import preprocess_input
import numpy as np

from PIL import Image

model = load_model(r'C:\Users\sabyr\OneDrive\Desktop\Pneumonia_Detection-master\project\models\model_92.keras')

image = Image.open(r'C:\Users\sabyr\OneDrive\Desktop\Pneumonia_Detection-master\lungs1.jpg')

image = image.resize((587, 306))

# Convert the image to an array
img_array = np.array(image)

# Preprocess the input by scaling pixel values to the range [-1, 1]
processed_img = preprocess_input(img_array)

predictions = model.predict(np.expand_dims(processed_img, axis=0))

print(predictions)