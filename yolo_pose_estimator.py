from ultralytics import YOLO

model = YOLO("yolo11n-pose.pt")

results = model(show=True,
                conf=0.3,
                save=False,
                device="cuda",
                max_det=5,
                show_boxes=False,
                source="rtsp://admin:topmireag309!@10.0.58.176//ISAPI/Streaming/Channels/101")
