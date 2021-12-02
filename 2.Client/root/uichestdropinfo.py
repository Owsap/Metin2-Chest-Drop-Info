# Author: blackdragonx61
# Date: 28.11.21

import ui
import item
import uiToolTip

class ChestDropInfoWindow(ui.ScriptWindow):
	DROP_SLOT_SIZE = 5 * 8

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.IsLoaded = False

		self.ItemVnum = -1
		self.PageCount = 0
		self.ScrollPos = 0

		self.DropDict = dict()
		self.MainItemSlot = None
		self.DropItemSlot = None
		self.ScrollBar = None

		self.ToolTipItem = uiToolTip.ItemToolTip()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		self.ScrollPos = 0

		self.DropDict = None
		self.MainItemSlot = None
		self.DropItemSlot = None
		self.ScrollBar = None

		self.ToolTipItem = None

	def __LoadWindow(self):
		if self.IsLoaded:
			return

		self.IsLoaded = True

		# Script
		try:
			self.__LoadScript("UIScript/ChestDropInfoWindow.py")
		except:
			import exception
			exception.Abort("ChestDropInfoWindow.__LoadWindow.__LoadScript")

		# Object
		try:
			self.__BindObject()
		except:
			import exception
			exception.Abort("ChestDropInfoWindow.__LoadWindow.__BindObject")

		# Event
		try:
			self.__BindEvent()
		except:
			import exception
			exception.Abort("ChestDropInfoWindow.__LoadWindow.__BindEvent")

	def __LoadScript(self, fileName):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, fileName)

	def __BindObject(self):
		self.MainItemSlot = self.GetChild("main_item_slot")
		self.DropItemSlot = self.GetChild("drop_item_slot")
		self.ScrollBar = self.GetChild("scroll_bar")

	def __BindEvent(self):
		self.GetChild("board").SetCloseEvent(ui.__mem_func__(self.Close))

		self.MainItemSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInMainItemSlot))
		self.MainItemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		self.DropItemSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInDropItemSlot))
		self.DropItemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		self.ScrollBar.SetMiddleBarSize(0.5)
		self.ScrollBar.SetScrollEvent(self.OnScroll)

	def UpdateItems(self):
		for i in range(ChestDropInfoWindow.DROP_SLOT_SIZE):
			self.DropItemSlot.ClearSlot(i)

		if self.ScrollPos in self.DropDict:
			for pos in self.DropDict[self.ScrollPos]:
					self.DropItemSlot.SetItemSlot(pos, self.DropDict[self.ScrollPos][pos])

		self.DropItemSlot.RefreshSlot()

	def SetUp(self, itemVnum):
		self.ItemVnum = itemVnum
		self.MainItemSlot.SetItemSlot(0, self.ItemVnum, 0)
		self.MainItemSlot.RefreshSlot()

		(self.PageCount, DropList) = item.GetDropInfo(self.ItemVnum)

		self.DropDict.clear()
		for i in range(self.PageCount + 1):
			self.DropDict[i] = dict()

		for page, pos, vnum in DropList:
			self.DropDict[page][pos] = vnum

		self.ScrollPos = 0
		if self.PageCount > 0:
			self.ScrollBar.Show()
			self.DropItemSlot.SetPosition(20, 90)
		else:
			self.DropItemSlot.SetPosition(20 + 10, 90)
			self.ScrollBar.Hide()

		self.UpdateItems()

	def Open(self, itemVnum = 50254):
		if self.IsShow():
			return

		self.__LoadWindow()
		self.SetUp(itemVnum)

		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def OverInMainItemSlot(self, slotIndex):
		if self.ToolTipItem:
			self.ToolTipItem.SetItemToolTip(self.ItemVnum)

	def OverInDropItemSlot(self, slotIndex):
		if self.ToolTipItem:
			if self.ScrollPos in self.DropDict:
				if slotIndex in self.DropDict[self.ScrollPos]:
					self.ToolTipItem.SetItemToolTip(self.DropDict[self.ScrollPos][slotIndex])

	def OverOutItem(self):
		if self.ToolTipItem:
			self.ToolTipItem.HideToolTip()
			self.ToolTipItem.ClearToolTip()

	def Close(self):
		self.OverOutItem()
		self.Hide()

	def OnScroll(self):
		self.ScrollPos = int(self.PageCount * self.ScrollBar.GetPos())
		self.UpdateItems()

	def OnRunMouseWheel(self, pos):
		if self.ScrollBar.IsShow():
			if pos > 0:
				self.ScrollBar.OnUp()
			else:
				self.ScrollBar.OnDown()

	def OnPressEscapeKey(self):
		self.Close()
		return True
