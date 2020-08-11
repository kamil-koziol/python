#!/usr/bin/env python
# coding: utf-8

# In[30]:


import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2


# In[33]:


IMG_PATH = "./rps/"
CATEGORIES = ["rock", "paper", "scissors"]
training_data = []


# In[34]:


for category in CATEGORIES:
    path = os.path.join(IMG_PATH, category)
    class_num = CATEGORIES.index(category)
    for img in os.listdir(path):
        try:
            img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array, (300,300))
            training_data.append([new_array, class_num])
        except Exception as e:
            pass


# In[35]:


import random
random.shuffle(training_data)


# In[36]:


x_train = []
y_train = []
for feature, label in training_data:
    x_train.append(feature)
    y_train.append(label)


# In[46]:


x_train = np.array(x_train).reshape(-1,300,300,1)


# In[50]:


model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3,3), input_shape=(300,300,1), activation=tf.nn.relu),
    tf.keras.layers.MaxPooling2D(2,2),
    
    tf.keras.layers.Conv2D(64, (3,3), activation=tf.nn.relu),
    tf.keras.layers.MaxPooling2D(2,2),
    
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Flatten(),
    
    tf.keras.layers.Dense(256, activation=tf.nn.relu),
    tf.keras.layers.Dense(3, activation=tf.nn.softmax)
])


# In[51]:


model.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss=tf.keras.losses.sparse_categorical_crossentropy,
    metrics = ['accuracy'])


# In[52]:


model.fit(x_train,y_train, epochs=1)


# In[ ]:




