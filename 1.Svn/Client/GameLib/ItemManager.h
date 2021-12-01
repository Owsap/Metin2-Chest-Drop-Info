//Find
		CItemData *		MakeItemData(DWORD dwIndex);

///Add
#if defined(__BL_CHEST_DROP_INFO__)
		using							TChestDropItemInfoVec = std::vector<DWORD>;
		using							TChestDropItemInfoMap = std::unordered_map<DWORD, TChestDropItemInfoVec>;

		bool							LoadChestDropInfo(const char* c_szFileName);
		const TChestDropItemInfoVec* 	GetItemDropInfoVec(const DWORD dwVnum) const;
#endif

//Find
		CItemData * m_pSelectedItemData;

///Add
#if defined(__BL_CHEST_DROP_INFO__)
		TChestDropItemInfoMap m_ItemDropInfoMap;
#endif