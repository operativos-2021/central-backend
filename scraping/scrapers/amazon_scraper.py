from selenium.common.exceptions import NoSuchElementException

def getAmazonInfo(driver, url, disable_continue):
    driver.get(url)

    title = getAmazonProductTitle(driver)
    price = getAmazonProductPrice(driver)
    platform = getAmazonProductPlatform(driver)

    product_info = {
        'ProductTitle': title,
        'ProductPrice': price,
        'ProductPlatform': platform
    }

    return product_info

def getAmazonProductTitle(driver):
    try:
        title = driver.find_element_by_xpath('//*[@id="productTitle"]').text
        return title
    except NoSuchElementException:
        return str(None)

def getAmazonProductPrice(driver):
    # try:
    #     price = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
    #     return '$'+price[4:]
    # except NoSuchElementException:
    #     price = driver.find_element_by_xpath('//*[@id="priceblock_pospromoprice"]').text
    #     return '$'+price[4:]
    tries = 0
    while tries < 3:
        try:
            if tries == 0:
                price = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
                return '$'+price[4:]
            elif tries == 1:
                price = driver.find_element_by_xpath('//*[@id="priceblock_pospromoprice"]').text
                return '$'+price[4:]
            elif tries == 2:
                price = driver.find_element_by_xpath('//*[@id="olp_feature_div"]/div[2]/span/a/span[2]').text
                return '$'+price[4:]
        except NoSuchElementException:
            price = 'None'
        tries += 1
    return price

def getAmazonProductPlatform(driver):
    try:  
        platform = driver.find_element_by_xpath('//*[@id="platformInformation_feature_div"]').text
        return platform[13:]
    except NoSuchElementException:
        return str(None)