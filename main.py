import cv2

# Load the Haar Cascade classifier for face detection
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize video capture from default webcam (index 0)
videoCapture = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not videoCapture.isOpened():
    print("Error: Could not open video device.")
else:
    while True:
        # Read a frame from the video capture
        ret, frame = videoCapture.read()

        if not ret:
            print("Error: Failed to capture image")
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the frame with rectangles drawn around faces
        cv2.imshow('Video', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all OpenCV windows
    videoCapture.release()
    cv2.destroyAllWindows()
