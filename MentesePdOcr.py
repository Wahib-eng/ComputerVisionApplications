import cv2
import numpy as np
from paddleocr import PaddleOCR

# Initialize PaddleOCR with English language
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Start webcam capture (0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Unable to access the camera.")
    exit()

# Define the coordinates for the square (you can adjust these as needed)
x, y, w, h = 200, 150, 300, 300  # x, y: top-left corner, w, h: width and height of the square

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture image.")
        break
    
    # Draw a rectangle (square) on the frame
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Extract the region of interest (ROI) from the square
    roi = frame[y:y+h, x:x+w]
    
    # Perform OCR on the region of interest
    result = ocr.ocr(roi, cls=True)

    # Initialize message and color with default values
    message = "No Text Detected"
    color = (0, 0, 255)  # Red color for failure

    # Initialize an empty list to store all detected text lines
    detected_texts = []

    # Check if result is not None and contains data
    if result is not None and len(result) > 0:
        # Extract all detected text lines
        for line in result:
            if line:  # Ensure the line is not None or empty
                for item in line:
                    detected_texts.append(item[1][0])  # Append all detected text to the list

        # Print all detected text
        print("Detected Texts:")
        for text in detected_texts:
            print(text)

        # Combine all detected text into a single string
        combined_text = ''.join(detected_texts)

        # Filter only alphanumeric characters (letters and numbers)
        alphanumeric_chars = [char for char in combined_text if char.isalnum()]  # Includes letters and numbers
        print(f"Alphanumeric Text: {''.join(alphanumeric_chars)}")

        if len(alphanumeric_chars) == 5:
            message = "Mentese dorgulandi"
            color = (0, 255, 0)  # Green color for success
        elif len(alphanumeric_chars) == 0: 
            message = "Menteseyi ilgili alana gosterniz !"
        else:
            message = "Mentese dorgulanmadi"
            color = (0, 0, 255)  # Red color for failure

    # Display the message above the square
    cv2.putText(frame, message, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2, cv2.LINE_AA)

    # Display the frame using OpenCV (efficient for real-time video)
    cv2.imshow("Webcam Feed", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
