from testScripts.WriteTestResult import writeTestResult
from . import  *


def dataDriverFun(dataSourceSheetObj, stepSheetObj):
    try:
        # 获取数据表中是否执行列对象
        dataIsExecuteColumn= excelObj.getColumn(dataSourceSheetObj,dataSource_isExecute)
        # 获取数据源表中电子邮箱列对象
        emailColumn= excelObj.getColumn(dataSourceSheetObj,dataSource_email)
        # 获取测试步骤中存在数据区域的行数
        stepRowNums= excelObj.getRowsNumber(stepSheetObj)
        # 记录成功的数据条数
        successDatas=0
        # 记录被设置为执行的数据条数
        requiredDatas=0
        for idx,data in enumerate(dataIsExecuteColumn[1:]):
            # 遍历数据源表，准备进行数据驱动测试
            # 因为第一行是标题行，从第二行开始遍历
            if data=="y":
                print("开始添加联系人%s"%emailColumn[idx+1])
                requiredDatas+=1
                # 定义记录执行成功步骤数变量
                successStep=0
                for index in range(2,stepRowNums+1):
                    # 获取数据驱动测试步骤表中第index行
                    rowObj= excelObj.getRow(stepSheetObj, index)
                    # 获取关键字作为调用的函数名
                    keyWord= rowObj[testStep_keyWords-1]
                    # 获取定位类型
                    locationType= rowObj[testStep_locationType-1]
                    # 获取定位表达式
                    locatorExpression= rowObj[testStep_locatorExpression-1]
                    # 获取操作值
                    operateValue= rowObj[testStep_operateValue-1]
                    i=0
                    if not operateValue=="":
                        operateValue= str(operateValue)
                    if operateValue=="None":
                        operateValue=None
                    if operateValue and operateValue.isalpha():
                        # 如果operateValue变量不为空，说明有操作值，从数据表中根据坐标获取对应单元格的数据
                        coordinate= operateValue+str(idx+2)
                        print(coordinate,"!!!!!!!!!!!!!!!!!!!!!!!!!")
                        operateValue= excelObj.getCellOfValue(dataSourceSheetObj,coordinate=coordinate)
                    # 构造需要执行的python表达式，对应的Action动作
                    if not operateValue == "":
                        operateValue = str(operateValue)
                    tmpStr = "'%s','%s'" % (locationType.lower(), locatorExpression.replace("'",'"')) if locationType and locatorExpression else ""
                    if tmpStr:
                        tmpStr += ",u'" + operateValue + "'" if operateValue else ""
                    else:
                        tmpStr += "u'" + operateValue + "'" if operateValue else ""
                    runStr = keyWord + "(" + tmpStr + ")"
                    print(runStr)

                    try:
                        """
                        通过eval函数，将拼接的页面动作函数调用的字符串表示
                        当成有效的PYTHON表达式来执行，从而执行测试步骤的sheet
                        中关键字在ageActiongwen文件中对应的映射方法，来完成页面操作
                        """
                        if operateValue!="否":
                            eval(runStr)
                    # except Exception as e:
                    #     print("执行步骤%s发生异常"%rowObj[testStep_testStepDescribe-1])
                    #     print(traceback.print_exc())
                    # else:
                    #     successStep+=1
                    #     print("执行步骤%s成功"%rowObj[testStep_testStepDescribe-1])
                    except Exception as e:
                        print("执行步骤‘%s’发生异常!!!!!!!!!!!!!!!!!!!!!!" % rowObj[testStep_testStepDescribe - 1])
                        capturePic = capture_screen()
                        errorInfo = traceback.format_exc()
                        writeTestResult(stepSheetObj, rowNo=index, colsNo="caseStep", testResult="faild",
                                        errorInfo=str(errorInfo), picPath=capturePic)
                    else:
                        successStep += 1
                        print("执行步骤‘%s’成功" % rowObj[testStep_testStepDescribe - 1])
                        writeTestResult(stepSheetObj, rowNo=index, colsNo="caseStep", testResult="pass")
                if stepRowNums==successStep+1:
                    successDatas+=1
                    # 如果说成功执行的步骤书等于表中的步骤数，说明第idx+2行的数据执行成功，写入通过信息
                    writeTestResult(sheetObj=dataSourceSheetObj,rowNo=idx+2,colsNo='dataSheet',testResult="pass")
                else:
                    writeTestResult(sheetObj=dataSourceSheetObj,rowNo=idx+2,colsNo='dataSheet',testResult="faild")
            else:
                # 将不需要执行的数据行的执行时间和执行结果单元格清空
                writeTestResult(sheetObj=dataSourceSheetObj, rowNo=idx + 2, colsNo='dataSheet', testResult="")
        if requiredDatas==successDatas:
            return 1
        return 0
    except Exception as e:
        raise e

