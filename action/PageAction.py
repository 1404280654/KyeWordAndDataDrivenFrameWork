from selenium import webdriver
from config.VarConfig import *
from util.ObjiectMap import getElement
from util.ClipboardUtil import Clipboard
from util.KeyBoardUtil import KeyboardKeys
from util.DirAndTime import *
from util.WaitUtil import WaitUtil
from selenium.webdriver.chrome.options import Options

import time


# 定义driver全局变量
driver = None
# 全局的等待类实例对象
waitUtil = None

def open_browser(browserName, *arg):
    global driver, waitUtil
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path=ieDriverFilePaht)
        elif browserName.lower == 'chrome':
            chrome_option = Options()
            # 添加屏蔽，提示信息的设置参数项
            chrome_option.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            driver = webdriver.Chrome(executable_path=chromeDriverFilePath,chrome_options=chrome_option)
        else:
            driver = webdriver.Firefox()
        # 创建等待类实例
        waitUtil = WaitUtil(driver)
    except Exception as e:
        raise e

# 访问网页地址
def visit_url(url, *arg):
    global driver
    try:
        driver.get(url)
    except Exception as e:
        raise e

# 关闭浏览器
def close_browser(*arg):
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise e

# 强制等待
def sleep(sleepSeconds, *arg):
    try:
        if sleepSeconds.find(".") > 0:
            sleepvale,NONE=sleepSeconds.split(".")
            time.sleep(int(sleepvale))
        else:
            time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e

# 清空输入框
def clear(locationType, locatorExpression, *arg):
    global driver
    try:
        getElement(driver, locationType, locatorExpression).clear()
    except Exception as e:
        raise e

# 输入框输入内容
def input_string(loctionType, locatorExpression, inputContent):
    global driver
    try:
        # if not str(inputContent).find(".")==-1:
        #     inputContent0,NONE=(inputContent).split(".")
        #     if NONE.str.isdigit():
        #         getElement(driver, loctionType, locatorExpression).send_keys(inputContent0)
        #     else:
        #         getElement(driver, loctionType, locatorExpression).send_keys(inputContent)
        # else:
        #     getElement(driver, loctionType, locatorExpression).send_keys(inputContent)
        if str(inputContent).find(".") > 0:
            inputContent0, NONE = str(inputContent).split(".")
            if NONE.isdigit():
                getElement(driver, loctionType, locatorExpression).send_keys(inputContent0)
            else:
                getElement(driver, loctionType, locatorExpression).send_keys(inputContent)
        else:
            getElement(driver, loctionType, locatorExpression).send_keys(inputContent)
    except Exception as e:
        raise e

# 单机页面元素
def click(loctionType, locatorExpression, *arg):
    global driver
    try:
        getElement(driver, loctionType, locatorExpression).click()
    except Exception as e:
        raise e

# 断言页面源码是否存在关键字
def assert_string_in_pagesource(assertString, *arg):
    global driver
    try:
        assert assertString in driver.page_source,"%s not found in page source"%assertString
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e

# 断言页面标题是否存在给定的关键字
def assert_title(titleStr, *args):
    global driver
    try:
        assert titleStr in driver.title,"%s not found in page source"%titleStr
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e

# 获取页面标题
def getTitle(*arg):
    global driver
    try:
        return driver.title
    except Exception as e:
        raise e

# 获取页面源码
def getPageSource(*arg):
    global driver
    try:
        return driver.page_source
    except Exception as e:
        raise e

# 切换入口frame
def switch_to_frame(locationType, framelcoatorExpression, *arg):
    global driver
    try:
        driver.switch_to.frame(getElement(driver, locationType, framelcoatorExpression))
    except Exception as e:
        print("frame error")
        raise e

# 切入frame回到默认框中
def switch_to_default_content(*arg):
    global driver
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e

# 模拟Ctrl+v操作
def paste_string(pasteString, *arg):
    try:
        Clipboard.setText(pasteString)
        time.sleep(1)
        KeyboardKeys.twoKeys("ctrl","v")
    except Exception as e:
        raise e

# 模拟Tab操作
def press_tab_key(*arg):
    try:
        KeyboardKeys.oneKey("tab")
    except Exception as e:
        raise e

# 模拟Enter操作
def press_enter_key(*arg):
    try:
        KeyboardKeys.oneKey("enter")
    except Exception as e:
        raise e

# 窗口最大化
def maximize_browser():
    global driver
    try:
        driver.maximize_window()
    except Exception as e:
        raise e

# 截取屏幕图片
def capture_screen(*args):
    global driver
    currTime = getCurrentTime()
    picNmaeAndPath = str(createCurrentDateDir())+"\\"+str(currTime)+".png"
    try:
        # 截取的图片保存在指定文件中
        driver.get_screenshot_as_file(picNmaeAndPath.replace('\\', r'\\'))
    except Exception as e:
        raise e
    else:
        return picNmaeAndPath

# 显示等待页面元素出现在DOM中，但不一定可见，存在则返该元素页面对象
def waitPresenceOfElementLocated(locationType, locatorExpression, *arg):
    global waitUtil
    try:
        waitUtil.presenceOfElementLocated(locationType, locatorExpression)
    except Exception as e:
        raise e

# 检查frame是否存在，存在则切换进frame中
def waitFrameToBeAvailableAndSwitchToIt(locationType, locatorExpression, *args):
    global waitUtil
    try:
        waitUtil.frameToAvailableAndSwtichToIt(locationType, locatorExpression)
    except Exception as e:
        raise e

# 显示等待页面元素出现在DOM中，且一定存在，返回该页面元素对象
def waitVisibilityOfElementLocated(locationType, locatorExpression, *args):
    global waitUtil
    try:
        waitUtil.visibilityOfElementLocated(locationType, locatorExpression)
    except Exception as e:
        raise e







