import cv2

# Sample data
detection_data = {
    '<OD>': {
        'bboxes': [
            [34.23999786376953, 160.0800018310547, 597.4400024414062, 371.7599792480469],
            [456.0, 97.68000030517578, 580.1599731445312, 261.8399963378906],
            [450.8800048828125, 276.7200012207031, 554.5599975585938, 370.79998779296875],
            [95.68000030517578, 280.55999755859375, 198.72000122070312, 371.2799987792969]
        ],
        'labels': ['car', 'door', 'wheel', 'wheel']
    }
}

# Load your original image
image_path = 'car.jpg'  # Replace with the path to your image
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
else:
    # Extract bounding boxes and labels
    bboxes = detection_data['<OD>']['bboxes']
    labels = detection_data['<OD>']['labels']

    # Draw bounding boxes and labels on the image
    for bbox, label in zip(bboxes, labels):
        x_min, y_min, x_max, y_max = map(int, bbox)

        # Draw the bounding box
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color=(255, 0, 0), thickness=2)

        # Put the label above the bounding box
        cv2.putText(image, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the image
    cv2.imshow('Object Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the image to a file if needed
    cv2.imwrite('output_image_with_boxes.jpg', image)
