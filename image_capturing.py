import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# Load pre-trained VGG16 model (without last layer)
vgg_model = VGG16(weights='imagenet')
vgg_model = Model(inputs=vgg_model.inputs, outputs=vgg_model.layers[-2].output)

# Function to extract image features
def extract_features(image_path):
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    features = vgg_model.predict(image, verbose=0)
    return features

 features = extract_features("sample.jpg")
print("Image features extracted successfully")
# Sample captions (for demo)
captions = [
    "a dog is playing in the park",
    "a cat is sitting on the sofa",
    "a man is riding a bicycle"
]

# Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(captions)
vocab_size = len(tokenizer.word_index) + 1
max_length = 10

# Dummy caption generator (demo purpose)
def generate_caption():
    return "A dog is playing in the park"

# Test with an image
image_path = "sample.jpg"   # put an image in same folder
features = extract_features(image_path)

print("Generated Caption:")
print(generate_caption())