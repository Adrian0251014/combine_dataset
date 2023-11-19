
# from PIL import Image
# import os

# def create_sign_language_image(word):
#     word = word.lower() 
#     images_folder = "/Users/adrian/TIPS/t2s/26_letters_images" 

#     for char in word:
#         if char.isalpha():
#             image_path = os.path.join(images_folder, f"{char}.jpg")
#             if os.path.exists(image_path):
#                 img = Image.open(image_path)
#                 img.show()


# word_to_display = input("Enter a word: ")
# create_sign_language_image(word_to_display)

from PIL import Image, ImageOps
import os

def create_sign_language_image(word, output_path):
    word = word.lower()
    images_folder = "/Users/adrian/TIPS/t2s/26_letters_images" 

    images_to_combine = []
    for char in word:
        if char.isalpha():
            image_path = os.path.join(images_folder, f"{char}.jpg")
            if os.path.exists(image_path):
                img = Image.open(image_path)
                images_to_combine.append(img)

    if images_to_combine:
        # Get total width and height
        total_width = sum(img.width + 10 for img in images_to_combine) - 10 
        max_height = max(img.height for img in images_to_combine)

        # Create a new image with the calculated size
        combined_image = Image.new('RGB', (total_width, max_height), (255, 255, 255))

        # Paste images horizontally
        x_offset = 0
        for img in images_to_combine:
            combined_image.paste(img, (x_offset, 0))
            x_offset += img.width + 10 

        # Save the combined image 
        combined_image.save(output_path)
        combined_image.show()
    else:
        print("No valid images found for the given word.")

word_to_display = input("Enter a word: ")
output_file_path = "/Users/adrian/Desktop/fingerspelling.jpg"  
create_sign_language_image(word_to_display, output_file_path)

