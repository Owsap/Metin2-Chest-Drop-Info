#Find
	def __UseItem(self, slotIndex):
		ItemVNum = player.GetItemIndex(slotIndex)
		item.SelectItem(ItemVNum)

#Add
		if app.__BL_CHEST_DROP_INFO__:
			if app.IsPressed(app.DIK_LCONTROL):
				if item.HasDropInfo(ItemVNum) and self.interface:
					self.interface.OpenChestDropWindow(ItemVNum)
				return