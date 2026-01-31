import tensorflow as tf
import os
import glob

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


train_frames_dir = r'C:\Users\scorp\OneDrive\rescue mission\env\dataset' 

train_masks_dir = r'C:\Users\scorp\OneDrive\rescue mission\env\output directory'


train_frames_list = sorted(glob.glob(os.path.join(train_frames_dir, "*.jpeg")))
train_masks_list = sorted(glob.glob(os.path.join(train_masks_dir, "*.png")))


if len(train_frames_list) == 0:
    raise ValueError(f"No images found in {train_frames_dir}. Check your path!")


if len(train_frames_list) != len(train_masks_list):
    print(f"Warning: Images ({len(train_frames_list)}) and Masks ({len(train_masks_list)}) count mismatch!")
    print("Make sure you ran masking.py successfully first.")


def load_and_preprocess(image_path, mask_path):
  
    img = tf.io.read_file(image_path)
    img = tf.image.decode_jpeg(img, channels=3)
    img = tf.image.resize(img, [256, 256])
    img = tf.cast(img, tf.float32) / 255.0  
    
    mask = tf.io.read_file(mask_path)
    mask = tf.image.decode_png(mask, channels=1) 
    mask = tf.image.resize(mask, [256, 256])
    mask = tf.cast(mask, tf.float32) / 255.0 
    
    return img, mask


train_dataset = tf.data.Dataset.from_tensor_slices((train_frames_list, train_masks_list))
train_dataset = train_dataset.map(load_and_preprocess)
train_dataset = train_dataset.batch(2) 

print("Successfully created dataset with", len(train_frames_list), "samples.")

def unet_model(output_channels):
    inputs = tf.keras.layers.Input(shape=[256, 256, 3])

    
    d1 = tf.keras.layers.Conv2D(64, 3, activation='relu', padding='same')(inputs)
    d1 = tf.keras.layers.MaxPooling2D()(d1)
    
    d2 = tf.keras.layers.Conv2D(128, 3, activation='relu', padding='same')(d1)
    d2 = tf.keras.layers.MaxPooling2D()(d2)

   
    b = tf.keras.layers.Conv2D(256, 3, activation='relu', padding='same')(d2)

    
    u1 = tf.keras.layers.UpSampling2D()(b)
    u1 = tf.keras.layers.Conv2D(128, 3, activation='relu', padding='same')(u1)
    
    u2 = tf.keras.layers.UpSampling2D()(u1)
    u2 = tf.keras.layers.Conv2D(64, 3, activation='relu', padding='same')(u2)

    
    outputs = tf.keras.layers.Conv2D(output_channels, 1, activation='sigmoid')(u2)

    return tf.keras.Model(inputs=inputs, outputs=outputs)


model = unet_model(output_channels=1) 
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print("Starting training...")

model.fit(train_dataset, epochs=20) 

model.save('land_water_model.h5')
print("Model trained and saved as land_water_model.h5")