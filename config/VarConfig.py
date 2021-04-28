import os

ieDriverFilePaht = "IE路径暂时没有"
chromeDriverFilePath = "暂时不用"
firefoxDriverPath = "好像也不用"

# 获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 异常图片存放目录
screenPictureDir = parentDirPath + "\\exceptionpictures\\"

#测试数据文件存放绝对路径
dataFilePath = parentDirPath+"\\testData\\163邮箱创建联系人并发邮件.xlsx"

#测试数据文件中，测试用例表中的对应数字序号
testCase_testCaseName=1
testCase_frameWorkName=3
testCase_testStepSheetName=4
testCase_dataSourceSheetName=5
testCase_isExecute=6
testCase_runTime=7
testCase_testResult=8

#用例步骤表中，部分列对应的数字序号
testStep_testStepDescribe=1
testStep_keyWords=2
testStep_locationType=3
testStep_locatorExpression=4
testStep_operateValue=5
testStep_runTime=6
testStep_testReuslt=7
testStep_errorInfo=8
testStep_errorPic=9

#测试数据表中，是否执行列对应的数字编号
dataSource_isExecute=6
dataSource_email=2
dataSource_runTime=7
dataSource_result=8

