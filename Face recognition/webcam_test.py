import cv2

print("📷 Starting webcam test...")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Webcam not working or not accessible.")
    exit()

print("✅ Webcam opened!")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Failed to grab frame.")
        break
    cv2.imshow("Webcam Test", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("🛑 Exiting webcam loop.")
        break

cap.release()
cv2.destroyAllWindows()
print("🧼 Cleaned up.")
