#encoding=utf-8

from action.PageAction import *
from util.ParseExcel import ParseExcle
from config.VarConfig import *
import time
import traceback

excelObj = ParseExcle()
excelObj.loadWorkBook(dataFilePath)