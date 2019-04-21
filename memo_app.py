"""以下、メモアプリです"""

import wx


class MyApp(wx.Frame):
    """フレームをオーバーライドしたアプリクラス"""

    def __init__(self, *args, **kw):
        super(MyApp, self).__init__(*args, **kw)

        self.init_ui()

    def init_ui(self):
        """画面の初期設定"""
        self.SetTitle('MEMO')
        self.SetBackgroundColour((255, 255, 255))
        self.SetPosition((200, 100))
        self.SetSize((420, 320))
        self.Show()

        panel_ui = wx.Panel(self, -1, pos=(50, 50), size=(300, 200))

        self.label = wx.StaticText(panel_ui, -1, '', pos=(10, 10))

        self.box = wx.TextCtrl(panel_ui, -1, pos=(10, 50))

        btn = wx.Button(panel_ui, -1, 'yyy', pos=(10, 90))
        btn.Bind(wx.EVT_BUTTON, self.clicked)

    def clicked(self, event):
        """テキストボックスをクリックした際のアクション"""
        text = self.box.GetValue()
        self.label.SetLabel(text)

if __name__ == "__main__":
    APP = wx.App()
    MyApp(None)
    APP.MainLoop()
