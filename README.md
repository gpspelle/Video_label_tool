# Label Video Tools

This code was built to label in a binary way (0, 1) videos containing people
falling or just living theirs lives. First, I tried to use some deep learning
labelling tools, but they were too complicated to such an easy task.

## Usage

!IMPORTANT!

After you run this command the video will appear on your screen. And content
will be set to 1 as default. If you press 'a' on your keyboard, content will
be labelled as 0 until you press 'l' on your keyboard.

$ python3 video_label_tool.py -path <your_video>

## Output

A file named as <your_video> but as a txt containing the number of frames and
a value for each frame. 
