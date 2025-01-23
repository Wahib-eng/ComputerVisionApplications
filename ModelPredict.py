# Import necessary libraries
from ultralytics import YOLO
import cv2

# Load the trained model
model = YOLO(r'hinge.pt')

# Start video capture from the default camera (0 for default webcam)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Unable to access the camera.")
else:
    print("Camera is working. Press 'q' to quit.")

# Loop to capture each frame and make predictions
while cap.isOpened():
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read from camera.")
        break

    # Run prediction on the frame
    results = model.predict(source=frame, save=False, show=False, conf=0.40)  # Set confidence threshold if desired

    # Visualize predictions on the frame
    for box in results[0].boxes:
        # Extract box coordinates and class label
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Box coordinates
        label = model.names[int(box.cls)]  # Class name
        confidence = box.conf[0]  # Confidence score
        
        # Draw the bounding box and label on the frame
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f'{label} {confidence:.2f}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame with predictions
    cv2.imshow("YOLO Real-Time Prediction", frame)

    # Exit loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
