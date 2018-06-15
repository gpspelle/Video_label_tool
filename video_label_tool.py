import numpy as np
import cv2
import os
import argparse
import sys

def video_label_tool(path): 
    cap = cv2.VideoCapture(path)

    current_state = 1
    annotation_list = []

    while(True):
        # Read one frame.
        ret, frame = cap.read()

        if not ret:
            break
        # Show one frame.
        cv2.imshow('frame', frame)

        # Check, if the space bar is pressed to switch the mode.
        key = cv2.waitKey(25)

        if key & 0xFF == ord('a'):
            current_state = 0
        elif key & 0xFF == ord('l') and current_state == 0:
            current_state = 1

        annotation_list.append(current_state)

    cap.release()
    cv2.destroyAllWindows()

    return annotation_list

argp = argparse.ArgumentParser(description='Label a video')
argp.add_argument("-path", dest='path', type=str, nargs=1, required=True,
                 help='Usage: -path <path_to_video>')
argp.add_argument("-multiple", dest='multiple', type=int, nargs=1, 
                 required=True, help='Usage: -set <True or False>')

try:
    args = argp.parse_args()
except:
    argp.print_help(sys.stderr)
    exit(1)


if args.multiple[0] == 1:
    annotation_list = video_label_tool(args.path[0])
    print(annotation_list)

    out = args.path[0][:-4]
    f = open(out + '.txt', 'w')
    sys.stdout = f
    print(len(annotation_list))
    for i in annotation_list:
        print(i)
else:

    cap = cv2.VideoCapture(args.path[0])
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    annotation_list = []
    for i in range(length):
       annotation_list.append(1) 

    print(annotation_list)

    out = args.path[0][:-4]
    f = open(out + '.txt', 'w')
    sys.stdout = f
    print(len(annotation_list))
    for i in annotation_list:
        print(i)
