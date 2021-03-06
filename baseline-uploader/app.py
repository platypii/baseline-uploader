#!/usr/bin/env python

import baseline_auth
import wx
import wx.adv

TRAY_TOOLTIP = 'System Tray Demo'
TRAY_ICON = 'res/favicon.ico'


def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item


class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self):
        super(TaskBarIcon, self).__init__()
        self.set_icon(TRAY_ICON)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'Say Hello', self.on_hello)
        create_menu_item(menu, 'Sign In', self.on_signin)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def set_icon(self, path):
        self.SetIcon(wx.Icon(path), TRAY_TOOLTIP)

    def on_left_down(self, event):
        print('Tray icon was left-clicked.')

    def on_hello(self, event):
        print('Hello, world!')

    def on_signin(self, event):
        print('Signing in...')
        baseline_auth.startAuth()

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)


def main():
    app = wx.App(True)
    TaskBarIcon()
    app.MainLoop()


if __name__ == '__main__':
    main()