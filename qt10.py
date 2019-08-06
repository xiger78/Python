#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QTextBrowser, QGridLayout
import requests
from bs4 import BeautifulSoup


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.le = QLineEdit()
        self.le.setPlaceholderText('yymmdd')
        self.le.returnPressed.connect(self.crawl_news)

        self.btn = QPushButton('Start')
        self.btn.clicked.connect(self.crawl_news)

        self.lbl = QLabel('날짜를 입력하세요.')

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        grid = QGridLayout()
        grid.addWidget(self.le, 0, 0, 1, 3)
        grid.addWidget(self.btn, 0, 3, 1, 1)
        grid.addWidget(self.lbl, 1, 0, 1, 4)
        grid.addWidget(self.tb, 2, 0, 1, 4)

        self.setLayout(grid)

        self.setWindowTitle('Web Crawler')
        self.setGeometry(100, 100, 450, 650)
        self.show()

    def crawl_news(self):
        date = self.le.text()

        if date:
            self.lbl.setText('[20' + str(date) + '] 많이 본 뉴스입니다.')
            self.tb.clear()
            url_news = 'https://news.naver.com'
            url = url_news + '/main/ranking/popularDay.nhn?rankingType=popular_day&date=20' + date
            r = requests.get(url)
            html = r.content
            soup = BeautifulSoup(html, 'html.parser')
            titles_html = soup.select('.ranking_section > ol > li > dl > dt > a')

            for i in range(len(titles_html)):
                title = titles_html[i].text
                link = url_news + titles_html[i].get('href')
                self.tb.append(str(i+1) + '. ' + title + ' (' + '<a href="' + link + '">링크</a>' + ')')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
