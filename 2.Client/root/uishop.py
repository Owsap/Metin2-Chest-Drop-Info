#Find
	def UnselectItemSlot(self, selectedSlotPos):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return

#Add
		if app.__BL_CHEST_DROP_INFO__:
			if app.IsPressed(app.DIK_LCONTROL):
				itemIndex = shop.GetItemID(selectedSlotPos)
				if item.HasDropInfo(itemIndex) and self.interface:
					self.interface.OpenChestDropWindow(itemIndex)
				return

#If you don't have interface:

#Find in class ShopDialog(ui.ScriptWindow): / def __init__(self):
		self.itemBuyQuestionDialog = None

#Add
		self.interface = None

#Find
	def OverOutItem(self):
		if 0 != self.tooltipItem:
			self.tooltipItem.HideToolTip()

#Add
	def BindInterface(self, interface):
		from _weakref import proxy
		self.interface = proxy(interface)