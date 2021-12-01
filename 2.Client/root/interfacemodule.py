#Add
if app.__BL_CHEST_DROP_INFO__:
	import uiChestDropInfo

#Find in def __init__(self):
		self.wndGuild = None

#Add
		if app.__BL_CHEST_DROP_INFO__:
			self.wndChestDropInfo = None

#Find
		self.wndChatLog = wndChatLog

#Add
		if app.__BL_CHEST_DROP_INFO__:
			self.wndChestDropInfo = uiChestDropInfo.ChestDropInfoWindow()

#Find
		if self.wndGameButton:
			self.wndGameButton.Destroy()

#Add
		if app.__BL_CHEST_DROP_INFO__:
			if self.wndChestDropInfo:
				del self.wndChestDropInfo

#Find
		if self.wndExpandedTaskBar:
			self.wndExpandedTaskBar.Hide()

#Add
		if app.__BL_CHEST_DROP_INFO__:
			if self.wndChestDropInfo:
				self.wndChestDropInfo.Hide()

#Find
	def BULID_ExitGuildArea(self, areaID):
		self.wndGameButton.HideBuildButton()

#Add
	if app.__BL_CHEST_DROP_INFO__:
		def OpenChestDropWindow(self, itemVnum):
			if self.wndChestDropInfo:
				self.wndChestDropInfo.Open(itemVnum)

#If you don't have interface(safebox):

#Find
		wndSafebox = uiSafebox.SafeboxWindow()

#Add
		wndSafebox.BindInterface(self)

#If you don't have interface(shop):

#Find
		self.dlgShop.LoadDialog()

#Add
		self.dlgShop.BindInterface(self)