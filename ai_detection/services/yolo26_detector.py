from ultralytics import YOLO
import cv2
import os


MODEL = YOLO("runs/detect/train/weights/best.pt")

def run_detection(image_path):

    results = MODEL(image_path)

    result = results[0]

    detections = []

    annotated_frame = result.plot()

    filename = os.path.basename(image_path)

    output_path = os.path.join(
        "media/results",
        filename
    )

    cv2.imwrite(output_path, annotated_frame)

    for box in result.boxes:

        cls_id = int(box.cls[0])

        class_name = MODEL.names[cls_id]

        confidence = float(box.conf[0])

        x1, y1, x2, y2 = map(
            int,
            box.xyxy[0]
        )

        detections.append({
            "class_name": class_name,
            "confidence": round(confidence, 2),
            "bounding_box": [x1, y1, x2, y2]
        })

    return {
        "detections": detections,
        "result_image": output_path
    }