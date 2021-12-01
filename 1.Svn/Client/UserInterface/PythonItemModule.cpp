//Find
void initItem()

///Add Above
#if defined(__BL_CHEST_DROP_INFO__)
#include "../EterBase/grid.h"

PyObject* itemHasDropInfo(PyObject* poSelf, PyObject* poArgs)
{
	int iItemIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iItemIndex))
		return Py_BadArgument();
	
	CItemData* pItemData;
	if (!CItemManager::Instance().GetItemDataPointer(iItemIndex, &pItemData))
		return Py_BuildValue("b", false);

	switch (pItemData->GetType())
	{
	case CItemData::EItemType::ITEM_TYPE_GIFTBOX:
	case CItemData::EItemType::ITEM_TYPE_TREASURE_BOX:
		break;
	default:
		return Py_BuildValue("b", false);
	}
	
	const CItemManager::TChestDropItemInfoVec* vDropInfo = CItemManager::Instance().GetItemDropInfoVec(iItemIndex);
	const bool bHasInfo = (vDropInfo != nullptr && (vDropInfo->empty() == false));

	return Py_BuildValue("b", bHasInfo);
}

PyObject* itemGetDropInfo(PyObject* poSelf, PyObject* poArgs)
{
	int iItemIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iItemIndex))
		return Py_BadArgument();

	PyObject* poList = PyList_New(0);
	uint8_t pageCount(0);

	const CItemManager::TChestDropItemInfoVec* vDropInfo = CItemManager::Instance().GetItemDropInfoVec(iItemIndex);
	if (vDropInfo != nullptr && vDropInfo->empty() == false)
	{
		CGrid m_Grid(5, 8);

		for (CItemManager::TChestDropItemInfoVec::const_iterator it = vDropInfo->begin(); it != vDropInfo->end(); ++it)
		{
			const DWORD dwDropVnum = *it;

			CItemData* pItemData;
			if (!CItemManager::Instance().GetItemDataPointer(dwDropVnum, &pItemData))
				continue;

			const BYTE bItemSize = pItemData->GetSize();

			while (true)
			{
				const int iPos = m_Grid.FindBlank(1, bItemSize);

				if (iPos >= 0)
				{
					m_Grid.Put(iPos, 1, bItemSize);
					PyList_Append(poList, Py_BuildValue("iii", pageCount, iPos, dwDropVnum));
					break;
				}
				else
				{
					m_Grid.Clear();
					++pageCount;
				}
			}
		}
	}

	return Py_BuildValue("iO", pageCount, poList);
}
#endif

//Find
		{ "LoadItemTable",					itemLoadItemTable,						METH_VARARGS },

///Add
#if defined(__BL_CHEST_DROP_INFO__)
		{ "HasDropInfo",					itemHasDropInfo,						METH_VARARGS },
		{ "GetDropInfo",					itemGetDropInfo,						METH_VARARGS },
#endif