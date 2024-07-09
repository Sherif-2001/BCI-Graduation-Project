import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, lfilter_zi, firwin
from time import sleep
from pylsl import StreamInlet, resolve_stream
from optparse import OptionParser
import seaborn as sns
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

sns.set(style="whitegrid")

class Ui_MainWindow(QtWidgets.QWidget):
    go_back = QtCore.pyqtSignal()
    go_to_automation = QtCore.pyqtSignal()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 662)
        MainWindow.setStyleSheet("background-color:#265073;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(120,120, 120);\n"
"border-radius:15;\n"
"color:rgb(255, 255, 255);\n"
"font: 25pt \"Forte\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(70, 70, 70);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 1, 1, 1)

        # Go back Button
        self.pushButton.clicked.connect(self.go_back.emit)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("qproperty-alignment: AlignCenter;\n"
"text-align:center;\n"
"font: 700 20pt; \n"
"color:rgb(255, 255, 255);\n"
"")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 5, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 5, 2, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius:15;\n"
"background-color:rgb(207, 0, 3);\n"
"color:rgb(255, 255, 255);\n"
"font: 25pt \"Forte\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(239, 0, 0);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 4, 1, 1)

        # Go to automation screen Button
        self.pushButton_2.clicked.connect(self.go_to_automation.emit)

        self.gridLayout_3.addWidget(self.widget_2, 4, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setStyleSheet("font: 700 15pt; \n"
"color:#F1FADA;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("font: 15pt; \n"
"color:rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.gridLayout_3.addWidget(self.widget_3, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 5, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 4, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 3, 0, 1, 1)

        # Add matplotlib canvas here
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.fig)
        self.axes = self.fig.add_subplot(111)

        self.gridLayout_3.addWidget(self.canvas, 2, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update_patient_name(self,patient_name):
        self.label_3.setText(patient_name)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Session"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "The session has not started yet"))
        self.pushButton_2.setText(_translate("MainWindow", "Record"))
        self.label_2.setText(_translate("MainWindow", "Patient Name:"))
        self.label_3.setText(_translate("MainWindow", "Name"))

class LSLViewer():

    def __init__(self, stream, fig, axes, window, scale, dejitter=True):
        """Init"""
        self.stream = stream
        self.window = window
        self.scale = scale
        self.dejitter = dejitter
        self.inlet = StreamInlet(stream, max_chunklen=12)
        self.filt = True

        info = self.inlet.info()
        description = info.desc()

        self.sfreq = info.nominal_srate()
        self.n_samples = int(self.sfreq * self.window)
        self.n_chan = info.channel_count()

        ch = description.child('channels').first_child()
        ch_names = [ch.child_value('label')]

        for i in range(self.n_chan):
            ch = ch.next_sibling()
            ch_names.append(ch.child_value('label'))

        self.ch_names = ch_names

        fig.canvas.mpl_connect('key_press_event', self.OnKeypress)
        fig.canvas.mpl_connect('button_press_event', self.onclick)

        self.fig = fig
        self.axes = axes

        sns.despine(left=True)

        self.data = np.zeros((self.n_samples, self.n_chan))
        self.times = np.arange(-self.window, 0, 1./self.sfreq)
        impedances = np.std(self.data, axis=0)
        lines = []

        for ii in range(self.n_chan):
            line, = axes.plot(self.times[::2],
                              self.data[::2, ii] - ii, lw=1)
            lines.append(line)
        self.lines = lines

        axes.set_ylim(-self.n_chan + 0.5, 0.5)
        ticks = np.arange(0, -self.n_chan, -1)

        axes.set_xlabel('Time (s)')
        axes.xaxis.grid(False)
        axes.set_yticks(ticks)

        ticks_labels = ['%s - %.1f' % (ch_names[ii], impedances[ii])
                        for ii in range(self.n_chan)]
        axes.set_yticklabels(ticks_labels)

        self.display_every = int(0.2 / (12/self.sfreq))

        self.bf = firwin(32, np.array([1, 40])/(self.sfreq/2.), width=0.05,
                         pass_zero=False)
        self.af = [1.0]

        zi = lfilter_zi(self.bf, self.af)
        self.filt_state = np.tile(zi, (self.n_chan, 1)).transpose()
        self.data_f = np.zeros((self.n_samples, self.n_chan))

    def update_plot(self):
        k = 0
        while self.started:
            samples, timestamps = self.inlet.pull_chunk(timeout=1.0,
                                                        max_samples=12)
            if timestamps:
                if self.dejitter:
                    timestamps = np.float64(np.arange(len(timestamps)))
                    timestamps /= self.sfreq
                    timestamps += self.times[-1] + 1./self.sfreq
                self.times = np.concatenate([self.times, timestamps])
                self.n_samples = int(self.sfreq * self.window)
                self.times = self.times[-self.n_samples:]
                self.data = np.vstack([self.data, samples])
                self.data = self.data[-(self.n_samples):]
                filt_samples, self.filt_state = lfilter(
                    self.bf, self.af,
                    samples,
                    axis=0, zi=self.filt_state)
                self.data_f = np.vstack([self.data_f, filt_samples])
                self.data_f = self.data_f[-self.n_samples:]
                k += 1
                if k == self.display_every:

                    if self.filt:
                        plot_data = self.data_f
                    elif not self.filt:
                        plot_data = self.data - self.data.mean(axis=0)
                    for ii in range(self.n_chan):
                        self.lines[ii].set_xdata(self.times[::2] -
                                                 self.times[-1])
                        self.lines[ii].set_ydata(plot_data[::2, ii] /
                                                 self.scale - ii)
                        impedances = np.std(plot_data, axis=0)

                    ticks_labels = ['%s - %.2f' % (self.ch_names[ii],
                                                   impedances[ii])
                                    for ii in range(self.n_chan)]
                    self.axes.set_yticklabels(ticks_labels)
                    self.axes.set_xlim(-self.window, 0)
                    self.fig.canvas.draw()
                    k = 0
            else:
                sleep(0.2)

    def onclick(self, event):
        print((event.button, event.x, event.y, event.xdata, event.ydata))

    def OnKeypress(self, event):
        if event.key == '/':
            self.scale *= 1.2
        elif event.key == '*':
            self.scale /= 1.2
        elif event.key == '+':
            self.window += 1
        elif event.key == '-':
            if self.window > 1:
                self.window -= 1
        elif event.key == 'd':
            self.filt = not(self.filt)

    def start(self):
        self.started = True
        self.thread = Thread(target=self.update_plot)
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        self.started = False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Setting up the LSLViewer
    streams = resolve_stream('type', 'EEG')
    if len(streams) == 0:
        raise(RuntimeError("Can't find EEG stream"))
    # lslv = LSLViewer(streams[0], ui.fig, ui.axes, window=5, scale=891)
    lslv = LSLViewer(streams[0], ui.fig, ui.axes, window=5, scale=57)
    
    # Start the LSLViewer
    lslv.start()

    MainWindow.show()
    sys.exit(app.exec_())

    # Stop the LSLViewer
    lslv.stop()
