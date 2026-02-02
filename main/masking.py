import cv2
import numpy as np
import os
import glob

def create_masks():
   
    input_dir = r'C:\Users\scorp\OneDrive\rescue mission\env\dataset' 
    output_dir = r'C:\Users\scorp\OneDrive\rescue mission\env\output directory'

    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created folder: {output_dir}")

   
    image_paths = glob.glob(os.path.join(input_dir, "*.jpeg"))
    
    if not image_paths:
        print(f"Error: No .jpeg images found in {input_dir}. Check your path!")
        return

    print(f"Found {len(image_paths)} images. Starting masking process...")

    for img_path in image_paths:
      
        img = cv2.imread(img_path)
        if img is None:
            continue

       
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower_land = np.array([35, 40, 40])
        upper_land = np.array([90, 255, 255])


        mask = cv2.inRange(hsv, lower_land, upper_land)

       
        base_name = os.path.basename(img_path)
        file_name = os.path.splitext(base_name)[0] + ".png"
        save_path = os.path.join(output_dir, file_name)

        cv2.imwrite(save_path, mask)
        print(f"Processed: {base_name} -> Saved as: {file_name}")

    print("\nAll masks created successfully!")

if __name__ == "__main__":

    create_masks()
