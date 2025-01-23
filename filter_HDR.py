import cv2
import numpy as np

def apply_hdr_filter(image_path, output_path):
    """
    Apply an HDR-like filter to an image.

    :param image_path: Path to the input image
    :param output_path: Path to save the processed image
    """
    # Load the image
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return
    
    # Convert the image to float32 for processing
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_float = np.float32(image) / 255.0

    # Perform tone mapping for HDR effect
    hdr_effect = cv2.detailEnhance(image, sigma_s=12, sigma_r=0.15)

    # Enhance the result for better HDR-like output
    hdr_effect = np.clip(hdr_effect * 1.5, 0, 255).astype(np.uint8)

    

    # Save the processed image
    hdr_output = cv2.cvtColor(hdr_effect, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, hdr_output)

    print(f"HDR-like image saved at {output_path}")
    

# Example usage
input_image_path = "20241205_121030.jpg"  # Path to your input image
output_image_path = "output_hdr1.jpg"  # Path to save the HDR effect image

apply_hdr_filter(input_image_path, output_image_path)
