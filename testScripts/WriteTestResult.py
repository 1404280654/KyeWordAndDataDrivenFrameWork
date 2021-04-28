from . import *

# 测试用例或则用例步骤执行结束后，向表中写入结果信息
def writeTestResult(sheetObj,rowNo,colsNo,testResult,errorInfo=None,picPath=None):
    # 测试通过结果信息为绿色，失败为红色
    colorDict={"pass":"green","faild":"red","":None}
    # 用来区分测试用例工作表和用力步骤工作表的时间和结果列，定义的数据字典
    closDict={
        "testCase":[testCase_runTime,testCase_testResult],
        "caseStep":[testStep_runTime,testStep_testReuslt],
        "dataSheet":[dataSource_runTime,dataSource_result]
    }
    try:
        # 在测试步骤sheet中写入测试结果
        #print("-------------------------------------------------------",colorDict[testResult])
        excelObj.writeCell(sheetObj,content=testResult, rowNo=rowNo, colsNo=closDict[colsNo][1], style=colorDict[testResult])
        if testResult == "":
            # 清空时间单元格
            excelObj.writeCell(sheetObj,content="", rowNo=rowNo, colsNo=closDict[colsNo][0])
        else:
            # 测试步骤sheet中，写入测试时间
            excelObj.writeCellCurrentTime(sheetObj, rowNo=rowNo, colsNo=closDict[colsNo][0])
        if errorInfo and picPath:
            # 测试步骤中sheet写入异常信息
            excelObj.writeCell(sheetObj,content=errorInfo, rowNo=rowNo, colsNo=testStep_errorInfo)
            # 测试步骤中写入异常截图
            excelObj.writeCell(sheetObj,content=picPath, rowNo=rowNo, colsNo=testStep_errorPic)
        else:
            if colsNo == "caseStep":
                # 在测试步骤中，清空异常信息单元格
                excelObj.writeCell(sheetObj,content="", rowNo=rowNo, colsNo=testStep_errorInfo)
                # 在测试步骤中，清空异常图片
                excelObj.writeCell(sheetObj,content="", rowNo=rowNo, colsNo=testStep_errorPic)
    except Exception as e:
        print("写excel时发生异常")
        print(traceback.print_exc())

