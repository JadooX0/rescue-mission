import tensorflow as tf
import numpy as np
import cv2
import os


model = tf.keras.models.load_model('land_water_model.h5')

def predict_and_save(image_path, save_path):
    
    img = cv2.imread(image_path)
    original_size = (img.shape[1], img.shape[0])
    
    
    input_img = cv2.resize(img, (256, 256))
    input_img = input_img / 255.0
    input_img = np.expand_dims(input_img, axis=0)

    
    prediction = model.predict(input_img)[0]
    prediction = (prediction > 0.5).astype(np.uint8) * 255
    
    
    full_mask = cv2.resize(prediction, original_size)

    
    overlay = img.copy()
    overlay[full_mask == 255] = [0, 255, 0]  
    overlay[full_mask == 0] = [255, 0, 0]    

    
    final_output = cv2.addWeighted(img, 0.6, overlay, 0.4, 0)
    
    cv2.imwrite(save_path, final_output)
    print(f"Segmented image saved to {save_path}")


predict_and_save(r'C:\Users\scorp\OneDrive\rescue mission\env\dataset\datasetimage10.jpeg', 'result10.png')