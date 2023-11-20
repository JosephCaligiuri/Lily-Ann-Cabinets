import cv2
import pytesseract

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Set up Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path to your Tesseract installation

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale for better OCR results
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the grayscale frame
    text = pytesseract.image_to_string(gray)

    # Display the frame with detected text and numbers
    cv2.imshow('Text and Numbers Detection', gray)

    # Print the detected text and numbers to the console
    print(text)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
