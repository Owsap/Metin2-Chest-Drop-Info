//Find
	if (!rkItemMgr.LoadItemTable(szItemProto))
	{
		TraceError("LoadLocaleData - LoadItemProto(%s) Error", szItemProto);
		return false;
	}

///Add
#if defined(__BL_CHEST_DROP_INFO__)
	char szChestDrop[256];
	snprintf(szChestDrop, sizeof(szChestDrop), "%s/chest_drop", localePath);

	if (!rkItemMgr.LoadChestDropInfo(szChestDrop))
	{
		TraceError("LoadLocaleData - LoadChestDropInfo(%s) Error", szChestDrop);
		return false;
	}
#endif