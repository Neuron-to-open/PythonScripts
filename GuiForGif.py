# /****************************************************************************
# * Author: Neuron-to-open
# * Date: 2024/7/21
# * Python : 3.11
# * 系统版本： Windows 11 家庭版 20H2
# * IDE: Pycharm
# * 编程语言: Python
# * =========== ====== ===== ==============================================
# * @Copyright (C) Yijiayi All Rights reserved
# *****************************************************************************/
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QLineEdit
from moviepy.editor import VideoFileClip


class MP4ToGIFConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MP4 to GIF Converter')

        layout = QVBoxLayout()

        self.label = QLabel('Select MP4 file:')
        layout.addWidget(self.label)

        self.button = QPushButton('Browse')
        self.button.clicked.connect(self.openFileDialog)
        layout.addWidget(self.button)

        self.output_label = QLabel('Output GIF filename:')
        layout.addWidget(self.output_label)

        self.output_filename = QLineEdit(self)
        self.output_filename.setPlaceholderText('Enter output filename without extension')
        layout.addWidget(self.output_filename)

        self.convert_button = QPushButton('Convert to GIF')
        self.convert_button.clicked.connect(self.convertToGIF)
        layout.addWidget(self.convert_button)

        self.setLayout(layout)

    def openFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "MP4 Files (*.mp4);;All Files (*)", options=options)
        if fileName:
            self.label.setText(f'Selected: {fileName}')
            self.selected_file = fileName

    def convertToGIF(self):
        if hasattr(self, 'selected_file') and self.output_filename.text():
            mp4_file = self.selected_file
            gif_file = self.output_filename.text() + '.gif'

            clip = VideoFileClip(mp4_file)
            clip.write_gif(gif_file)

            self.label.setText(f'GIF saved as: {gif_file}')
        else:
            self.label.setText('Please select an MP4 file and enter an output filename.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MP4ToGIFConverter()
    ex.show()
    sys.exit(app.exec_())
