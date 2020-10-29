import argparse
import pytesseract
from PIL import Image

def parse_arguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", type=str, required=False, default="usr/image.jpg", help="Image from which text must be read")
    ap.add_argument("-l", "--lang", type=str, required=False, help="Language that Tesseract should use to identify words")
    ap.add_argument("-d", "--tessdata-dir", required=False, help="Path to the dataset Tesseract should use to train its neural network")
    
    return vars(ap.parse_args())

def args_to_tess_config(args):
    config = ""
    if args["lang"]:
        config += f'-l {args["lang"]}'
    if args["tessdata_dir"]:
        config += f' --tessdata-dir "{args["tessdata_dir"]}"'

    return config

def ocr(image_filename, tesseract_config):
    image = Image.open(image_filename)
    
    text = pytesseract.image_to_string(image, config=tesseract_config) 
    return text


args = parse_arguments()
config = args_to_tess_config(args)

print(ocr(args["image"], config))