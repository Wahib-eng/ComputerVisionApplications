import cv2
import numpy as np

def detect_cracks_with_high_contrast(image_path):
    """
    Detect cracks on black metal surfaces with high-contrast enhancement.
    Display the results in resized windows.
    :param image_path: Path to the input image
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply CLAHE for localized high-contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    high_contrast = clahe.apply(gray)
    
    # Apply Canny edge detection
    edges = cv2.Canny(high_contrast, threshold1=50, threshold2=150)
    
    # Resize images to a smaller size for display
    display_size = (1000, 1000)  # Width x Height
    original_resized = cv2.resize(image, display_size)
    contrast_resized = cv2.resize(high_contrast, display_size)
    edges_resized = cv2.resize(edges, display_size)
    
    # Display results
    cv2.imshow("Original (Resized)", original_resized)
    cv2.imshow("High Contrast (Resized)", contrast_resized)
    cv2.imshow("Edges (Resized)", edges_resized)
    
    # Wait for a key press to close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
detect_cracks_with_high_contrast("20241205_121030.jpg")
