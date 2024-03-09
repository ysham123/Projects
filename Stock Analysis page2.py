from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QComboBox, QPushButton
import sys
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import yfinance as yf
import mplfinance as mpf

class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 800, 600)  # Adjusted for better visibility on standard screens
        self.setWindowTitle("Stock Data Visualization")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.comboBox = QComboBox(self)
        self.layout.addWidget(self.comboBox)
        self.comboBox.addItem("NVDA")
        self.comboBox.addItem("TSLA")
        self.comboBox.addItem("AMZN")
        self.comboBox.addItem("MRNA")
        self.comboBox.addItem("CRWD")

        self.comboBox.currentIndexChanged.connect(self.index_changed)

        self.figure = Figure(figsize=(10, 8), dpi=100)  # Adjusted for better visibility
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Back Button
        self.back_button = QPushButton("Back", self)
        self.layout.addWidget(self.back_button)
        self.back_button.clicked.connect(self.handle_back)

    def handle_back(self):
        self.close()  # Closes the current window, simulate going 'back'

    def index_changed(self, index):
        stock_symbol = self.comboBox.currentText()
        data = self.fetch_stock_data(stock_symbol)

        self.figure.clear()

        # Adjusting the subplot layout to better accommodate both plots
        ax1 = self.figure.add_subplot(211)  # Adjusted for stock price and moving averages
        ax2 = self.figure.add_subplot(212)  # Adjusted for volume, ensuring it doesn't overlap with ax1

        # Plot closing prices
        ax1.plot(data.index, data['Close'], label='Close Price', color='blue', linewidth=1.5)

        # Calculate and plot moving averages
        moving_average_30 = data['Close'].rolling(window=30).mean()
        moving_average_50 = data['Close'].rolling(window=50).mean()
        ax1.plot(data.index, moving_average_30, label='30-Day MA', color='red', linestyle='--')
        ax1.plot(data.index, moving_average_50, label='50-Day MA', color='green', linestyle='--')

        # Plot volume
        ax2.bar(data.index, data['Volume'], color='gray', width=2)

        # Improve graph aesthetics
        ax1.set_title(f"{stock_symbol} Stock Analysis", fontsize=14)
        ax1.set_ylabel("Price (USD)", fontsize=12)
        ax1.legend()
        ax1.grid(True)

        ax2.set_xlabel("Date", fontsize=12)
        ax2.set_ylabel("Volume", fontsize=12)
        ax2.grid(True)

        # Adjust layout to make sure everything fits without overlap
        self.figure.tight_layout()

        self.canvas.draw()

    def fetch_stock_data(self, symbol, period="1y", interval="1d"):
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period, interval=interval)
        return hist

if __name__ == "__main__":
    app = QApplication(sys.argv)
    second_window = SecondWindow()
    second_window.show()
    sys.exit(app.exec())
