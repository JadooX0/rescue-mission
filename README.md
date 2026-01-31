Autonomous Search and Rescue: Terrain Segmentation & Casualty Allocation
🚁 About the Project
This project was developed for the UAS-DTU Technical Round. It solves the challenge of autonomous disaster response by combining Computer Vision and Decision Logic.

The pipeline takes aerial images of disaster zones and performs two critical tasks:

Terrain Segmentation: Uses a Deep Learning U-Net model to distinguish between land (safe zones) and water (hazard zones).

Casualty Allocation: A priority-based algorithm that assigns detected casualties (Children, Elderly, Adults) to specific rescue pads based on their medical urgency and location using the Log Q scoring formula.

Key Features
Deep Learning Segmentation: Built with TensorFlow/Keras to provide pixel-perfect land/water masks.

Priority-Based Rescue: Prioritizes casualties based on Shape (Age) and Color (Emergency Level).

Rescue Ratio (P 
r
​
 ): Automatically calculates the mission efficiency score.

🛠️ How to Use
1. Prerequisites
Ensure you have Python 3.10+ installed. It is recommended to use the provided virtual environment (env).

2. Installation
Clone the repository and install the required libraries:

Bash
git clone https://github.com/JadooX0/rescue-mission.git
cd rescue-mission
pip install -r requirements.txt
3. Running Segmentation
To generate a land/water mask from an aerial image:

Bash
python main/predict.py
The output will be saved as result1.png in the root directory.

4. Running Allocation
To calculate the rescue assignments and the final Rescue Ratio (P 
r
​
 ):

Bash
python main/allocation.py
This will print the allocation list for the Blue, Pink, and Grey pads to the console.

 Methodology
U-Net Model: Trained on a custom dataset of aerial wreckage images to achieve high accuracy in varying light conditions.

Log Q Scoring:

Score=(Age×Emergency)−log 
10
​
 (Distance+1)
This ensures that high-priority individuals are rescued even if they are slightly further away, while maintaining fuel efficiency.

 Project Structure
main/: Core Python scripts for prediction and allocation.

land_water_model.h5: The pre-trained neural network weights.

dataset/: Training and validation data.

result1.png: Example output of the segmentation model.

Final Steps to Submit:
Open VS Code, paste the text above into your README.md.

Save it.

Push it to GitHub:

PowerShell
git add README.md
git commit -m "Added professional README"
git push origin main
Would you like me to help you generate the requirements.txt file now to make sure the "How to Use" section actually works for the judges?
