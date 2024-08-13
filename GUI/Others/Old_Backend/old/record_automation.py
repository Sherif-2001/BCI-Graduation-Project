from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import random
from pylsl import StreamInlet, resolve_stream
import time
import csv
import threading
import os

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 429)
        MainWindow.setStyleSheet("background-color:#265073;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("qproperty-alignment: AlignCenter;\n"
"text-align:center;")
        self.widget.setObjectName("widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        # //////////////////////// Grasp Release Paper ////////////////////////
        self.grasp_release_label_6 = QtWidgets.QLabel(self.widget)
        self.grasp_release_label_6.setStyleSheet("qproperty-alignment: AlignCenter;\n"
"text-align:center;\n"
"font: 700 20pt; \n"
"color:rgb(255, 255, 255);\n"
"")
        self.grasp_release_label_6.setObjectName("grasp_release_label_6")
        self.horizontalLayout_6.addWidget(self.grasp_release_label_6)
        # //////////////////////// End of Grasp Release Paper ////////////////////////
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.gridLayout.addWidget(self.widget, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)
        self.photo_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.photo_widget.sizePolicy().hasHeightForWidth())
        self.photo_widget.setSizePolicy(sizePolicy)
        self.photo_widget.setMinimumSize(QtCore.QSize(352, 111))
        self.photo_widget.setSizeIncrement(QtCore.QSize(1, 1))
        self.photo_widget.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.photo_widget.setObjectName("photo_widget")
        # //////////////////////// Image Label ////////////////////////
        self.imageLabel = QtWidgets.QLabel(self.photo_widget)
        self.imageLabel.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        
        # Image paths
        self.grasp_img_path = "Imgs/Grasp.png"
        self.release_img_path = "Imgs/Release.jpeg"

        # Create a layout for the photo_widget and add the imageLabel to it
        self.photoLayout = QtWidgets.QVBoxLayout(self.photo_widget)
        self.photoLayout.addWidget(self.imageLabel)

        # //////////////////////// End of Image Label ////////////////////////
        self.gridLayout.addWidget(self.photo_widget, 3, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("QMenuBar::item:selected { /* when mouse hover */\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Load alarm sound
        self.alarm_sound = QMediaPlayer()
        self.alarm_sound.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile("alarm.wav")))

        # Timer to alternate tasks and images
        self.get_ready_timer = QtCore.QTimer(MainWindow)
        self.get_ready_timer.timeout.connect(self.show_get_ready)

        self.rest_timer = QtCore.QTimer(MainWindow)
        self.rest_timer.timeout.connect(self.show_rest)

        self.current_task_index = 0

        # Task list
        tasks = ['Right Grasp', 'Right Release']
        repetitions = 2

        # Generate a list with each name repeated 20 times
        self.task_repeated = [task for task in tasks for _ in range(repetitions)]

        # Shuffle the list to randomize the order
        random.shuffle(self.task_repeated)

        # Start the initial cycle after 5 seconds
        QtCore.QTimer.singleShot(5000, self.show_get_ready)

    def on_resize(self, event):
        self.resize_image()
        event.accept()

    def resize_image(self):
        if self.current_task_index < len(self.task_repeated):
            task = self.task_repeated[self.current_task_index]
            if "Grasp" in task:
                current_image_path = self.grasp_img_path
            elif "Release" in task:
                current_image_path = self.release_img_path
            else:
                current_image_path = None

            if current_image_path:
                self.imageLabel.setPixmap(QtGui.QPixmap(current_image_path).scaled(self.photo_widget.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            else:
                self.imageLabel.clear()

    def show_get_ready(self):
        self.grasp_release_label_6.setText("Get Ready")
        self.imageLabel.clear()
        self.alarm_sound.play()
        self.get_ready_timer.stop()
        QtCore.QTimer.singleShot(2000, self.show_task)  # Show task after "Get Ready" for 2 seconds

    def show_task(self):
        if self.current_task_index < len(self.task_repeated):
            task = self.task_repeated[self.current_task_index]
            self.grasp_release_label_6.setText(task)
            if "Grasp" in task:
                self.imageLabel.setPixmap(QtGui.QPixmap(self.grasp_img_path).scaled(self.photo_widget.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            elif "Release" in task:
                self.imageLabel.setPixmap(QtGui.QPixmap(self.release_img_path).scaled(self.photo_widget.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            else:
                self.imageLabel.clear()

            sub_name = "sherif"
            session_num = 1
            run = self.current_task_index + 1
            folder_path = "Records\sherif"            
            file_name = f"sub-{sub_name}_ses-{session_num}_task-{task}_run-{run}_eeg.csv"

            # add folder path and file name to file path
            file_path = os.path.join(folder_path, file_name)

            print(f"Trial {run}: {task}")  # Print the file name to the terminal
            print(file_name)  # Print the file name to the terminal
            print(file_path)  # Print the file name to the terminal

            # Start a new thread for EEG recording
            self.eeg_thread = threading.Thread(target=self.record_eeg, args=(file_path,))
            self.eeg_thread.start()

    def record_eeg(self, file_name):
        # Record EEG data
        if record_eeg_to_csv(file_name, self.sfreq, self.ch_names, 1):
            print("Recording Done")
            self.current_task_index += 1
            QtCore.QTimer.singleShot(0, self.show_rest)  # Show rest immediately after task is done

    def show_rest(self):
        self.grasp_release_label_6.setText("Stop take rest")
        self.imageLabel.clear()
        self.rest_timer.stop()
        QtCore.QTimer.singleShot(4000, self.show_get_ready)  # Show rest message for 4 seconds, then show "Get Ready"

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Patient Screen"))
        self.grasp_release_label_6.setText(_translate("MainWindow", "The session has not started yet"))

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

# //////////////////// Main Code //////////////////////////

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_MainWindow()

    # Extract EEG stream info
    MainWindow.sfreq, MainWindow.ch_names = extract_stream_info()

    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
