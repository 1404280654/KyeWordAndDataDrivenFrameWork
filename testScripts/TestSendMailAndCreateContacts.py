from . import *
from testScripts import CreateContacts
from testScripts.WriteTestResult import writeTestResult

def TestSendMailAndCreateContacts():
    try:
        # 根据Excele中的sheet获取sheet对象
        caseSheet=excelObj.getSheetByName("测试用例")
        # 获取测试用例表中的sheet是否执行列的对象
        isExecuteColumn=excelObj.getColumn(caseSheet,testCase_isExecute)
        # 记录执行成功的测试用例个数
        successfulCase=0
        # 记录需要执行的用例个数
        requireCase=0
        for idx,i in enumerate(isExecuteColumn[1:]):
            # 第一列为标题，从第二列开始读取
            caseName= excelObj.getCellOfValue(caseSheet,rowNo=idx+2,colsNo=testCase_testCaseName)
            # 循环便利”测试用例“表中的测试用例，执行被设置为执行的用例
            if i=='y':
                requireCase+=1
                # 获取测试用例表中，第idx+1行中用例执行时所使用的框架
                useFrameWorkName=excelObj.getCellOfValue(caseSheet,rowNo=idx+2,colsNo=testCase_frameWorkName)
                # 获取测试用例表中，第idx+1行中用例执行时所使用的步骤Sheet名
                stepSheetName=excelObj.getCellOfValue(caseSheet, rowNo=idx + 2, colsNo=testCase_testStepSheetName)
                print("--------------------------",stepSheetName,"---------------------")
                if useFrameWorkName=="数据":
                    print("*************************调用数据驱动**************************")
                    dataSheetName=excelObj.getCellOfValue(caseSheet,rowNo=idx+2,colsNo=testCase_dataSourceSheetName)
                    # 获取第idx+1行测试用例步骤sheet对象
                    stepSheetObj=excelObj.getSheetByName(stepSheetName)
                    dataSheetObj=excelObj.getSheetByName(dataSheetName)
                    result= CreateContacts.dataDriverFun(dataSheetObj, stepSheetObj)
                    if result:
                        print("用例%s执行成功"%caseName)
                        successfulCase+=1
                        writeTestResult(caseSheet, rowNo=idx + 2,colsNo="testCase",testResult="pass")

                    else:
                        print("用例%s失败失败！！！！！！！！！！" % caseName)
                        writeTestResult(caseSheet, rowNo=idx + 2, colsNo="testCase", testResult="faild")
                elif useFrameWorkName=="关键字":
                    print("*************************调用关键字驱动**************************")
                    caseStepObj=excelObj.getSheetByName(stepSheetName)
                    stepNums=excelObj.getRowsNumber(caseStepObj)
                    successfulStep=0
                    print("到这里了1111111111111")
                    for index in range(2,stepNums+1):
                        stepRow= excelObj.getRow(caseStepObj,index)
                        keyWord= stepRow[testStep_keyWords-1]
                        locationType=stepRow[testStep_locationType-1]
                        locatorExpression=stepRow[testStep_locatorExpression-1]
                        operateValue= stepRow[testStep_operateValue-1]
                        #print(stepRow)
                        if not operateValue=="":
                            operateValue=str(operateValue)
                        if operateValue == "None":
                            operateValue = ""
                        tmpStr = "'%s','%s'" % (locationType.lower(), locatorExpression.replace("'",'"')) if locationType and locatorExpression else ""
                        if tmpStr:
                            tmpStr += ",u'" + operateValue + "'" if operateValue else ""
                        else:
                            tmpStr += "u'" + operateValue + "'" if operateValue else ""
                        runStr = keyWord + "(" + tmpStr + ")"
                        print(runStr)
                        try:
                            eval(runStr)
                        except Exception as e:
                            print("执行步骤‘%s’发生异常!!!!!!!!!!!!!!!!!!!!!!"%stepRow[testStep_testStepDescribe-1])
                            capturePic= capture_screen()
                            errorInfo= traceback.format_exc()
                            writeTestResult(caseStepObj,rowNo=index,colsNo="caseStep",testResult="faild",errorInfo=str(errorInfo),picPath=capturePic)
                        else:
                            successfulStep+=1
                            print("执行步骤‘%s’成功" % stepRow[testStep_testStepDescribe - 1])
                            writeTestResult(caseStepObj, rowNo=index, colsNo="caseStep", testResult="pass")
                    if successfulStep==stepNums-1:
                        successfulCase+=1
                        print("用例%s执行成功" % caseName)
                        writeTestResult(caseSheet, rowNo=idx + 2, colsNo="testCase", testResult="pass")
                    else:
                        print("用例%s失败失败！！！！！！！！！！" % caseName)
                        writeTestResult(caseSheet, rowNo=idx + 2, colsNo="testCase", testResult="faild")
            else:
                writeTestResult(caseSheet,rowNo=idx+2,colsNo="testCase",testResult="")
                pass
        print("全部执行完饿了-----------+++++++++++++++++*-************************************/////////////////---------")
    except Exception as e:
        print(traceback.print_exc())



