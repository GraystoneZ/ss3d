import argparse
from pathlib import Path
from PIL import Image
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True, type=str, help='input image')
parser.add_argument('--output_dir', required=True, type=str, help='output directory')
args = parser.parse_args()

def get_rgba(image):
    try:
        from rembg import remove
    except ImportError:
        print('Please install rembg with "pip install rembg"')
        sys.exit()
    return remove(image, alpha_matting=False)