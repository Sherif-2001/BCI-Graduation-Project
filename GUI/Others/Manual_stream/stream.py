import numpy as np
import time
from pylsl import StreamInfo, StreamOutlet

# Create a StreamInfo object
stream_name = 'EEGStream'
num_channels = 9
sample_rate = 500
info = StreamInfo(stream_name, 'EEG', num_channels, sample_rate, 'float32', 'myuid34234')

# Create a StreamOutlet object
outlet = StreamOutlet(info)

# Load saved data from file
# Assuming the saved data is in a CSV file with shape (num_samples, num_channels)
saved_data = np.loadtxt('saved_eeg_data.csv', delimiter=',')

# Simulate streaming the data
for sample in saved_data:
    outlet.push_sample(sample)
    time.sleep(1 / sample_rate)  # Simulate the real-time sampling rate
