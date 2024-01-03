import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QListWidget, QStackedWidget
from PyQt6.QtCore import QTimer, Qt, QPoint
from PyQt6.QtGui import QPainter, QPen, QColor, QFont

class SpinningWheelWidget(QWidget):
    def __init__(self, movies):
        super().__init__()
        self.movies = movies
        self.angle = 0
        self.selected_movie = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.rotate_wheel)
        self.setFont(QFont('Arial', 12, QFont.Weight.Bold))
        self.hide()  # Initially hide the spinning wheel

    def start_spinning(self):
        self.selected_movie = None
        self.timer.start(50)  # Start the spinning
        self.show()

    def rotate_wheel(self):
        self.angle += 5  # Increase the angle to rotate
        if self.angle >= 360:
            self.angle -= 360
        self.update()  # Trigger the paint event

        # Stop condition and movie selection
        if random.random() < 0.05:  # Random stop condition
            self.timer.stop()
            self.select_movie()

    def select_movie(self):
        index = random.randint(0, len(self.movies) - 1)
        self.selected_movie = self.movies[index]
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        pen = QPen()
        pen.setWidth(4)
        pen.setColor(QColor(0, 0, 0))
        painter.setPen(pen)
        rect = self.rect()
        center = QPoint(rect.width() / 2, rect.height() / 2)
        radius = min(rect.width() / 2, rect.height() / 2) - 20
        painter.drawEllipse(center, radius, radius)

        # Display selected movie inside the wheel
        if self.selected_movie:
            painter.drawText(center, self.selected_movie)
        else:
            # Draw a rotating line to simulate spinning
            painter.drawLine(center.x(), center.y(), center.x(), center.y() - radius)
            painter.rotate(self.angle)


        # Display selected movie inside the wheel
        if self.selected_movie:
            painter.drawText(center, self.selected_movie)

class MovieApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movie Recommender")
        self.setGeometry(400, 400, 1200, 1000)

        # Stacked widget to manage multiple pages
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Initialize and add pages
        self.main_page = MainPage(self)
        self.second_page = SecondPage(self)
        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.second_page)

    def switch_to_page(self, page_index, category=None):
        if page_index == 1 and category:
            self.second_page.update_recommendations(category)
        self.stacked_widget.setCurrentIndex(page_index)

class MainPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.layout = QVBoxLayout(self)

        # Genre selection list
        self.listWidget = QListWidget()
        self.listWidget.currentItemChanged.connect(self.on_genre_select)
        self.layout.addWidget(self.listWidget)

        # Add genres to the list
        self.stored_info = {
    "Classic Hollywood": [
        "Citizen Kane (1941)", 
        "Casablanca (1942)", 
        "Gone with the Wind (1939)",
        "Sunset Boulevard (1950)", 
        "The Maltese Falcon (1941)"
    ],
    "Science Fiction": [
        "Blade Runner (1982)", 
        "2001: A Space Odyssey (1968)", 
        "Star Wars: A New Hope (1977)",
        "The Matrix (1999)", 
        "Alien (1979)",
        "Interstellar (2014)",
        "District 9 (2009)"
    ],
    "Action & Adventure(old)": [
        "Indiana Jones: Raiders of the Lost Ark (1981)", 
        "Die Hard (1988)", 
        "Mad Max: Fury Road (2015)"
    ],
    "Action & Adventure": [
        "The Dark Knight (2008)", 
        "Gladiator (2000)",
        "John Wick (2014)",
        "The Avengers (2012)"
    ],
    "Drama": [
        "The Godfather (1972)", 
        "Schindler's List (1993)", 
        "12 Angry Men (1957)",
        "Forrest Gump (1994)", 
        "Fight Club (1999)",
        "No Country for Old Men (2007)",
        "There Will Be Blood (2007)"
    ],
    "Comedy": [
        "Some Like It Hot (1959)", 
        "Monty Python and the Holy Grail (1975)", 
        "Annie Hall (1977)",
        "The Big Lebowski (1998)", 
        "Groundhog Day (1993)",
        "Superbad (2007)",
        "The Hangover (2009)"
    ],
    "Romance": [
        "Casablanca (1942)", 
        "Pride and Prejudice (2005)", 
        "Before Sunrise (1995)",
        "The Notebook (2004)", 
        "Titanic (1997)",
        "Eternal Sunshine of the Spotless Mind (2004)",
        "La La Land (2016)"
    ],
    "Horror": [
        "Psycho (1960)", 
        "The Shining (1980)", 
        "Get Out (2017)",
        "Halloween (1978)", 
        "The Exorcist (1973)",
        "The Conjuring (2013)",
        "Hereditary (2018)"
    ],
    "Animated": [
        "Toy Story (1995)", 
        "Spirited Away (2001)", 
        "The Lion King (1994)",
        "Finding Nemo (2003)", 
        "Up (2009)",
        "Inside Out (2015)",
        "Coco (2017)"
    ],
    "Musical": [
        "The Sound of Music (1965)", 
        "La La Land (2016)", 
        "Moulin Rouge! (2001)",
        "West Side Story (1961)", 
        "Chicago (2002)",
        "Hamilton (2020)",
        "The Greatest Showman (2017)"
    ],
    "Mystery & Thriller": [
        "Se7en (1995)", 
        "Inception (2010)", 
        "The Usual Suspects (1995)",
        "Fight Club (1999)", 
        "Memento (2000)",
        "Gone Girl (2014)",
        "Shutter Island (2010)"
    ],
    "Fantasy": [
        "The Lord of the Rings: The Fellowship of the Ring (2001)", 
        "Harry Potter and the Sorcerer's Stone (2001)", 
        "Pan's Labyrinth (2006)",
        "Avatar (2009)", 
        "Alice in Wonderland (2010)",
        "The Shape of Water (2017)",
        "Doctor Strange (2016)"
    ],
    "Biographical": [
        "Amadeus (1984)", 
        "A Beautiful Mind (2001)", 
        "The Wolf of Wall Street (2013)",
        "Lincoln (2012)", 
        "The King's Speech (2010)",
        "The Social Network (2010)",
        "Bohemian Rhapsody (2018)"
    ],
    "War":[
        "Saving Private Ryan (1998)", 
        "Apocalypse Now (1979)", 
        "Full Metal Jacket (1987)",
        "Platoon (1986)", 
        "The Hurt Locker (2008)",
        "Dunkirk (2017)",
    ]
        }

        for category in self.stored_info.keys():
            self.listWidget.addItem(category)

        # Button to get recommendations (initially disabled)
        self.button = QPushButton("Get Recommendations", self)
        self.button.clicked.connect(self.on_button_click)
        self.button.setEnabled(False)
        self.layout.addWidget(self.button)

    def on_genre_select(self, current, previous):
        if current is not None:
            self.button.setEnabled(True)

    def on_button_click(self):
        selected_category = self.listWidget.currentItem().text()
        self.parent.switch_to_page(1, selected_category)

class SecondPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.layout = QVBoxLayout(self)
        self.recommendation_label = QLabel("Spin the wheel for a movie recommendation!")
        self.recommendation_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.recommendation_label)
        self.back_button = QPushButton('Back to Main Page')
        self.back_button.clicked.connect(lambda: parent.switch_to_page(0))
        self.layout.addWidget(self.back_button)
        self.spinning_wheel = None

    def update_recommendations(self, category):
        movies = self.parent.main_page.stored_info.get(category, [])
        if not self.spinning_wheel:
            self.spinning_wheel = SpinningWheelWidget(movies)
            self.layout.addWidget(self.spinning_wheel)
        else:
            self.spinning_wheel.movies = movies
        self.spinning_wheel.start_spinning()

# Entry point of the application
def main():
    app = QApplication(sys.argv)
    main_window = MovieApp()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
