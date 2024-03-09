from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
import os
import sys
from page2 import SecondWindow


class MainWindow(QMainWindow):
    """
    Main window class for the Stock Market Analysis application, 
    showcasing key insights and trends from 2018 to 2028.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Market Analysis")
        self.setGeometry(300, 300, 800, 600)  # Set initial size and position
        self.initUI()

    def initUI(self):
        """Initializes the main user interface components."""
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(centralWidget)

        # Title label
        title_label = QLabel("Stock Market Analysis", self)
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        gridLayout.addWidget(title_label, 0, 0, 1, -1, Qt.AlignmentFlag.AlignHCenter)

        # Stock image
        imagePath = os.path.join(os.path.expanduser('~'), 'Downloads', 'stocks_image.png')
        stock_image = QLabel(self)
        stock_image.setPixmap(QPixmap(imagePath))
        gridLayout.addWidget(stock_image, 1, 0, 1, -1, Qt.AlignmentFlag.AlignHCenter)

        # Key Insights and Trends label
        insights_label = QLabel("Key Insights and Trends", self)
        insights_label.setFont(QFont("Arial", 16, QFont.Weight.Medium))
        gridLayout.addWidget(insights_label, 2, 0, 1, -1)

        # Insights content
        insights_content = QLabel(
            "1. Elevate Your Wealth: Drive long-term growth through strategic stock selections.\n"
            "2. Mitigate Risk: Diversify your portfolio to navigate market volatility with confidence.\n"
            "3. Generate Income: Capitalize on dividends for a steady income stream alongside potential capital gains.",
            self
        )
        insights_content.setFont(QFont("Arial", 14))
        gridLayout.addWidget(insights_content, 3, 0, 1, -1)

        # Learn More button
        learn_more_button = QPushButton("Learn More", self)
        learn_more_button.clicked.connect(self.openSecondWindow)
        gridLayout.addWidget(learn_more_button, 4, 0, 1, -1, Qt.AlignmentFlag.AlignHCenter)

    def openSecondWindow(self):
        """Opens a secondary window with additional information."""
        self.secondWindow = SecondWindow()
        self.secondWindow.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
