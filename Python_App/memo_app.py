import sys
from PySide2.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide2.QtGui import QIcon


# TrayWidgetクラスは、QSystemTrayIconを継承して作成
class TrayWidget(QSystemTrayIcon):
    def __init__(self, parent=None):
        QSystemTrayIcon.__init__(self, parent)

        # タスクトレイアイコン クリックメニュー登録
        menu = QMenu(parent)
        qt_action = menu.addAction("Qtちゃん")
        qt_action.triggered.connect(self.Message)
        menu.addSeparator()
        quit_action = menu.addAction("&Quit")
        quit_action.triggered.connect(self.Quit)

        # タスクトレイアイコン クリックメニュー設定
        self.setContextMenu(menu)

        # 初期アイコン設定
        self.setIcon(QIcon('QtChanBack.png'))


    # "Qtちゃん"メニューでメッセージ表示
    def Message(self):
        self.showMessage("ゆるキャラ", "Qtちゃんだよ", QIcon('QtChan.png'), 5000 );

    # "Quit"にて、タスクトレイアイコンアプリを閉じる
    def Quit(self):
        QApplication.quit()


def main():
    app = QApplication([])
    tray = TrayWidget()
    # タスクトレイに表示
    tray.show()

    ret = app.exec_()
    sys.exit(ret)


if __name__ == '__main__':
    main()