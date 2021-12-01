#Find in def AddItemData(self, itemVnum, metinSlot, attrSlot = 0, flags = 0, unbindTime = 0):
#At end of the function
			elif item.LIMIT_TIMER_BASED_ON_WEAR == limitType:
				self.AppendTimerBasedOnWearLastTime(metinSlot)
				#dbg.TraceError("1) REAL_TIME flag On ")		
		
		self.ShowToolTip()

#Change
			elif item.LIMIT_TIMER_BASED_ON_WEAR == limitType:
				self.AppendTimerBasedOnWearLastTime(metinSlot)
				#dbg.TraceError("1) REAL_TIME flag On ")

		if app.__BL_CHEST_DROP_INFO__:
			self.AppendChestDropInfo(itemVnum)
		
		self.ShowToolTip()

#Find
	def __IsOldHair(self, itemVnum):
		return itemVnum > 73000 and itemVnum < 74000

#Add
	if app.__BL_CHEST_DROP_INFO__:
		def AppendChestDropInfo(self, itemVnum):
			hasinfo = item.HasDropInfo(itemVnum)
			if hasinfo:
				self.AppendSpace(5)
				#self.AppendTextLine("|Eemoji/key_ctrl|e + |Eemoji/key_x|e - Chest Drop Info", self.NORMAL_COLOR)
				self.AppendTextLine("[Chest Drop Info]", self.NORMAL_COLOR)