##Facial Recognition System 🧠📸

A real-time facial recognition system built using Python and OpenCV. It uses the Haar Cascade Classifier to detect faces from live webcam feeds and highlights them with bounding boxes.

🚀 Features
	•	Real-time face detection from webcam feed
	•	Uses Haar Cascade Classifier for robust face detection
	•	Highlights detected faces with green rectangles
	•	Option to exit the live feed by pressing q
	•	Achieved ~95% accuracy in detection with optimized parameters

🛠️ Technologies Used
	•	Python
	•	OpenCV
	•	Haar Cascade Classifier (frontal face detection)

📸 How It Works
	1.	The webcam captures real-time video.
	2.	Each frame is converted to grayscale for better processing.
	3.	The Haar Cascade classifier detects faces in the frame.
	4.	Detected faces are highlighted with bounding boxes.

🧾 Prerequisites
	•	Python 3.x
	•	OpenCV (pip install opencv-python)

🧪 Installation & Usage

# Clone the repository
git clone https://github.com/yourusername/facial-recognition-system.git
cd facial-recognition-system

# Install dependencies
pip install opencv-python

# Run the program
python face_detection.py

💻 Output
	•	Opens a webcam window showing the live video feed.
	•	Draws green rectangles around detected faces.
	•	Press q to exit the video feed.

📂 File Structure

facial-recognition-system/
│
├── face_detection.py      # Main script
└── README.md              # Project documentation

📌 Notes
	•	The system uses OpenCV’s default Haar cascade model for face detection.
	•	For better accuracy, make sure you are in a well-lit environment.

📃 License

This project is open-source and available under the MIT License.

⸻

Let me know if you want to include enhancements like saving face data, adding recognition features, or converting it to a Flask web app.
