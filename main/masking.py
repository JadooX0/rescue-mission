import cv2
import numpy as np
import os
import glob

def create_masks():
    # 1. Define your folder paths
    # Using raw strings (r'') prevents the 'unicodeescape' error you encountered
    input_dir = r'C:\Users\scorp\OneDrive\rescue mission\env\dataset' 
    output_dir = r'C:\Users\scorp\OneDrive\rescue mission\env\output directory'

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created folder: {output_dir}")

    # 2. Get a list of all JPEG images in your input folder
    image_paths = glob.glob(os.path.join(input_dir, "*.jpeg"))
    
    if not image_paths:
        print(f"Error: No .jpeg images found in {input_dir}. Check your path!")
        return

    print(f"Found {len(image_paths)} images. Starting masking process...")

    for img_path in image_paths:
        # Load the image
        img = cv2.imread(img_path)
        if img is None:
            continue

        # 3. Convert to HSV color space
        # This makes it easier to isolate the green/brown land from the blue ocean 
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # 4. Define the color range for LAND (Green and Brown)
        # These values target the 'brown/green region' mentioned in the task 
        lower_land = np.array([35, 40, 40])
        upper_land = np.array([90, 255, 255])

        # 5. Create the binary mask
        # Pixels in the land range become WHITE (255), everything else becomes BLACK (0)
        mask = cv2.inRange(hsv, lower_land, upper_land)

        # 6. Save the mask with the same filename but as .png
        # Using .png is better for masks as it is lossless (no compression blur)
        base_name = os.path.basename(img_path)
        file_name = os.path.splitext(base_name)[0] + ".png"
        save_path = os.path.join(output_dir, file_name)

        cv2.imwrite(save_path, mask)
        print(f"Processed: {base_name} -> Saved as: {file_name}")

    print("\nAll masks created successfully! You can now run imagesegmentation.py.")

if __name__ == "__main__":
    create_masks()