#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from enum import Enum

token = "urtoken"
db_file = "database.vdb"


class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_ENTER_POS = "1"
    S_ENTER_MOVE = "2"
    S_ENTER_SHOOT = "3"

