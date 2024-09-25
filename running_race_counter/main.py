from ultralytics import YOLO
from ultralytics.solutions import object_counter
import cv2

model = YOLO("model/yolov9e.pt")
cap = cv2.VideoCapture("video/race.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (
    int(cap.get(x))
    for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS)
)

region_points = [(270, 500), (700, 500), (630, 450), (320, 450)]
classes_to_count = [0]  # person

window_size = (800, 600)
# Video writer
video_writer = cv2.VideoWriter(
    "output/race_people_counting.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h)
)

# Init Object Counter
counter = object_counter.ObjectCounter(
    view_img=True, reg_pts=region_points, classes_names=model.names, line_thickness=2
)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print(
            "Video frame is empty or video processing has been successfully completed."
        )
        break
    tracks = model.track(im0, persist=True, show=False, classes=classes_to_count)

    im0 = counter.start_counting(im0, tracks)
    video_writer.write(im0)
    # Check for key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):  # Press 'q' to exit
        break

cap.release()
video_writer.release()
cv2.destroyAllWindows()
