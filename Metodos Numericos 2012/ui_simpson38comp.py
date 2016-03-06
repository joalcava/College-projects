#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Wed Apr  2 15:47:10 2014

import wx
import simpson3_8Compuesto as s38c
# begin wxGlade: extracode
# end wxGlade


class simpson38comp(wx.Frame):
	def __init__(self, *args, **kwds):
		# begin wxGlade: simpson38comp.__init__
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		self.label_1 = wx.StaticText(self, -1, "Funcion")
		self.text_ctrl_1 = wx.TextCtrl(self, -1, "")
		self.label_2 = wx.StaticText(self, -1, "Limite Superior")
		self.text_ctrl_2 = wx.TextCtrl(self, -1, "")
		self.label_3 = wx.StaticText(self, -1, "Limite Inferior")
		self.text_ctrl_3 = wx.TextCtrl(self, -1, "")
		self.label_4 = wx.StaticText(self, -1, "Numero de intervalos")
		self.text_ctrl_4 = wx.TextCtrl(self, -1, "")
		self.button_1 = wx.Button(self, -1, "Fuck Yeah!")

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_BUTTON, self.call_simpson38comp, self.button_1)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: simpson38comp.__set_properties
		self.SetTitle("Simpson 3/8 Compuesto")
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: simpson38comp.__do_layout
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		sizer_2 = wx.BoxSizer(wx.VERTICAL)
		sizer_2.Add(self.label_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
		sizer_2.Add(self.text_ctrl_1, 0, wx.EXPAND, 0)
		sizer_2.Add(self.label_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
		sizer_2.Add(self.text_ctrl_2, 0, wx.EXPAND, 0)
		sizer_2.Add(self.label_3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
		sizer_2.Add(self.text_ctrl_3, 0, wx.EXPAND, 0)
		sizer_2.Add(self.label_4, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
		sizer_2.Add(self.text_ctrl_4, 0, wx.EXPAND, 0)
		sizer_2.Add(self.button_1, 0, wx.EXPAND, 0)
		sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
		self.SetSizer(sizer_1)
		sizer_1.Fit(self)
		self.Layout()
		# end wxGlade

	def call_simpson38comp(self, event):  # wxGlade: main.<event_handler>
		var = s38c.Simpson38Comp(str(self.text_ctrl_1.GetValue()),float(self.text_ctrl_3.GetValue()),float(self.text_ctrl_2.GetValue()),int(self.text_ctrl_4.GetValue()))
		var.graph()
		event.Skip()