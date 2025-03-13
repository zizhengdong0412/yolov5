import cv2

cap = cv2.VideoCapture(0)  # Try 0, 1, or 2 for different cameras
if not cap.isOpened():
    print("❌ Camera access failed!")
else:
    print("✅ Camera initialized successfully!")