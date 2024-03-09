import sys
from PyQt6.QtWidgets import QApplication
from page1 import MainWindow  # Ensure this matches your file and class names
import qdarkstyle  # Corrected import statement for the installed package

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Apply the dark theme using QDarkStyle
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt6'))  # Corrected function call

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())
