from util.ObjiectMap import *
from util.KeyBoardUtil import KeyboardKeys
from util.ClipboardUtil import Clipboard
from util.WaitUtil import WaitUtil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from action.PageAction import *


def TestSendMailWithAttachment():
    open_browser("firefox")
    visit_url("http://mail.163.com")
    sleep(3)
    assert_string_in_pagesource("163网易")
    waitFrameToBeAvailableAndSwitchToIt("id", "x-URS-iframe")
    input_string("xpath", "//input[@name='email']", "13924451750")
    input_string("xpath", "//input[@name='password']", "kh13530152776")
    click("id", "dologin")
    print("登陆邮箱成功")
    sleep(5)
    switch_to_default_content()
    assert_title("网易邮箱")
    waitVisibilityOfElementLocated("xpath", "//div[text()='通讯录']")
    click("id", "_mail_tabitem_1_49text")
    sleep(1)
    click("xpath", "//span[text()='新建联系人']")
    input_string("xpath", "//a[@title='编辑详细姓名']/preceding-sibling::div/input", "lily")

if __name__=="__main__":
    TestSendMailWithAttachment()
