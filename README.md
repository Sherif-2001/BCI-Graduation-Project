# Hand Rehabilitation System Using Functional Electrical Stimulation (FES) Based on Brain-Computer Interface (BCI)

## Table of Contents
- [Overview](#project-overview)
- [Features](#features)
- [System Components](#system-components)
- [Setup and Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Results and Discussion](#results)
- [Future Work](#future-work)
- [Team](#team)
- [Acknowledgements](#acknowledgements)
- [References](#references)

## Project Overview

Hand function impairment, including paralysis or muscle weakness (paresis), often results from neurological disorders such as stroke, spinal cord injury, and traumatic brain injury. This project presents an innovative rehabilitation system that integrates Brain-Computer Interface (BCI) technology with Functional Electrical Stimulation (FES) to address these challenges. The system captures brain electroencephalography (EEG) signals using Motor Imagery techniques, classifies these signals with an AI model, and activates FES to stimulate the relevant muscles, enabling the intended hand movements.

## Features
- **BCI Module**: Captures and processes EEG signals using Motor Imagery techniques.
- **FES Module**: Stimulates muscle contraction through electrical impulses.
- **AI Integration**: Classifies EEG signals to interpret user intentions.
- **Feedback Glove**: Provides real-time feedback on hand movements to ensure correct execution.
- **GUI**: Monitors system parameters, allows EEG recording, and maintains a patient database with electronic reports.
- **IoT Network**: Integrates all system components for seamless communication and control.

## System Components

1. **Brain-Computer Interface (BCI)**
   - **EEG Data Acquisition**: Captures brain signals using a Neuron Spectrum EEG device.
   - **Pre-processing**: Applies baseline correction, band-pass filtering, and trial trimming.
   - **Feature Extraction**: Utilizes Common Spatial Patterns (CSP) and Filter Bank Common Spatial Patterns (FBCSP).
   - **Classification**: Employs AI models such as SVM, MLP, LDA, Logistic Regression, and Extra Trees.

2. **Functional Electrical Stimulation (FES)**
   - **Stimulation Parameters**: Adjustable frequency, intensity, and pulse duration.
   - **Therapy Protocols**: Supports various hand function training patterns.
   - **Safety Features**: Includes isolation transformers, diodes, digital potentiometers, and software protection.

3. **Feedback Glove**
   - **Design**: Comfortable and flexible, equipped with sensors to measure finger angles.
   - **Functionality**: Uses hall effect sensors to detect magnetic field changes during finger movements.

4. **Graphical User Interface (GUI)**
   - **Control and Monitoring**: Provides an intuitive interface for system control and parameter monitoring.
   - **Reporting**: Gathers and presents performance data and system logs for analysis.

5. **IoT Network**
   - **Integration and Communication Flow**: Ensures coordinated interaction between the Master CPU (Decision Module), FES MC (Action Module), and Glove MC (Feedback Module).
   - **Message Protocol**: Utilizes seven messages for communication, with continuous data exchange for real-time operation.
   - **Communication Technologies**: Employs User Datagram Protocol (UDP) and ESP-NOW for low-latency and reliable data transmission.

   ### Messages Transmitted Through Modules
   | Message | Description | Sender | Receiver
   | ----------- | ----------- | ----------- | ----------- |
   | Message 1 | FES Initial Parameters | GUI | FES |
   | Message 2 | Glove Calibration | FES | Glove |
   | Message 3 | Angles Acquisition | Glove | GUI |
   | Message 4 | State Reporting | Glove | GUI |
   | Message 5 | Decision (Grasp/Release) | GUI | Glove |
   | Message 6 | Channel ON (Grasp/Release) | Glove | FES |
   | Message 7 | Realtime FES parameters | FES | GUI |

   ### Master CPU (Decision Module)
   - **EEG Signal Processing and AI Model**: Uses Lab Streaming Layer (LSL) protocol to receive EEG signals and AI models to analyze motor imagery patterns.
   - **Glove State Handling**: Manages the operational state of the glove, ensuring proper feedback.
   - **GUI**: Provides an intuitive interface for monitoring and controlling the system.
   - **Reporting**: Gathers and presents performance data and system logs.

   ### FES MC (Action Module)
   - **FES Parameters**: Manages intensity required for efficient function performance.
   - **Pulse Generation**: Produces electrical pulses for muscle stimulation.
   - **Grasp-Release Functions**: Executes commands for grasp and release actions.

   ### Glove MC (Feedback Module)
   - **Angles Acquisition**: Continuously measures and reports the angles of the user's fingers.
   - **State Reporting**: Indicates the current state of the glove (grasp or release mode).

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Omar-Saad-ELGharbawy/BCI-Graduation-Project

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the EEG device and FES system according to the provided documentation.

4. **Run the GUI application**:
   ```bash
   python main.py
   ```

## Usage

### Calibrate the System:
 - Set initial FES parameters.
 - Perform glove calibration.

### Begin a Session:
 - Start the EEG recording.
 - Follow the on-screen instructions for Motor Imagery tasks.

### Monitor Progress:
 - Use the GUI to monitor real-time feedback and adjust parameters as needed.
 - Review session reports to track patient progress.

## Dataset
 - The project utilizes both a public online dataset and collected data for training and validation.
 - Public Dataset: Clinical Brain-Computer Interfaces Challenge WCCI 2020 Glasgow dataset. [Dataset](https://github.com/5anirban9/Clinical-Brain-Computer-Interfaces-Challenge-WCCI-2020-Glasgow)

## Results
The system achieved an average prediction accuracy of 79% for real-time predictions using a 2-second window of EEG data. The use of real-time feedback and adjustable FES parameters significantly improved rehabilitation outcomes compared to fixed parameters.

## Future Work
1. Collect more data to improve model accuracy.
2. Enhance the FES circuit for better control.
3. Improve glove sensor sensitivity to reduce delay.

## Team
| Team Members' Names                                  |   CV    |
|------------------------------------------------------|:-------:|
| [Dina Hussam](https://github.com/Dinahussam)         |         |
| [Neveen Mohamed](https://github.com/NeveenMohamed)   |         |
| [Omar Ahmed ](https://github.com/omaranwar21)        |         |
| [Omar Saad ](https://github.com/Omar-Saad-ELGharbawy)|         |
| [Sherif Ahmed](https://github.com/Sherif-2001)       |         |


## Acknowledgements
Supervised by Dr. Aliaa Rehan Youssef, Department of Systems and Biomedical Engineering, Cairo University.

## References
- [Choi, I., Kwon, G. H., Lee, S., & Nam, C. S. (2020). Functional electrical stimulation controlled by motor imagery brain-computer interface for rehabilitation. Brain Sciences, 10(8), 512.](https://www.mdpi.com/2076-3425/10/8/512)
- [Ang, Kai Keng, et al. "Filter bank common spatial pattern (FBCSP) in brain-computer interface." 2008 IEEE international joint conference on neural networks (IEEE world congress on computational intelligence). IEEE, 2008.](https://www.researchgate.net/publication/224330976_Filter_Bank_Common_Spatial_Pattern_FBCSP_in_brain-computer_interface)
- [Zhang, C., Kim, Y. K., & Eskandarian, A. (2021). EEG-inception: an accurate and robust end-to-end neural network for EEG-based motor imagery classification. Journal of Neural Engineering, 18(4), 046014.](https://www.researchgate.net/publication/349984885_EEG-inception_An_accurate_and_robust_end-to-end_neural_network_for_EEG-based_motor_imagery_classification)
