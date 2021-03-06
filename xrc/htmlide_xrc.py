# This file was automatically generated by pywxrc.
# -*- coding: UTF-8 -*-

import wx
import wx.xrc as xrc

__res = None

def get_resources():
    """ This function provides access to the XML resources in this module."""
    global __res
    if __res == None:
        __init_resources()
    return __res




class xrcHtmlIde(wx.Frame):
#!XRCED:begin-block:xrcHtmlIde.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcHtmlIde.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "HtmlIde")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.html_src = xrc.XRCCTRL(self, "html_src")
        self.gui_go = xrc.XRCCTRL(self, "gui_go")
        self.html_window = xrc.XRCCTRL(self, "html_window")





# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    __res.Load('htmlide.xrc')
