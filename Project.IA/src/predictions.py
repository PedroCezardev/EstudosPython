from ultralytics import YOLO
import cv2


def predict_image(img_array):
    return model(img_array)

def plot_predictions(img_array, predictions):
    # Map the class IDs to the custom class names and draw the boxes on the image
    for result in predictions:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy.tolist()[0])  # Convert to list and map to integers
            confidence = box.conf.item()

            if confidence > THRESHHOLD_DETECTION:
                # Draw bounding box and label on the image
                cv2.rectangle(img_array, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img_array, f"{CLASS_NAME} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return img_array


THRESHHOLD_DETECTION = 0.5
CLASS_NAME = "Carro"
model = YOLO("../assets/models/yolov8s.pt")
camera = cv2.VideoCapture(0)
is_running = True


while is_running:

    status, frame = camera.read()

    predictions = predict_image(frame)

    frame_ploted = plot_predictions(frame, predictions)

    if not status or cv2.waitKey(1) & 0xff == ord('q'):
        is_running = False

    cv2.imshow("Camera", frame_ploted)