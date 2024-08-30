<div align='center'><img style="width:30%" src='https://github.com/user-attachments/assets/52b08b6e-64cf-437b-86a2-55dc410e918f'/></div>
<div align='center'> <h1> 🎥  Motion Detection using OpenCV </h1> </div>
<p>This project uses OpenCV to detect motion levels in real-time through a webcam. The program categorizes the motion into three levels and displays the current level on the video feed.</p>

<br>
<h3> Build with Libraries </h3>
<p>
»<b>OpenCV</b> to capture the video</p> 

<br>

##  🔍  How It Works

- **Video Capture**: Captures video from the webcam.
- **Background Subtraction**: Uses `cv2.createBackgroundSubtractorMOG2` to detect moving objects.
- **Motion Detection**: Calculates the sum of detected pixels to determine the level of motion:
  - **Stable**: No significant motion detected.
  - **1st level motion detected!**: Low level of motion.
  - **2nd level motion detected!**: Medium level of motion.
  - **3rd level motion detected!**: High level of motion.
