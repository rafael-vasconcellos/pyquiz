import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from questions import *


text = lambda: None
text.title = '#94A3B8'
text.subtitle = '#A1A1AA'
text.button = '#38BDF8'
text.buttonRGB = 'rgba(56, 189, 248, .2)'

background = lambda: None
background.color = '#0F172A'

count = 0

def styled_button(text_label, x=700, y=100, callback= None, weight='normal'):
    button = QPushButton(text_label)
    button.setFixedSize(x, y)
    button.setCursor(Qt.PointingHandCursor)
    button.setStyleSheet(f"""
        border-radius: 30px;
        background-color: {text.buttonRGB};
        color: {text.button};
        font-size: 27px;
        font-weight: {weight};
    """)
    if callback:
        button.clicked.connect(callback)
    return button

def title(text_label, size, color=text.title, weight='normal'):
    h1 = QLabel(text_label)
    h1.setStyleSheet(f"""
        font-size: {size}px;
        font-weight: {weight};
        color: {color};
    """)
    return h1

def displayText(layout, index, alternative, next_button):
    global count
    if alternative['label']:
        questions[current_question.index]['answered'] = 'correct'
        count += 1
    else:
        questions[current_question.index]['answered'] = 'wrong'
    for i in range(1, layout.count()):
        item = layout.itemAt(i)
        if 'widget' in dir(item):
            widget = item.widget()
            if isinstance(widget, QLabel):
                    layout.removeWidget(widget)
                    widget.deleteLater()
            elif isinstance(widget, QPushButton):
                    widget.clicked.disconnect()
    
    label = title(alternative['exp'], 20, text.subtitle)
    layout.insertWidget(index, label)
    next_button.clicked.connect(questions_screen.update)


def nextQuestion():
    global current_question
    for indice in questions:
        if indice['answered'] is None:
            current_question = Question(indice)
            return True

    return False


def main_screen(end=False):
    main_widget = QWidget()
    if end:
        main_button = styled_button('Encerrar', x=150, y=75, weight='bold', callback=app.quit)
    else:
        main_button = styled_button('Iniciar', x=150, y=75, weight='bold', callback=questions_screen.update)

    h1 = title('Pyquiz', 72, weight='bold')
    button_container = QWidget()
    containerLayout = QHBoxLayout(button_container)
    containerLayout.setAlignment(Qt.AlignCenter)
    containerLayout.addWidget(main_button)
    spacer_between = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)


    hLayout = QHBoxLayout(main_widget)
    hLayout.setAlignment(Qt.AlignCenter)
    vLayout = QVBoxLayout()
    vLayout.setAlignment(Qt.AlignCenter)
    vLayout.addItem(spacer_between) ; vLayout.addWidget(h1)
    if end:
        resultContainer = QWidget()
        resultContainer.setContentsMargins(0, 50, 0, 50)
        resultLayout = QVBoxLayout(resultContainer)
        resultLayout.setAlignment(Qt.AlignCenter)
        result = title( f'Resultado: {str(int(  (count/len(questions))*100  ))}%', 
                        52, text.subtitle)
        resultLayout.addWidget(result)
        vLayout.addWidget(resultContainer)
    else:
        vLayout.addItem(spacer_between)
    vLayout.addWidget(button_container) ; vLayout.addItem(spacer_between)
    hLayout.addLayout(vLayout)
    return main_widget


class questionsScreen:
    def __init__(self):
        self._questions_widget = QWidget()
        self._questions_widget.setContentsMargins(20, 0, 0, 0)

        self.next_button = styled_button('Next', x=150, y=75, weight='bold', callback= lambda: None)
        self.h1 = title('', 52, weight='bold')
        self.altA = styled_button('')
        self.altB = styled_button('')
        self.altC = styled_button('')
        self.altD = styled_button('')

        hLayout = QHBoxLayout(self._questions_widget)
        vLaylout = QVBoxLayout() ; self.vLaylout = vLaylout
        vLaylout.setAlignment(Qt.AlignCenter)

        vLaylout.addWidget(self.h1) ; vLaylout.addItem(QSpacerItem(20, 110, QSizePolicy.Minimum, QSizePolicy.Expanding))
        vLaylout.addWidget(self.altA) ; vLaylout.addSpacing(10)
        vLaylout.addWidget(self.altB) ; vLaylout.addSpacing(10)
        vLaylout.addWidget(self.altC) ; vLaylout.addSpacing(10)
        vLaylout.addWidget(self.altD) ; vLaylout.addSpacing(10)

        rightContainer = QWidget()
        cLayout = QVBoxLayout(rightContainer)
        cLayout.setAlignment(Qt.AlignBottom)
        cLayout.addWidget(self.next_button)

        hLayout.addLayout(vLaylout)
        hLayout.addItem(QSpacerItem(80, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        hLayout.addWidget(rightContainer)

    def update(self):
        if nextQuestion():
                self.h1.setText(current_question.text)
                self.altA.setText(current_question.altA['text'])
                self.altA.clicked.connect( lambda: displayText(self.vLaylout, 4, current_question.altA, self.next_button) )
                self.altB.setText(current_question.altB['text'])
                self.altB.clicked.connect( lambda: displayText(self.vLaylout, 6, current_question.altB, self.next_button) )
                self.altC.setText(current_question.altC['text'])
                self.altC.clicked.connect( lambda: displayText(self.vLaylout, 8, current_question.altC, self.next_button) )
                self.altD.setText(current_question.altD['text'])
                self.altD.clicked.connect( lambda: displayText(self.vLaylout, 10, current_question.altD, self.next_button) )
                body_layout.addWidget(self._questions_widget)
        else:
                body_layout.addWidget(main_screen(end=True))

        for i in range(1, self.vLaylout.count()):
            if 'widget' in dir(self.vLaylout.itemAt(i)):
                widget = self.vLaylout.itemAt(i).widget()
                if isinstance(widget, QLabel):
                    self.vLaylout.removeWidget(widget)
                    widget.deleteLater()

        self.next_button.clicked.disconnect()
        body_layout.itemAt(body_layout.count()-2).widget().hide()


app = QApplication(sys.argv)
tela = QMainWindow()
body = QWidget()
body.resize(1000, 700)
body.setStyleSheet(f'background-color: {background.color}')
body_layout = QVBoxLayout(body)

questions_screen = questionsScreen()


body_layout.addWidget(main_screen())
body.show()
app.exec()
