# Smile detection with automatic photo capture

This OpenCV based python project detects smile on a face by using OpenCV's pre-trained Haar Cascade classifiers from live webcam feed. 

Features:

- Real time face and smile detection
- captures photo automatically when smile is detected
- displays message "photo taken" for 2 seconds after automatic photo capture
- saves images with auto-incremenet file names

Main functions used:

- cv.VideoCapture(1): opens live webcam feed
- CascadeClassifier: uses OpenCV’s Haar cascades to detect faces and smiles
- cv.imwrite(): saves the current frame when a smile is detected in the same directory where the script is run
- cv.putText(): displays text on live webcam feed when a photo is taken
- cv.flip(): flips the frame to create a selfie-like view
- cv.imshow() and cv.waitKey(): used to display the video feed and handle keypresses
