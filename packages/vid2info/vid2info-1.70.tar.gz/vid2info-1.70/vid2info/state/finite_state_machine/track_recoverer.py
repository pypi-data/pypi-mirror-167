import numpy as np
from warnings import warn
from time import time

from vid2info.utils.general import iou

from vid2info.state.config import DIFFERENCE_TO_CONSIDER_ELEMENT_LEFT_SCENE_IN_SECONDS, MIN_IOU_TO_CONSIDER_OVERLAP, \
    OUT_CLASS_NAME, OUT_TIMESTAMP

from vid2info.state.finite_state_machine.element_finite_state_machine import ElementFiniteStateMachine


class TrackRecoverer:
    def __init__(self, finite_state_machines_config: dict, recover_track_attempts: int = 10):
        self.state_buffer = None # Must be initialized before recovering track_ids.
        self.finite_state_machines_config = finite_state_machines_config
        self.recover_tracks_attempts = {}
        self.recovered_tracks_correspondences = {}
        self.max_recover_track_attempts = recover_track_attempts


    def recover_track_id_from_state_machine(self, last_detection, track_id: int, current_class: str | None = None, bbox_xyxy: np.ndarray | None = None,
                                  recover_default_machines: bool = False, in_scene_tracks: tuple | list = ()) -> ElementFiniteStateMachine | None:
        """
        Returns the state machine of the element with the given track_id. If this element is new,
        it will create a new state machine using the configs given in element_state_machine_configs.

        :param track_id: int. The track_id of the element.
        :param current_class : str | None. The current class of the element, only used if the element is new.
        :param bbox_xyxy: np.ndarray | None. The bounding box of the element, only used if the element is new.
        :param recover_default_machines: bool. If True, the default state machines will be recovered if the element is new.
        :param in_scene_tracks: tuple | list. The tracks of the elements that are actually in the scene. Only used if
                recover_default_machines is True.

        :return ElementFiniteStateMachine. The current state machine of the element.
        """
        assert self.state_buffer is not None, "The state buffer must be initialized before recovering track_ids."
        finite_state_machine = last_detection.finite_state_machine if last_detection is not None else None
        if finite_state_machine is None:
            assert current_class is not None, "If the element is new, the current class must be given."
            if current_class not in self.finite_state_machines_config:
                assert 'default' in self.finite_state_machines_config, f"Element class {current_class} not found " \
                                                                       f"in finite state machine configs and no default " \
                                                                       f"config found."
                if recover_default_machines:
                    recovered_track_id = self.recover_track_id(class_name=current_class, bbox_xyxy=bbox_xyxy,
                                                               in_scene_tracks=in_scene_tracks)
                    print(f"Recovered track_id {recovered_track_id} for original {track_id}")
                    if recovered_track_id is not None:
                        self.recovered_tracks_correspondences[track_id] = recovered_track_id
                        if track_id in self.recover_tracks_attempts:
                            print(f"Recovered track {track_id} with track {recovered_track_id} after {self.recover_tracks_attempts[track_id]} attempts.")
                        return self.state_buffer.get_element_state_machine(track_id=recovered_track_id, current_class=current_class,
                                                               recover_default_machines=False)
                    else:
                        self.recover_tracks_attempts[track_id] = self.recover_tracks_attempts.get(track_id, 0) + 1
                        # We will set this state machine temporally as None, so we can recover it later.
                        if self.recover_tracks_attempts[track_id] < self.max_recover_track_attempts:
                            print(f"Could not recover track {track_id} after {self.recover_tracks_attempts[track_id]} attempts.")
                            return None
                        else:
                            print(f"Generating default state machine for track {track_id} after {self.recover_tracks_attempts[track_id]} attempts.")

                warn(f"Element class {current_class} not found in finite state machine configs. Using default")
                current_class = 'default'
            config = self.finite_state_machines_config[current_class]
            finite_state_machine = ElementFiniteStateMachine(config=config)
        return finite_state_machine

    def recover_track_id(self, class_name: str, bbox_xyxy: np.ndarray,
                         max_difference_in_seconds: float | int = DIFFERENCE_TO_CONSIDER_ELEMENT_LEFT_SCENE_IN_SECONDS,
                         in_scene_tracks : list | tuple = (),
                         min_iou: float = MIN_IOU_TO_CONSIDER_OVERLAP) -> int | None:
        """
        Tries to recover the track_id of an element for which we suspect that the track_id could have been lost
        given its finite_state_machine. If the track_id is recovered, it will be returned. If not, None will be returned.

        NOTE: This is only reliable when the elements are very static. Do not relay in this function if your elements
        are moving and tends to be overlapping between them.

        :param class_name: str. The current class detected for that element.
        :param bbox_xyxy: np.ndarray. The current bounding box of the element.
        :param in_scene_tracks: list | tuple. The tracks of the elements that are actually in the scene.
        :param max_difference_in_seconds: float | int. The maximum time difference in seconds to consider than
                                                an element in the history has not checked.
        :param min_iou: float. The minimum IoU between the bounding boxes of the element and the elements in the scene.

        :return int | None. The track_id of the element if it is recovered, None otherwise.
        """

        current_time = time()
        # Search in the elements_history for those elements that have the same out_class_name than our current class.
        suspicious_track_ids = []
        for track_id, element_info in self.state_buffer.elements_history.items():
            # If the class is the same as the output class of the element and the time difference is short enough
            if track_id not in in_scene_tracks and element_info[OUT_CLASS_NAME] == class_name and \
                    element_info[OUT_TIMESTAMP] > current_time - max_difference_in_seconds:
                # Consider it as suspicious
                suspicious_track_ids.append(track_id)
        if len(suspicious_track_ids) > 0:
            # Check for the closer bbox to the current bbox
            suspicious_bboxes = [self.state_buffer.get_biggest_bbox_of_element(track_id=suspicious_track_id)
                                 for suspicious_track_id in suspicious_track_ids]
            # Get the intersection over union (IoU) between the current bbox and each suspicious bbox
            iou_values = [iou(bbox_xyxy, suspicious_bbox) if suspicious_bbox is not None else 0.
                          for suspicious_bbox in suspicious_bboxes]
            assert len(iou_values) == len(suspicious_track_ids), "The number of IoU values must be the same as the " \
                                                                    "number of suspicious track_ids. Got " \
                                                                    f"{len(iou_values)} and {len(suspicious_track_ids)}"
            if any(iou_value > min_iou for iou_value in iou_values):
                # Get the index of the biggest IoU value
                max_iou_index = np.argmax(iou_values)
                old_track_id = suspicious_track_ids[max_iou_index]
                return old_track_id
            else:
                print(f"Could not recover track_id for element with class {class_name} and bbox {bbox_xyxy}.")

        return None

    def track_id_is_being_recovered(self, track_id: int, state_machine: ElementFiniteStateMachine | None = None) -> bool:
        """
        Checks if the given track_id is being recovered or not.

        :param track_id: int. The track_id to check.
        :param state_machine: ElementFiniteStateMachine | None. The state machine of the element with the given
            track_id or None. When using the recoverer together with finite_state_machines (as always will happen),
            this function will only return True if the state_machine is None. This is because the recoverer will
            not assign any state machine while trying to recover the track_id.

        :return bool. True if the track_id is being recovered, False otherwise.
        """
        return track_id in self.recover_tracks_attempts and self.recover_tracks_attempts[track_id] < self.max_recover_track_attempts \
            and state_machine is None and track_id not in self.recovered_tracks_correspondences