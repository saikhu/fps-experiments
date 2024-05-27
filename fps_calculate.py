import cv2
import time
import sys
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

def capture_video(frame_width, frame_height, backend, backend_name, camera_index):
    try:
        cap = cv2.VideoCapture(camera_index, backend)
        if not cap.isOpened():
            return "Error: Backend {} could not open camera.".format(backend_name) 
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

        num_frames = 100
        start_time = time.time()

        for _ in range(num_frames):
            ret, frame = cap.read()
            if not ret:
                return "Error: Frame capture failed with backend {}.".format(backend_name)


        end_time = time.time()
        duration = end_time - start_time

        if duration <= 0:
            return "Error: Duration for frame capture is zero or negative."

        avg_fps = num_frames / duration
        return avg_fps

    except Exception as e:
        return "An error occurred: {}".format(e)

    finally:
        if 'cap' in locals() and cap.isOpened():
            cap.release()

if __name__ == "__main__":
    camera_index = "./videos//file_example_MP4_1920_18MG.mp4"
    # camera_index = 2
    frame_sizes = [(640, 480), (1280, 720), (1920, 1080)]  # Add more sizes as needed
    backends = [
        (cv2.CAP_ANY, "CAP_ANY"),
        (cv2.CAP_V4L2, "CAP_V4L2"),
        (cv2.CAP_FIREWIRE, "CAP_FIREWIRE"),
        # (cv2.CAP_FFMPEG, "CAP_FFMPEG"),
        (cv2.CAP_GSTREAMER, "CAP_GSTREAMER"),
        (cv2.CAP_IMAGES, "CAP_IMAGES"),
        (cv2.CAP_DSHOW, "CAP_DSHOW"),
        (cv2.CAP_MSMF, "CAP_MSMF"),
        # (cv2.CAP_OPENCV_MJPEG, "CAP_OPENCV_MJPEG"),
        # Add more if necessary
    ]

    results = []
    for frame_width, frame_height in frame_sizes:
        for backend, backend_name in backends:
            result = capture_video(frame_width, frame_height, backend, backend_name, camera_index)
            if isinstance(result, float):
                results.append((backend_name, frame_width, frame_height, result))
            else:
                print(result)  # Print errors and warnings

    print("\n\nPython Version: {}".format(sys.version))
    print("OpenCV Version: {}\n".format(cv2.__version__))

    print("FPS Results:")
    for backend_name, width, height, fps in results:
        print("Backend: {}, Frame Size: {}x{}, Average FPS: {}".format(backend_name, width, height, fps))
