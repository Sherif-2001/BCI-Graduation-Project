import numpy as np
import time
from pylsl import StreamInfo, StreamOutlet, local_clock

# Define channel names
channel_names = ['C3', 'CZ', 'C4', 'FCZ', 'FC3', 'CP4', 'CPZ', 'CP3', 'FC4']

# Create a StreamInfo object
stream_name = 'EEGStream'
num_channels = len(channel_names)
sample_rate = 500
info = StreamInfo(stream_name, 'EEG', num_channels, sample_rate, 'float32', 'myuid34234')

# Add channel names to the StreamInfo object
channels = info.desc().append_child("channels")
for name in channel_names:
    channels.append_child("channel").append_child_value("label", name)

# Create a StreamOutlet object
outlet = StreamOutlet(info)

# Load saved data from file
# Assuming the saved data is in a CSV file with shape (num_samples, num_channels)
# saved_data = np.loadtxt('saved_eeg_data.csv', delimiter=',')
# combined_data = np.load("combined_magdy_Release.npy")
combined_data = np.load("E:\BCI\GP Repos\BCI-Graduation-Project\Manual_stream\combined_magdy_Release.npy")
transposed_eeg_buffer = combined_data.T


# Simulate streaming the data
for sample in transposed_eeg_buffer:
    outlet.push_sample(sample)
    time.sleep(1 / sample_rate)  # Simulate the real-time sampling rate
# # Simulate streaming the data
# for sample in saved_data:
#     outlet.push_sample(sample, local_clock())
#     time.sleep(1 / sample_rate)  # Simulate the real-time sampling rate
