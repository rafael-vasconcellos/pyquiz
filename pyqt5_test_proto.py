import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QLabel
from PyQt5.QtCore import Qt

def styled_button(text, x, y, weight, callback):
    button = QPushButton(text)
    button.setFixedSize(x, y)
    button.setStyleSheet(f"font-weight: {weight};")
    button.clicked.connect(callback)
    return button

def title(text, size, weight):
    label = QLabel(text)
    label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet(f"font-size: {size}px; font-weight: {weight};")
    return label

def reset():
    # Implement your reset logic here
    pass

def main_screen(end=False):
    app = QApplication(sys.argv)
    main_widget = QWidget()

    if end:
        main_button = styled_button('Reiniciar', 150, 75, 'bold', reset)
    else:
        main_button = styled_button('Iniciar', 150, 75, 'bold', lambda: questions_screen.update(start=True))

    h1 = title('Pyquiz', 72, 'bold')
    button_container = QWidget()
    containerLayout = QHBoxLayout(button_container)
    containerLayout.setAlignment(Qt.AlignCenter)
    containerLayout.addWidget(main_button)
    spacer_between = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

    hLayout = QHBoxLayout(main_widget)
    hLayout.setAlignment(Qt.AlignCenter)
    vLayout = QVBoxLayout()
    vLayout.setAlignment(Qt.AlignCenter)
    vLayout.addItem(spacer_between)
    vLayout.addWidget(h1)

    if end:
        resultContainer = QWidget()
        resultContainer.setContentsMargins(0, 50, 0, 50)
        resultLayout = QVBoxLayout(resultContainer)
        resultLayout.setAlignment(Qt.AlignCenter)
        result = title(f'Resultado: {str(int((count/len(questions))*100))}%', 52, 'subtitle')
        resultLayout.addWidget(result)
        vLayout.addWidget(resultContainer)
    else:
        vLayout.addItem(spacer_between)

    vLayout.addWidget(button_container)
    vLayout.addItem(spacer_between)
    hLayout.addLayout(vLayout)

    main_widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main_screen()
