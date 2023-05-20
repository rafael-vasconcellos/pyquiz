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

def styled_button(text_label, x=700, y=100, callback=lambda: None, weight='normal'):
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
    button.clicked.connect(callback)
    return button

def title(text_label, size, color=text.title, weight='bold'):
    h1 = QLabel(text_label)
    h1.setStyleSheet(f"""
        font-size: {size}px;
        font-weight: {weight};
        color: {color};
    """)
    return h1

def displayText(layout, index, alternative):
    questions[current_question.index]['answered'] = 'correct' if alternative['label'] else 'wrong'
    for i in range(1, layout.count()):
        item = layout.itemAt(i)
        if 'widget' in dir(item):
            if isinstance(item.widget(), QLabel):
                widget = item.widget()
                layout.removeWidget(widget)
                widget.deleteLater()
    
    label = title(alternative['exp'], 20, text.subtitle, weight='normal')
    layout.insertWidget(index, label)


def nextQuestion():
    global current_question
    for indice in questions:
        if indice['answered'] is None:
            current_question = Question(indice)
            return True
    return False


def main_screen():
    main_widget = QWidget()
    h1 = title('Pyquiz', 72)
    main_button = styled_button('Iniciar', x=150, y=75, weight='bold', callback=questions_screen)
    button_container = QWidget()
    containerLayout = QHBoxLayout(button_container)
    containerLayout.setAlignment(Qt.AlignCenter)
    containerLayout.addWidget(main_button)
    spacer_between = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    

    hLayout = QHBoxLayout(main_widget)
    hLayout.setAlignment(Qt.AlignCenter)
    vLayout = QVBoxLayout()
    vLayout.setSpacing(0)
    vLayout.setContentsMargins(0, 0, 0, 0)
    vLayout.setAlignment(Qt.AlignCenter)
    vLayout.addItem(spacer_between) ; vLayout.addWidget(h1)
    vLayout.addItem(spacer_between) ; vLayout.addWidget(button_container)
    vLayout.addItem(spacer_between)
    hLayout.addLayout(vLayout)
    return main_widget


def questions_screen():
    main_widget = QWidget()
    main_widget.setContentsMargins(20, 0, 0, 0)
    hLayout = QHBoxLayout(main_widget)
    vLaylout = QVBoxLayout()
    vLaylout.setAlignment(Qt.AlignCenter)
    if nextQuestion():
        h1 = title(current_question.text, 52)
        button_altA = styled_button(current_question.altA['text'], callback=lambda: displayText(vLaylout, 4, current_question.altA))
        button_altB = styled_button(current_question.altB['text'], callback=lambda: displayText(vLaylout, 6, current_question.altB))
        button_altC = styled_button(current_question.altC['text'], callback=lambda: displayText(vLaylout, 8, current_question.altC))
        button_altD = styled_button(current_question.altD['text'], callback=lambda: displayText(vLaylout, 10, current_question.altD))

        vLaylout.addWidget(h1) ; vLaylout.addItem(QSpacerItem(20, 110, QSizePolicy.Minimum, QSizePolicy.Expanding))
        vLaylout.addWidget(button_altA) ; vLaylout.addSpacing(10)
        vLaylout.addWidget(button_altB) ; vLaylout.addSpacing(10)
        vLaylout.addWidget(button_altC) ; vLaylout.addSpacing(10)
        vLaylout.addWidget(button_altD) ; vLaylout.addSpacing(10)

        next_button = styled_button('Next', x=150, y=75, weight='bold', callback=questions_screen)
        rightContainer = QWidget()
        cLayout = QVBoxLayout(rightContainer)
        cLayout.setAlignment(Qt.AlignBottom)
        cLayout.addWidget(next_button)

        hLayout.addLayout(vLaylout)
        hLayout.addItem(QSpacerItem(450, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        hLayout.addWidget(rightContainer)
        body_layout.deleteLater()
        body_layout.addWidget(main_widget)


app = QApplication(sys.argv)
tela = QMainWindow()
body = QWidget()
body.resize(1000, 700)
body.setStyleSheet(f'background-color: {background.color}')
body_layout = QVBoxLayout(body)

body_layout.addWidget(main_screen())
body.show()
app.exec()

# o método show a ser usado necessariamente precisa ser o elemento pai, aqui o main_widget.show() é usado
# note que o main_widget não usa a variável tela como argumento, desta maneira "main_widget = QWidget(tela)"
# se assim o fosse, o "tela.show()" que precisaria ser usado