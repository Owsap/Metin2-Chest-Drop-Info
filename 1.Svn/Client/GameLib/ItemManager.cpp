///Add
#if defined(__BL_CHEST_DROP_INFO__)
bool CItemManager::LoadChestDropInfo(const char* c_szFileName)
{
	if (m_ItemDropInfoMap.empty() == false)
		return true;

	CMappedFile file;
	LPCVOID pvData;

	if (!CEterPackManager::Instance().Get(file, c_szFileName, &pvData))
		return false;

	size_t mapSize = 0;
	file.Read(&mapSize, sizeof(mapSize));

	for (size_t i = 0; i < mapSize; i++)
	{
		DWORD dwItemVnum = 0;
		file.Read(&dwItemVnum, sizeof(dwItemVnum));

		size_t vecSize = 0;
		file.Read(&vecSize, sizeof(vecSize));
		
		TChestDropItemInfoVec& vecDrop = m_ItemDropInfoMap[dwItemVnum];
		for (size_t j = 0; j < vecSize; j++)
		{
			DWORD dwDropVnum = 0;
			file.Read(&dwDropVnum, sizeof(dwDropVnum));
			
			if (dwDropVnum != 0)
				vecDrop.push_back(dwDropVnum);
		}
		
		std::sort(vecDrop.begin(), vecDrop.end(), 
			[this](TChestDropItemInfoVec::value_type const a, TChestDropItemInfoVec::value_type const b)
		{
			CItemData* pItemData[2];
			if (GetItemDataPointer(a, &pItemData[0]) && GetItemDataPointer(b, &pItemData[1]))
				return pItemData[0]->GetSize() < pItemData[1]->GetSize();

			return false;
		});
	}

	return true;
}

const CItemManager::TChestDropItemInfoVec* CItemManager::GetItemDropInfoVec(const DWORD dwVnum) const
{
	TChestDropItemInfoMap::const_iterator it = m_ItemDropInfoMap.find(dwVnum);
	if (it != m_ItemDropInfoMap.end())
	{
		const TChestDropItemInfoVec* pVec = &(it->second);
		return pVec;
	}

	return nullptr;
}
#endif