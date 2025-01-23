import cv2
import os
import pandas as pd
from datetime import datetime
import pytz
from paddleocr import PaddleOCR

# Path to your folder of images and output Excel file
folder_path = r'C:\Users\intern.rd\OneDrive - BIZE PROJE GELISTIRME A.S\Desktop\Projects\Text2Excel for Diabetes'  
output_excel_path =  r"C:\Users\intern.rd\OneDrive - BIZE PROJE GELISTIRME A.S\Desktop\Projects\file.xlsx"

confidence_threshold = 90

# Specify the Istanbul time zone (for Turkey)
local_timezone = pytz.timezone("Europe/Istanbul")

# Initialize PaddleOCR with English language
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Prepare a list to store the results
data = []

# Process each image in the folder
for filename in os.listdir(folder_path):
    image_path = os.path.join(folder_path, filename)

    # Ensure only image files are processed
    if os.path.isfile(image_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        print(f"Processing '{filename}'...")

        # Load the image using OpenCV
        image = cv2.imread(image_path)

        # Check if the image is loaded properly
        if image is None:
            print(f"Error: Unable to load image at '{image_path}'. Skipping...")
            continue

        # Perform OCR on the loaded image
        result = ocr.ocr(image, cls=True)

        # Extract detected text with only numbers and confidence >= 85
        for line in result:
            for item in line:
                detected_text = item[1][0]
                confidence_score = item[1][1] * 100  # Convert to percentage

                # Filter by confidence and include only numeric characters
                if confidence_score >= confidence_threshold:
                    numbers = ''.join([char for char in detected_text if char.isdigit()])
                    if numbers:
                        # Get the current time in the Istanbul time zone
                        current_time = datetime.now(local_timezone)
                        
                        # Append the data with date and local time
                        data.append({
                            "Filename": filename,
                            "Detected Numbers": numbers,
                            "Date": current_time.strftime("%Y-%m-%d"),
                            "Time": current_time.strftime("%H:%M:%S")
                        })
                        print(f"Detected Numbers: {numbers}, Date: {current_time.strftime('%Y-%m-%d')}, Time: {current_time.strftime('%H:%M:%S')}")

# Convert the data list to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel(output_excel_path, index=False)
print(f"\nAll detected numbers have been saved to '{output_excel_path}'.")
