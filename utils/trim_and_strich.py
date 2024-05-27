import cv2
from tqdm import tqdm


# Function to concatenate videos vertically
def concat_vertical(video1, video2, output_path):
    cap1 = cv2.VideoCapture(video1)
    cap2 = cv2.VideoCapture(video2)

    # Find the minimum length (in frames) between the two videos
    min_frames = min(int(cap1.get(cv2.CAP_PROP_FRAME_COUNT)), int(cap2.get(cv2.CAP_PROP_FRAME_COUNT)))

    # Video properties
    fps = cap1.get(cv2.CAP_PROP_FPS)
    width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
    width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
    height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Use the larger width for both videos
    max_width = max(width1, width2)
    max_height = max(height1, height2)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Adjust codec as needed
    out = cv2.VideoWriter(output_path, fourcc, 14, (width1 + width2, max_height))

    # for _ in range(min_frames):
    for _ in tqdm(range(min_frames), desc="Processing Frames"):
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if ret1 and ret2:
            # Resize frames to have the same width if necessary
            if frame1.shape[1] != max_width:
                # frame1 = cv2.resize(frame1, (max_width, height1))
                frame1 = cv2.resize(frame1, (width1, max_height))
            if frame2.shape[1] != max_width:
                # frame2 = cv2.resize(frame2, (max_width, height2))
                frame2 = cv2.resize(frame2, (width2, max_height))

            # Concatenate frames vertically
            combined_frame = cv2.hconcat([frame1, frame2])
            out.write(combined_frame)
        else:
            break

    # Release everything
    cap1.release()
    cap2.release()
    out.release()

# Example usage
video1_path = './videos/Screen_Recording_20231212_140844.mp4'
video2_path = './videos/Screen_Recording_20231212_140845.mp4'
output_video_path = './videos/combined_video_h_0.mp4'

concat_vertical(video1_path, video2_path, output_video_path)
