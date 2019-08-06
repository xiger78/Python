import sys
from PyQt5.QtWidgets import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.get_size()

    def initUI(self):
        self.setGeometry(300, 300, 350, 450)
        self.setWindowTitle('Main window')

        self.statusbar = self.statusBar()  # 상태바 만들기

        self.textedit = QTextEdit(self)
        self.label = QLabel(self)
        self.lineedit = QLineEdit(self)

        # self.label.setText("test...")
        self.label.resize(300, 20)  # width, heigt 만큼 크기 조절
        self.label.move(10, 10)  # x, y 로 디동하기

        self.lineedit.move(10, 40)
        self.lineedit.resize(300, 20)

        self.textedit.move(10, 70)
        self.textedit.resize(self.textedit.sizeHint())
        self.show()

    def get_size(self):
        rect = self.frameGeometry()  # 프로그램 창 크기??
        self.label.setText("x={0},y={1},width={2},height={3}".format(rect.x(), rect.y(), rect.width(), rect.height()))

        r = QDesktopWidget().availableGeometry()  # # 작업표시줄 제외한 화면크기 반환
        # r = QDesktopWidget().screenGeometry()  #  화면 해상도
        self.lineedit.setText("x={0},y={1},width={2},height={3}".format(r.x(), r.y(), r.width(), r.height()))

        self.textedit.setText("입력 text")  # 내용 입력
        txt = self.textedit.toPlainText()  # 내용글 얻어오기

        self.statusbar.showMessage(txt)  # 상태바에 출력


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
