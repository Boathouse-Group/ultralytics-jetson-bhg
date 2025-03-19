import cv2
from ultralytics import YOLO

# Load a YOLO11n PyTorch model
# model = YOLO("yolo11n.pt")
# Export the model to TensorRT
#model.export(format="engine")  # creates 'yolo11n.engine'

# Load the exported TensorRT model
trt_model = YOLO("yolo11n.engine", task="detect")

# Run inference with streaming mode
results = trt_model(source=0, stream=True)

# Process results generator
for result in results:
    # Get the annotated frame
    frame = result.plot()  # Annotate the frame with bounding boxes, labels, etc.

    # Display the frame using OpenCV
    cv2.imshow("Live Detection", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cv2.destroyAllWindows()
