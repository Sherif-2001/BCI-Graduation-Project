# BCI-based FES for Hand Rehabilitation

Welcome to the BCI-based FES for Hand Rehabilitation project! This project aims to assist in the rehabilitation of hand movements for patients through the use of Brain-Computer Interface (BCI) and Functional Electrical Stimulation (FES). The system reads brain signals, processes them through an AI model, and uses FES to stimulate specific muscles in the patient's arm. Additionally, a glove measures hand angles to ensure correct movement execution, and a comprehensive GUI facilitates session management and progress tracking.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [System Components](#system-components)
- [Setup and Installation](#setup-and-installation)
- [How to Use](#how-to-use)
- [Calibration](#calibration)
- [Rehabilitation Sessions](#rehabilitation-sessions)
- [Network and Communication](#network-and-communication)
- [Development](#development)
- [Data Collection](#data-collection)
- [Methodology](#methodology)
- [Results and Discussion](#results-and-discussion)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [Contributors](#contributors)
- [License](#license)

## Introduction

This project integrates BCI and FES technologies to aid in hand rehabilitation. By translating brain signals into electrical stimulations, patients can perform specific hand movements. The system includes a glove to measure hand angles and a GUI to manage rehabilitation sessions, calibrate devices, monitor brain signals, and collect data.

## Features

- **BCI Integration**: Reads brain signals and inputs them to an AI model.
- **AI Model**: Converts brain signals into commands for the FES device.
- **FES Device**: Controls electrodes on the patient's arm to stimulate specific muscles.
- **Measurement Glove**: Measures hand angles to verify correct movement execution.
- **Microcontroller**: Processes data from the glove and sends it to the GUI.
- **Comprehensive GUI**: Manages sessions, calibrates devices, monitors brain signals, and collects data.
- **Progress Reports**: Generates reports at the end of each session for clinicians.

## System Components

- **BCI Device**: Captures brain signals from the patient.
- **AI Model**: Processes brain signals to generate movement commands.
- **FES Device**: Receives commands and stimulates the patient's arm muscles via electrodes.
- **Measurement Glove**: Detects hand angles to verify movements.
- **Microcontroller**: Processes glove data and communicates with the GUI.
- **GUI**: Built to manage rehabilitation sessions, calibration, signal monitoring, and data collection.

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Omar-Saad-ELGharbawy/BCI-Graduation-Project
Hardware Setup:

BCI Device: Set up the BCI device according to the manufacturer's instructions.
FES Device: Connect the FES device to the patient's arm and ensure all electrodes are properly placed.
Measurement Glove: Fit the glove on the patient's hand and connect it to the microcontroller.
Software Setup:

Ensure you have the required software installed (e.g., Python, necessary libraries for AI model, microcontroller firmware, etc.).
Open the project in your preferred development environment.
How to Use
Calibration
BCI Device Calibration: Follow the on-screen instructions in the GUI to calibrate the BCI device.
Glove Calibration: Use the GUI to calibrate the measurement glove, ensuring accurate hand angle measurements.
Rehabilitation Sessions
Start a Session: Use the GUI to start a new rehabilitation session.
Monitor Brain Signals: The GUI displays real-time brain signal data from the BCI device.
Execute Movements: The AI model processes brain signals and sends commands to the FES device, stimulating specific muscles for desired hand movements.
Verify Movements: The measurement glove checks if the movements were executed correctly and sends data to the microcontroller.
Track Progress: At the end of each session, a detailed report is generated for the clinician to review the patient's progress.
Network and Communication
Our system involves a coordinated interaction between three primary modules: the Master CPU (Decision Module), the FES MC (Action Module), and the Glove MC (Feedback Module). These modules communicate wirelessly using User Datagram Protocol (UDP) and ESP-NOW protocol due to its low-latency and reliable data transmission.

Communication Flow
Master CPU (Decision Module):

EEG Signal Processing and AI Model: Uses the Lab Streaming Layer (LSL) protocol to receive EEG signals and the AI model to analyze motor imagery patterns to identify user intentions.
Glove State Handling: Manages the operational state of the glove, ensuring proper feedback is provided.
Graphical User Interface (GUI): Provides an intuitive interface for monitoring and controlling systems.
Reporting: Gathers and presents performance data and system logs for analysis.
FES MC (Action Module):

FES Parameters: Manages the intensity required for efficient function performance.
Pulse Generation: Produces the electrical pulses necessary for muscle stimulation.
Grasp-Release Functions: Executes the commands for grasp and release actions based on the decision from the Master CPU.
Glove MC (Feedback Module):

Angles Acquisition: Continuously measures and reports the angles of the user's fingers.
State Reporting: Indicates the current state of the glove, whether it is in grasp or release mode.
Communication Messages
The integration is performed through seven messages:

Message 1: Initial FES Parameters (one time per session)
Message 2: Glove Calibration (one time per session)
Message 3: Angles from the glove
Message 4: State of grasping/releasing
Message 5: Decision of grasp/release
Message 6: Channel ON for grasp/release
Message 7: Real-time FES Parameters
Development
This project was developed using a combination of hardware and software components. The AI model was built using TensorFlow and the GUI was developed using PyQt. The microcontroller firmware was written in C, and data communication between components was handled via UDP and ESP-NOW protocols.

Data Collection
Public Dataset: Clinical Brain-Computer Interfaces Challenge WCCI 2020 Glasgow dataset.
Collected Data: EEG data from 4 subjects, recorded using Neuron Spectrum EEG device at 500 Hz.
Data Collection Protocol
Channels: Nine channels: C3, CZ, C4, FCZ, FC3, CP4, CPZ, CP3, FC4
Tasks: Hand Grasp Imagination, Hand Release Imagination, Baseline
Each session: 30 trials per task, 6 seconds per trial
Methodology
Data Pre-processing
Baseline Correction: Removing DC offsets and slow drifts.
Band-Pass Filtering: Retaining alpha (8-13 Hz) and beta (13-30 Hz) bands.
Trial Trimming: Removing the first and last seconds of each trial.
Feature Extraction and Classification
CSP and FBCSP: Enhancing discriminative power.
Deep Learning and Machine Learning Models: Achieving high accuracy in classifying motor imagery tasks.
Results and Discussion
AI Model Performance:
FBCSP + LDA: 85% accuracy within subjects.
EEG Inception MI: 88% accuracy across subjects.
Collected Data: 79% average accuracy using a hard-voting ensemble classifier with a 2-second EEG data window.
Conclusion
The integration of BCI and FES technologies enhances hand rehabilitation by interpreting user intentions and providing precise muscle stimulation. The system's effectiveness is supported by real-time feedback from a specialized glove and a comprehensive GUI for monitoring and control.

Future Work
Improving model accuracy with more data.
Enhancing FES circuit for better control.
Upgrading glove sensors for reduced delay.
Implementing expert handling and a training phase for optimal use.
Contributors
Dina Abrahim
Neveen Hassan
Omar Mansour
Omar Elgharbawy
Sherif Ahmed
Aliaa Rehan Youssef