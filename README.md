# Driver Drowsiness Detection System with OpenCV & Machine Learning 
This driver drowsiness detection project is created to prevent accidents. Drowsiness means sleepiness, so it prevents accidents that are caused by drivers who are feeling drowsy or we can say who fell asleep while driving. So we are creating a Drowsiness detection system that will detect that the person’s eyes are closed or open. And if a person’s eyes are closed for a few seconds, the system will alert the person by ringing an alert sound.
# Our approach to Create Drowsiness detection system:
In this project, for collecting images from webcam we will be using OpenCV and feed these images to our Deep learning model which will classify that the person’s eyes is ‘Open’ or ‘Closed’. So we will follow these steps:
*	We will take image input from the camera
*	Detect face and eyes in the image.
*	Create a Region of Interest(ROI), for both detected face and eyes.
*	Feed this to our classifier(model), which will categorize whether eyes are open or closed.
*	At last, we will calculate the time to check if the person is drowsy or not.
