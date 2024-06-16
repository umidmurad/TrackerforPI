# Author : Umid M.
# Date : 06/16/2024

import cv2 as cv

# Initialize video capture from the default camera
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Read two initial frames
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while True:
    # Calculate absolute difference between the first and second frame
    diff = cv.absdiff(frame1, frame2)
    
    # Convert the difference to grayscale
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    
    # Gaussian blur the grayscale image
    # https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    
    # Apply thresholding to get binary image
    # https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
    _, thresh = cv.threshold(blur, 30, 255, cv.THRESH_BINARY)
    
    # Dilate the thresholded image to fill in holes
    dilated = cv.dilate(thresh, None, iterations=3)
    
    # Find contours in the binary image
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    # Draw bounding boxes around detected contours
    for contour in contours:
        # Increasing the thresholding value will reduce the number of contours detected
        # basically, it will reduce the noise in the image, and show less movements
        if cv.contourArea(contour) < 15000:
            continue
        x, y, w, h = cv.boundingRect(contour)
        cv.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the resulting frame
    cv.imshow('frame', frame1)
    
    # Read the next frame, if no frame is read, break the loop
    frame1 = frame2
    ret, frame2 = cap.read()
    if not ret:
        break
    
    if cv.waitKey(1) == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv.destroyAllWindows()
