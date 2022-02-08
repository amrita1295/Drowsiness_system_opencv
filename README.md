# Driver Drowsiness Detection System with OpenCV & Machine Learning 
This driver drowsiness detection project is created to prevent accidents. Drowsiness means sleepiness, so it prevents accidents that are caused by drivers who are feeling drowsy or we can say who fell asleep while driving. So we are creating a Drowsiness detection system that will detect that the person’s eyes are closed or open. And if a person’s eyes are closed for a few seconds, the system will alert the person by ringing an alert sound.
# Our approach to Create Drowsiness detection system:
In this project, for collecting images from webcam we will be using OpenCV and feed these images to our Deep learning model which will classify that the person’s eyes is ‘Open’ or ‘Closed’. So we will follow these steps:
*	We will take image input from the camera
*	Detect face and eyes in the image.
*	Create a Region of Interest(ROI), for both detected face and eyes.
*	Feed this to our classifier(model), which will categorize whether eyes are open or closed.
*	At last, we will calculate the time to check if the person is drowsy or not.
# Driver Drowsiness Detection Project Code :
**haarcascade files:** This folder has files that are used to detect the face and eyes of a person, these files are xml files. The haar cascade files have many xml files that are required to detect objects in an image. You can download this also just by searching on Google.
**Beep-07.wav:** This file is used to play the alert sound when a person closes its eyes for a few seconds.
**drowsiness_system.py:** This file consists of full implementation of our project in which we have loaded the model and used it to alert the person whenever he/she will feel drowsy. So this is the main file, you have to run this file for detection procedure.
## Let’s go step by step:
1. Importing all the needed libraries:
2. Setting an alarm sound file, and we will set a path of haar cascade files to detect face, detect left eye, and detect right eye.
3. After this we will load our model, and using OpenCV we will access a webcam that will capture each frame.
4. This is the main logic of code. In this code we are checking that, if the person’s left eye and right eye are closed, time will increase and if time increases more than 10 the alert sound will start, and if both eyes are open the time decreases and sound stops after some time.
