import cv2
import numpy as np
import easyocr
import sys

# Initialize the EasyOCR reader with English language support
reader = easyocr.Reader(['en'], gpu=True)  # Load once only in memory.

def headwritingTotext(img):
    """
    Extracts text from an image using EasyOCR.

    Args:
        img (str): Path to the input image file.

    Returns:
        list: A list of detected text strings.
    """
    # Read the input image
    image = cv2.imread(img)

    # Sharpen the edges of the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpen = cv2.filter2D(gray, -1, sharpen_kernel)

    # Threshold the image to create a binary version
    thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Use EasyOCR to read text from the preprocessed image
    r_easy_ocr = reader.readtext(thresh, detail=0)

    return r_easy_ocr

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_image_path>")
        sys.exit(1)

    input_image_path = sys.argv[1]
    extracted_text = headwritingTotext(input_image_path)

    print("Extracted text:")
    for text in extracted_text:
        print(text)
