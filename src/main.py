import face_recognition
import cv2
from simple_facerec import SimpleFacerec
import time
import os
import uuid

# Encode faces from as folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Initialize video source and object detection network
camera = cv2.VideoCapture(0)

# Initialize the last time a picture was taken
last_saved_time = 0

while True:
    ret, frame = camera.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        top, right, bottom, left = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        # Set frame color based on whether the person is known or unknown
        if name == "Unknown":
            color = (0, 0, 255)  # Red for unknown faces
            # Check if 3 seconds have passed since the last picture was taken
            current_time = time.time()
            if current_time - last_saved_time >= 3:
                # Save the image with a unique filename
                face_image = frame[top:bottom, left:right]
                if not os.path.exists("unknown"):
                    os.makedirs("unknown")
                unknown_filename = f"unknown/{str(uuid.uuid4())}.jpg"
                cv2.imwrite(unknown_filename, face_image)
                last_saved_time = current_time
        else:
            color = (0, 255, 0)  # Green for known faces

        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_DUPLEX, 1, color, 2)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 4)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:  # Press 'Esc' to exit
        break

camera.release()
cv2.destroyAllWindows()