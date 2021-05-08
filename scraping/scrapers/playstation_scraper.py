from selenium.common.exceptions import NoSuchElementException

def getPlaystationInfo(driver, url):
    driver.get(url)

    title = getPlaystationProductTitle(driver)
    price = getPlaystationProductPrice(driver)
    platform = getPlaystationProductPlatform(driver)

    product_info = {
        'ProductTitle': title,
        'ProductPrice': price,
        'ProductPlatform': platform
    }

    return product_info

def getPlaystationProductTitle(driver):
    try:
        xpath = '//*[@id="main"]/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div/h1'
        title = driver.find_element_by_xpath(xpath).get_attribute('textContent')
        return title
    except NoSuchElementException:
        return str(None)

def getPlaystationProductPrice(driver):
    try:
        xpath = '//*[@id="main"]/div[2]/div[1]/div/div[1]/div/div[3]/div/div/div/label/div/span/span/span/span'
        price = driver.find_element_by_xpath(xpath).get_attribute('textContent')
        return price
    except NoSuchElementException:
        return str(None)

def getPlaystationProductPlatform(driver):
    try:
        xpath = '//*[@id="main"]/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div/div[2]/span'
        platform = driver.find_element_by_xpath(xpath).get_attribute('textContent')
        return platform
    except NoSuchElementException:
        return str(None)