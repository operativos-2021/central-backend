from selenium.common.exceptions import NoSuchElementException

def getNintendoInfo(driver, url):
    driver.get(url)

    title = getNintendoProductTitle(driver)
    price = getNintendoProductPrice(driver)
    sku = getNintendoProductSKU(driver)

    product_info = {
        'ProductTitle': title,
        'ProductPrice': price,
        'ProductSKU#': sku
    }

    return product_info

def getNintendoProductTitle(driver):
    try:
        xpath = '//*[@id="maincontent"]/div[3]/div/div[1]/div[1]/h1/span'
        title = driver.find_element_by_xpath(xpath).get_attribute('textContent')
        return title
    except NoSuchElementException:
        return str(None)

def getNintendoProductPrice(driver):
    try:
        xpath = '/html/body/div[2]/main/div[3]/div/div[1]/div[3]/div[1]/span/span/span[2]'
        price = driver.find_element_by_xpath(xpath).get_attribute('textContent')
        return price
    except NoSuchElementException:
        return str(None)

def getNintendoProductSKU(driver):
    try:
        xpath = '//*[@id="maincontent"]/div[3]/div/div[1]/div[2]/div'
        sku = driver.find_element_by_xpath(xpath).get_attribute('textContent')
        return sku
    except NoSuchElementException:
        return str(None)