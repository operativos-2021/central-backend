from selenium.common.exceptions import NoSuchElementException

def getAmazonInfo(driver, url, disable_continue):
    driver.get(url)
    if disable_continue:
        try:
            button = driver.find_element_by_xpath('/html/body/div[2]/header/div/div[4]/div[1]/div/div/div[3]/span[1]/span/input')
            button.click()
        except NoSuchElementException:
            print("No check")
        

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