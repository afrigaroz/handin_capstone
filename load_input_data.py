# load_input_data.py

"""
Loads shot and tracking data, and matches each shot to
the closest tracking frame using video timestamp.
"""

import json
import os

def load_shot_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def load_tracking_data(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    frames = [json.loads(line) for line in lines[1:]]  # skip metadata
    return frames

def get_closest_frame(frames, video_ts):
    return min(frames, key=lambda frame: abs(frame['vid_timestamp'] - video_ts))

def find_input_pair(match_id, shots_dir="shots", tracking_dir="jsonls"):
    shot_path = os.path.join(shots_dir, f"{match_id}.json")
    tracking_path = os.path.join(tracking_dir, f"{match_id}_tracking_data.jsonl")

    if not os.path.exists(shot_path):
        raise FileNotFoundError(f"Shot file not found: {shot_path}")
    if not os.path.exists(tracking_path):
        raise FileNotFoundError(f"Tracking file not found: {tracking_path}")

    shots = load_shot_data(shot_path)
    tracking_frames = load_tracking_data(tracking_path)

    input_pairs = []
    for shot in shots:
        video_ts = float(shot["videoTimestamp"])
        closest_frame = get_closest_frame(tracking_frames, video_ts)
        input_pairs.append((shot, closest_frame))

    return input_pairs
