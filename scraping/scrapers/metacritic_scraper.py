from selenium.common.exceptions import NoSuchElementException

def getMetacriticInfo(driver, url):
    driver.get(url)

    title = getProductTitle(driver)
    platform = getProductPlatform(driver)
    metascore = getProductMetascore(driver)
    user_score = getProductUserScore(driver)

    product_info = {
        'ProductTitle': title,
        'ProductPlatform': platform,
        'ProductMetascore': metascore,
        'ProductUserScore': user_score
    }

    return product_info

def getProductTitle(driver):
    try:
        xpath = '//*[@id="main"]/div/div[1]/div[1]/div[1]/div[2]/a/h1'
        title = driver.find_element_by_xpath(xpath).text
        return title
    except NoSuchElementException:
        return str(None)

def getProductPlatform(driver):
    try:
        xpath = '//*[@id="main"]/div/div[1]/div[1]/div[1]/div[2]/span/a'
        platform = driver.find_element_by_xpath(xpath).text
        return platform
    except NoSuchElementException:
        return str(None)

def getProductMetascore(driver):
    try:
        xpath = '//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/div/div/a/div/span'
        metascore = driver.find_element_by_xpath(xpath).text
        return metascore
    except NoSuchElementException:
        return str(None)

def getProductUserScore(driver):
    try:
        xpath = '//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div[1]/div/a/div'
        user_score = driver.find_element_by_xpath(xpath).text
        return user_score
    except NoSuchElementException:
        return str(None)