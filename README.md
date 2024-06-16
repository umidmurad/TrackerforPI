# TrackerforPI

## The goal of the project is to create a Live Image/Video tracker using OpenCV to use a Raspberry PI camera, or a laptop camera to see and track moving objects. 

### More information about OpenCV can be found here: https://docs.opencv.org/4.x/
The camera will be constantly watching the surroundings. It will use OpenCV libraries to track any items that show up in its visual. 

#### Current Progress
- Detect movement
- Put a border around the moving object, and display it. 

#### Future Goals for the project: 
- Add support for detecting the tracked item (Human, or Cat), possibly use LLM libraries for this. 
- If a moving object comes into the view, log its time and date.
- Send a text or email at the end of the day, with logs, images etc.


## How to Run the Application
1. Download the file, and move to that directory in the terminal.
2. Run `python3 Tracker.py` 


