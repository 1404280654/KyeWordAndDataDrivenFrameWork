from selenium.webdriver.support.ui import WebDriverWait

# 获取单个页面元素
def getElement(dirver, locationType, locatorExpression):
    try:
        element = WebDriverWait(dirver, 30).until(lambda x: x.find_element(by=locationType, value=locatorExpression))
        return element
    except Exception as e:
        raise e
# 获取多个相同的页面元素，已list返回
def getElements(driver, locationType, locatorExpression):
    try:
        element = WebDriverWait(driver, 30).until(lambda x: x.find_elements(by=locationType, value=locatorExpression))
        return element
    except Exception as e:
        raise e

if __name__  == "__main__":
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com/")
    searchBOX= getElement(driver, "id", "kw")
    print(searchBOX.tag_name)
    aList = getElements(driver, "tag name", "a")
    print(len(aList))
    driver.quit()