import cv2
import os
import sys
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

def capture_and_save_video(codec, file_extension):
    try:
        cap = cv2.VideoCapture("parking_entrance.mp4")
        if not cap.isOpened():
            raise ValueError("Error: Camera could not be opened.")

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*codec)
        out = cv2.VideoWriter(f'videos/output_{codec}.{file_extension}', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

        print("Press 'q' to stop recording...")

        while True:
            ret, frame = cap.read()
            if not ret:
                raise ValueError("Error: Frame capture failed.")
            out.write(frame)

            # Display the resulting frame
            # cv2.imshow('Frame', frame)

            # # Break the loop when 'q' is pressed
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break

        return f"Video successfully saved with codec {codec}."

    except Exception as e:
        return f"An error occurred: {e}"

    finally:
        cap.release()
        out.release()
        # cv2.destroyAllWindows()


if __name__ == "__main__":
    codec_extension_pairs = [('XVID', 'avi'), ('MJPG', 'avi'), ('MP4V', 'mp4'), ('AVC1', 'mp4')]
    
    for codec, file_extension in codec_extension_pairs:
        result = capture_and_save_video(codec, file_extension)
        print(result)
