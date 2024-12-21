import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from batch.utils.video_processor import process_video

if __name__ == "__main__":
    process_video('b.mp4')