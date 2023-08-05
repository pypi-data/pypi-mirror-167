"""
The VideoReader class charges a video file and provides a way to access the frames.

Author: Eric Canas
Github: https://github.com/Eric-Canas
Email: eric@ericcanas.com
Date: 09-07-2022
"""

import os
import cv2
import numpy as np
from warnings import warn
import time

class VideoReader:
    def __init__(self, video_path: str, simulated_frame_rate: None | int = None, as_rgb: bool = False,
                 h: int | None = None, w: int|None = None, batch_size : int | None = None,
                 simulate_webcam: bool = True):
        """
        Initialize the VideoReader.
        :param video_path: str. Path to the video file.
        :param simulated_frame_rate: If not None, the iterator will yield the frames at the given simulated frame rate.
        It must be between 0 and the video real frame rate.
        :param as_rgb: If True, the frames will be returned as RGB instead of BGR.
        :param h: int or None. Height to resize the frames to. If None, the original height will be used, except if
                w is provided, in which case it will resize to keep the original aspect ratio.
        :param w: int or None. Width to resize the frames to. If None, the original width will be used, except if
                h is provided, in which case it will resize to keep the original aspect ratio.
        :param batch_size: int or None. If not None, the iterator will yield batches of frames (B, H, W, C), if
                None, the iterator will yield the frames as they are (H, W, C).
        :param simulate_webcam: If True, the iterator will simulate a webcam. It means that every time you ask for a frame you
                won't be really receiving the next frame, but the frame that would be given by a real webcam taking into account
                the current timestamp.
        """
        assert os.path.isfile(video_path), f'Video file {video_path} not found.'
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.frame_count = int(self.cap.get(propId=cv2.CAP_PROP_FRAME_COUNT))
        self.fps = int(self.cap.get(propId=cv2.CAP_PROP_FPS))
        self.frame_size_hw = (int(self.cap.get(propId=cv2.CAP_PROP_FRAME_HEIGHT)), int(self.cap.get(propId=cv2.CAP_PROP_FRAME_WIDTH)))

        if simulated_frame_rate is not None:
            assert 0 < simulated_frame_rate <= self.fps, f'Simulate frame rate {simulated_frame_rate} out of range. Must be' \
                                                       f' between 0 and the video real frame rate {self.fps}.'
            assert simulated_frame_rate == int(simulated_frame_rate), f'Simulate frame rate {simulated_frame_rate} must be an integer.'
        self.frames_offset = int(self.fps // simulated_frame_rate) if simulated_frame_rate is not None else 1
        self.as_rgb = as_rgb

        if h is not None or w is not None:
            # If one is None, calculate the other
            if sum(1 for x in (h, w) if x is None) == 1:
                h, w = self.calculate_frame_size_keeping_aspect_ratio(h=h, w=w)
            elif np.isclose(h/w, self.frame_size_hw[0]/self.frame_size_hw[1]):
                warn(f'Video_Reader have been set to resize videos to {h}x{w}, the original video aspect ratio '
                     f'will be lost {self.frame_size_hw[0]}x{self.frame_size_hw[1]}.', UserWarning)
            self.output_hw = (h, w)
        else:
            self.output_hw = self.frame_size_hw
        self.batch_size = batch_size

        self.start_timestamp = time.time()
        self.simulate_webcam = simulate_webcam
        if self.simulate_webcam:
            if simulated_frame_rate is not None:
                self.frames_offset = 1
                warn(f"simulated_frame_rate is nullified when using simulate_webcam. Set to None", UserWarning)

    @property
    def frame_index(self):
        return int(self.cap.get(propId=cv2.CAP_PROP_POS_FRAMES))

    @property
    def current_timestamp_seconds(self):
        return self.cap.get(propId=cv2.CAP_PROP_POS_MSEC) / 1000.0

    def __iter__(self):
        self.start_timestamp = time.time()
        self.cap.set(propId=cv2.CAP_PROP_POS_FRAMES, value=0)
        return self

    def __next__(self):
        if self.frame_index < self.frame_count - self.frames_offset:
            return self.read_next_frame()
        else:
            raise StopIteration

    def __del__(self):
        # Close the video
        self.cap.release()
        self.cap = None

    def __len__(self):
        return int(self.frame_count // self.frames_offset)

    def get_frame(self, frame_index: int, move_current_frame: bool = False) -> np.ndarray:
        """
        Get a frame from the video.

        :param frame_index: Index of the frame to get.
        :param move_current_frame: If True, the current frame will be moved to the given frame_index.

        :return: The frame at the given index as a numpy array (H x W x RGB).
        """
        assert frame_index < self.frame_count, f'Frame index {frame_index} out of range.'
        previous_frame = self.frame_index
        self.cap.set(propId=cv2.CAP_PROP_POS_FRAMES, value=frame_index)
        frame = self.read_next_frame()
        if not move_current_frame:
            self.cap.set(propId=cv2.CAP_PROP_POS_FRAMES, value=previous_frame-1)
        return frame

    def read_next_frame(self) -> np.ndarray:
        """
        Read the next frame from the video. (Skipping the frames_offset if it is greater than one.)
        """
        batch_size = 1 if self.batch_size is None else self.batch_size
        frames = []
        for i in range(batch_size):
            for _ in range(1, self.frames_offset):
                ret = self.cap.grab()
                if not ret:
                    if self.frame_index < self.frame_count:
                        if len(frames) > 0:
                            return frames[0] if self.batch_size is None else np.stack(frames, axis=0)
                        else:
                            warn(f'Frame could not be read, but the video have not finished. Frame index: {self.frame_index}.'
                                 f' Frame count: {self.frame_count}.', RuntimeWarning)
                    raise StopIteration("The video have finished.")
            # Get current video frame count
            ret, frame = self.cap.read() if not self.simulate_webcam else self.__get_webcam_simulated_frame()
            if not ret:
                if self.frame_index < self.frame_count:
                    warn(f'Frame could not be read, but the video have not finished. Frame index: {self.frame_index}.'
                         f' Frame count: {self.frame_count}.', RuntimeWarning)
                raise StopIteration("The video have finished.")
            else:
                if self.output_hw != self.frame_size_hw:
                    frame = cv2.resize(src=frame, dsize=self.output_hw[::-1])
            if self.as_rgb:
                frame = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2RGB, dst=frame)
            frames.append(frame)
        return frames[0] if self.batch_size is None else np.stack(frames, axis=0)

    def read_video_iterator(self, from_start: bool = False) -> np.ndarray:
        """
        Yields the frames of the video. If simulate_frame_rate is not None,
         the frames are yielded at the given simulated frame rate. That is, skipping real_frame_rate / simulate_frame_rate
         at each iteration.

        :param from_start: If True, the iterator will start from the beginning of the video.

        :return: The next frame in the video.
        """
        if from_start:
            self.cap.set(propId=cv2.CAP_PROP_POS_FRAMES, value=0)

        while self.frame_index < self.frame_count-self.frames_offset:
            img = self.read_next_frame()
            yield img
        raise StopIteration

    def __get_webcam_simulated_frame(self):
        current_second = time.time()
        current_video_second = current_second - self.start_timestamp
        seconds_by_frame = 1 / self.fps
        while self.current_timestamp_seconds < current_video_second+seconds_by_frame:
            ret = self.cap.grab()
            if not ret:
                raise StopIteration("The video have finished.")
        return self.cap.read()


    # --------------- AUXILIARY METHODS ---------------
    def calculate_frame_size_keeping_aspect_ratio(self, h:int | None, w:int|None) -> tuple[int, int]:
        """
        When only one of the frame size dimensions is given, the other one is calculated keeping the
        aspect ratio with the original video.

        :param h: int or None. Height of the frame. If None, w must be provided.
        :param w: int or None. Width of the frame. If None, h must be provided.
        :return: The height and width of the frame.
        """
        frame_h, frame_w = self.frame_size_hw
        if h is None and w is not None:
            h = int(round(frame_h * w / frame_w))
        elif h is not None and w is None:
            w = int(round(frame_w * h / frame_h))
        else:
            raise ValueError(f'Only one of the frame size dimensions must be provided. Got h={h} and w={w}.')
        return h, w
