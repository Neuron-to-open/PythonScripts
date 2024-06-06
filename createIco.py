# /****************************************************************************
# * Author: Neuron-to-open
# * Date: 2024/6/5
# * Python : 3.11
# * 系统版本： Windows 11 家庭版 20H2
# * IDE: Pycharm
# * 编程语言: Python
# * =========== ====== ===== ==============================================
# * @Copyright (C) Yijiayi All Rights reserved
# *****************************************************************************/
from PIL import Image


# Define a function to convert JPG format images to ICO format
def convert_jpg_to_ico(input_path, output_path):
    """
    Convert a JPG image to ICO format.

    Parameters:
    input_path (str): The path of the input JPG image file.
    output_path (str): The path to save the converted ICO image file.

    Returns:
    None
    """
    try:
        # Use the Image library to open the JPG image file
        # Open the JPG image
        with Image.open(input_path) as img:
            # Save the image as ICO format
            # Save as ICO
            img.save(output_path, format='ICO')
        # Print the conversion success message
        print(f"Successfully converted {input_path} to {output_path}")
    except Exception as e:
        # Print the error message if an exception occurs during conversion
        print(f"An error occurred: {e}")


# Example usage
# Define the path of the input JPG image and the path to save the output ICO image
input_jpg = "E:\\pictures\\动漫游戏与影视\\原神\\kkld.jpg"
output_ico = 'output_icon.ico'

# Call the function to perform the conversion
convert_jpg_to_ico(input_jpg, output_ico)
