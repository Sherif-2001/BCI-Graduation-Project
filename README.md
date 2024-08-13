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
- [Development](#development)

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

2. **Hardware Setup**:
- BCI Device: Set up the BCI device according to the manufacturer's instructions.
- FES Device: Connect the FES device to the patient's arm and ensure all electrodes are properly placed.
- Measurement Glove: Fit the glove on the patient's hand and connect it to the microcontroller.

3. **Software Setup**:
- Ensure you have the required software installed (e.g., Python, necessary libraries for AI model, microcontroller firmware, etc.).
- Open the project in your preferred development environment.

## How to Use
### Calibration
- BCI Device Calibration: Follow the on-screen instructions in the GUI to calibrate the BCI device.
- Glove Calibration: Use the GUI to calibrate the measurement glove, ensuring accurate hand angle measurements.

### Rehabilitation Sessions
1. Start a Session: Use the GUI to start a new rehabilitation session.
2. Monitor Brain Signals: The GUI displays real-time brain signal data from the BCI device.
3. Execute Movements: The AI model processes brain signals and sends commands to the FES device, stimulating specific muscles for desired hand movements.
4. Verify Movements: The measurement glove checks if the movements were executed correctly and sends data to the microcontroller.
5. Track Progress: At the end of each session, a detailed report is generated for the clinician to review the patient's progress.

## Development
This project was developed using a combination of hardware and software components. The AI model was built using [specify AI framework], and the GUI was developed using **PyQt**. The microcontroller firmware was written in **C**, and data communication between components was handled via [specify protocol].
