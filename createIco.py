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
import os


def png_to_ico(png_path, ico_path=None, sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]):
    """
    Convert a PNG image to an ICO file with multiple sizes.

    :param png_path: Path to the input PNG file.
    :param ico_path: Path to the output ICO file. If None, it will be saved in the same directory as the PNG file with the same name.
    :param sizes: List of sizes for the ICO file.
    """
    # Open the PNG file
    img = Image.open(png_path)

    # Ensure the image has an alpha channel
    img = img.convert("RGBA")

    # Save the image as an ICO file
    if ico_path is None:
        ico_path = os.path.splitext(png_path)[0] + '.ico'

    img.save(ico_path, format='ICO', sizes=sizes)


# Example usage:
png_path = 'example.png'  # Replace with your PNG file path
ico_path = 'example.ico'  # Replace with your desired ICO file path
png_to_ico(png_path, ico_path)
