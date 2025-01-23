import os

def rename_images_in_folder(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    print(f"Files found: {files}")  # Debugging line to display files
    
    # Filter out only image files (based on common image extensions)
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    images = [file for file in files if file.lower().endswith(image_extensions)]
    
    # Sort the images to ensure a consistent order
    images.sort()

    # Loop through images and rename them
    for index, image in enumerate(images, start=1):
        # Generate new name
        new_name = f"KN_{index}{os.path.splitext(image)[1]}"
        
        # Define the full paths
        old_path = os.path.join(folder_path, image)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the image
        os.rename(old_path, new_path)
        print(f"Renamed: {image} -> {new_name}")

# Example usage
folder_path = r"C:\Users\intern.rd\OneDrive - BIZE PROJE GELISTIRME A.S\Desktop\Projects\Datasets\MenteseDefects58"
rename_images_in_folder(folder_path)
