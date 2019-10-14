#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:42:40 2019

@author: dayanarios
(1 = dog, 0 = cat).
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
"""

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

TRAIN_DATA_DIR = "../data/train"
TEST_DATA_DIR = "../data/test1"
IMG_WIDTH = 150
IMG_HEIGHT = 150


def label_img(label):  
    if label == 'cat':
        return 0
    elif label == 'dog':
        return 1
    else:
        return -1

def prepare_training_data():
    training_data = []
    for img in os.listdir(TRAIN_DATA_DIR):
        if img.endswith(".jpg"):
            path = os.path.join(TRAIN_DATA_DIR, img)
            label, _id, _ = img.split(".", 2)
            label_code = label_img(label)
            img = cv2.imread(path,cv2.IMREAD_COLOR)
            img = cv2.resize(img, (IMG_WIDTH,IMG_HEIGHT))
            training_data.append((label_code, img, _id))
    
    training_data = np.array(training_data)
    #np.save('training_data', training_data)
    return training_data

def prepare_testing_data():
    testing_data = []
    for img in os.listdir(TEST_DATA_DIR):
        if img.endswith(".jpg"):
            path = os.path.join(TEST_DATA_DIR, img)
            print(path)
            _id, _ = img.split(".", 1)
            print(_id)
            img = cv2.imread(path,cv2.IMREAD_COLOR)
            img = cv2.resize(img, (IMG_WIDTH,IMG_HEIGHT))
            testing_data.append((img, _id))
    
    #cv2.imshow("test", img)
    #cv2.waitKey(25)
    #cv2.destroyAllWindows()
    testing_data = np.array(testing_data)
    return testing_data

def display_image(data, n):
    #data = np.load('training_data.npy', allow_pickle=True)
    image = data[n][1]
    plt.axis("off")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()
            
    
from keras.models import Sequential



if __name__ == '__main__':
    #training_data = prepare_training_data()#shape 20,000 x 3
    #print(training_data.shape)
    #testing_data = prepare_testing_data()
    #display_image()
    prepare_testing_data()