import cv2
import os

# Create the folder if it doesn't exist
known_faces_dir = "known_faces"
if not os.path.exists(known_faces_dir):
    os.makedirs(known_faces_dir)

# Ask for name
name = input("Enter the name for the image file (without extension): ").strip()
filename = os.path.join(known_faces_dir, f"{name}.jpg")

# Start video capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Press 's' to save image, 'q' to quit without saving.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow("Capture Face - Press 's' to Save, 'q' to Quit", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")
        break
    elif key == ord('q'):
        print("Quit without saving.")
        break

cap.release()
cv2.destroyAllWindows()
