from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import random
from pylsl import StreamInlet, resolve_stream
import time
import csv
import threading

import os
# //////////////////// EEG Recording Functions //////////////////////////

def connect_to_stream():
    # Resolve an EEG stream
    print("Looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')
    if not streams:
        print("No EEG stream found.")
        return False
    # Create a stream inlet
    inlet = StreamInlet(streams[0])
    return inlet

def extract_stream_info():
    inlet = connect_to_stream()
    info = inlet.info()
    description = info.desc()

    sfreq = info.nominal_srate()
    n_chan = info.channel_count()

    ch = description.child('channels').first_child()
    ch_names = [ch.child_value('label')]

    for i in range(n_chan):
        ch = ch.next_sibling()
        ch_names.append(ch.child_value('label'))
    old_channels = ch_names
    ch_names = [item.split('\n')[0] for item in old_channels]

    inlet.close_stream()
    return sfreq, ch_names


def record_eeg_to_csv(filename, sfreq, ch_names, duration=10):
    # Connect an EEG stream
    inlet = connect_to_stream()

    # Initialize a CSV writer
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header containing channel names
        header = ["Timestamp"] + ch_names[0:-1]
        csv_writer.writerow(header)
        
        # Record EEG data
        f = inlet.flush()
        print("Start")
        sample, timestamp = inlet.pull_sample()
        start_time = timestamp
        csv_writer.writerow([timestamp-start_time] + sample)
        p_start_time = time.time()
        # print(p_start_time)
        # while (time.time() - start_time) < record_duration:
        while (timestamp - start_time) < duration:
            sample, timestamp = inlet.pull_sample()
            # Write the timestamp and sample data to the CSV file
            csv_writer.writerow([timestamp-start_time] + sample)
    current_time = time.time()
    delta = current_time-p_start_time
    print(F"Recording Time : {delta} ")

    inlet.close_stream()
    inlet.flush()
    print("Recording complete.")

    return True
