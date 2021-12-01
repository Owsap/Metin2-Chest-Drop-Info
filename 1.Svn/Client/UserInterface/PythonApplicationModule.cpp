///Add
#if defined(__BL_CHEST_DROP_INFO__)
	PyModule_AddIntConstant(poModule, "__BL_CHEST_DROP_INFO__", true);
#else
	PyModule_AddIntConstant(poModule, "__BL_CHEST_DROP_INFO__", false);
#endif