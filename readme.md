
# Before running the script, ensure you have the following installed:
- Python (version 3.6 or higher)
- OpenCV (cv2) library
- EasyOCR library
Usage- Save the script to a Python file (e.g., text_extraction.py).
- Run the script from the command line with the path to the input image as an argument:

python text_extraction.py <input_image_path>

# Script Breakdown
1. Initialization- The script initializes an EasyOCR reader with English language support.
- The gpu=True argument enables GPU acceleration if available.
2. Function 
- headwritingTotext(img)- This function extracts text from an input image.
- Arguments:
    - img: Path to the input image file.
- Steps:
    - Read the input image using OpenCV (cv2).
    - Enhance the image by sharpening its edges.
    - Create a binary version of the image using thresholding.
    - Utilize EasyOCR to read text from the preprocessed image.
    - Return a list of detected text strings.
3. Main Execution- The script checks if the correct number of command-line arguments (i.e., the input image path) is provided.
- If not, it prints a usage message and exits.
- Otherwise, it calls the headwritingTotext function with the input image path.
- Finally, it prints the extracted text.
Example UsageSuppose you have an image named sample_image.jpg. Run the script as follows:

python script.py sample_image.jpg

Notes- Replace <input_image_path> with the actual path to your image.
