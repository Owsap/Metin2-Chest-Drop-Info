#Add
if app.__BL_CHEST_DROP_INFO__:
	import item

#Find in class SafeboxWindow(ui.ScriptWindow):
	def UseItemSlot(self, slotIndex):
		mouseModule.mouseController.DeattachObject()

#Add
		if app.__BL_CHEST_DROP_INFO__:
			if app.IsPressed(app.DIK_LCONTROL):
				itemVnum = safebox.GetItemID(slotIndex)
				if item.HasDropInfo(itemVnum) and self.interface:
					self.interface.OpenChestDropWindow(itemVnum)
				return

#Find in class MallWindow(ui.ScriptWindow):
	def UseItemSlot(self, slotIndex):
		mouseModule.mouseController.DeattachObject()

#Add
		if app.__BL_CHEST_DROP_INFO__:
			if app.IsPressed(app.DIK_LCONTROL):
				itemVnum = safebox.GetMallItemID(slotIndex)
				if item.HasDropInfo(itemVnum) and self.interface:
					self.interface.OpenChestDropWindow(itemVnum)
				return

#If you don't have interface:

#Find in class SafeboxWindow(ui.ScriptWindow): / def __init__(self):
		self.ySafeBoxStart = 0

#Add
		self.interface = None

#Find in same class
	def OnPressEscapeKey(self):
		self.Close()
		return True

#Add
	def BindInterface(self, interface):
		from _weakref import proxy
		self.interface = proxy(interface)

#Find in class MallWindow(ui.ScriptWindow): / def __init__(self):
		self.ySafeBoxStart = 0

#Add
		self.interface = None

#Find in same class
	def OnPressEscapeKey(self):
		self.Close()
		return True

#Add
	def BindInterface(self, interface):
		from _weakref import proxy
		self.interface = proxy(interface)