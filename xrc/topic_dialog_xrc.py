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




class xrcTopicDialog(wx.Dialog):
#!XRCED:begin-block:xrcTopicDialog.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcTopicDialog.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreDialog()
        self.PreCreate(pre)
        get_resources().LoadOnDialog(pre, parent, "TopicDialog")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.description_text = xrc.XRCCTRL(self, "description_text")
        self.passage_list_ctrl = xrc.XRCCTRL(self, "passage_list_ctrl")
        self.passage_preview = xrc.XRCCTRL(self, "passage_preview")

        self.Bind(wx.EVT_CHAR, self.OnChar_passage_list_ctrl, self.passage_list_ctrl)

#!XRCED:begin-block:xrcTopicDialog.OnChar_passage_list_ctrl
    def OnChar_passage_list_ctrl(self, evt):
        # Replace with event handler code
        print "OnChar_passage_list_ctrl()"
#!XRCED:end-block:xrcTopicDialog.OnChar_passage_list_ctrl        




# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    __res.Load('topic_dialog.xrc')