from os import replace

import selenium
from scraping.scrapers.amazon_scraper import getAmazonInfo
from selenium.common.exceptions import NoSuchElementException

def getHowLongToBeatInfo(driver, url):
    driver.get(url)

    title = getProductTitle(driver)
    info = getProductInfo(driver)
    img = getProductImage(driver)
    times = getTimes(driver)

    product_info = {
        'ProductTitle': title,
        'ProductInfo': info,
        'ProductImg': img,
        'ProductSoloTime': times['Single-Player'],
        'ProductCoopTime': times['Co-Op'],
        'ProductVsTime': times['Vs.'],
        'ProductMainStoryTime': times['Main Story'],
        'ProductMainExtrasTime': times['Main + Extras'],
        'ProductCompletionist': times['Completionist'],
        'ProductAllStylesTime': times['All Styles'],
    }

    return product_info

def getProductTitle(driver):
    try:
        xpath = '//*[@id="global_site"]/div[1]/div[1]/div[1]/div[1]'
        title = driver.find_element_by_xpath(xpath).text
        return title
    except NoSuchElementException:
        return str(None)

def getProductImage(driver):
    try:
        xpath = '//*[@id="global_site"]/div[3]/div/div[1]/div[1]/img'
        img = driver.find_element_by_xpath(xpath).get_attribute('src')
        return img
    except NoSuchElementException:
        return str(None)

def getProductInfo(driver):
    info_list = driver.find_elements_by_class_name('profile_info')
    info_results = {}
    description = True

    for div in info_list:
        if description:
            all_text = div.get_attribute('textContent').strip()
            read_more = "...Read More"

            parent_text = all_text.replace(read_more, '')
            description = False
            info_results['description'] = parent_text
        else:
            title_list = div.find_elements_by_tag_name('strong')
            title_text = ''
            for title in title_list:
                title_text = title.get_attribute('textContent').strip().replace(":", "")

            all_text = div.get_attribute('textContent').strip()
            parent_text = all_text.replace(title_text+":", '').strip()

            info_results[title_text] = parent_text

    return info_results

def getTimes(driver):
    time_types = {'Single-Player': getProductSoloTime, 'Co-Op': getProductCoopTime, 'Vs.': getProductVsTime,
                'Main Story': getProductMainStoryTime, 'Main + Extras': getProductMainExtrasTime,
                'Completionist': getProductCompletionistTime, 'All Styles': getProductAllStylesTime}
    
    results = {'Single-Player': 'None', 'Co-Op': 'None', 'Vs.': 'None', 'Main Story': 'None',
                'Main + Extras': 'None', 'Completionist': 'None', 'All Styles': 'None'}
    
        
    try:
        title_list = driver.find_elements_by_xpath(f'//*[@id="global_site"]/div[2]/div/div[2]/div[1]/ul/li')

        for position in range(len(title_list)):
            xpath = f'//*[@id="global_site"]/div[2]/div/div[2]/div[1]/ul/li[{position+1}]/h5'
                
            title = driver.find_element_by_xpath(xpath).text
            time, time_type = time_types[title](driver, position+1, 2)
            if time != 'None':
                results[time_type] = time
    except NoSuchElementException:
        title_list = driver.find_elements_by_xpath(f'//*[@id="global_site"]/div[3]/div/div[2]/div[1]/ul/li')

        for position in range(len(title_list)):
            xpath = f'//*[@id="global_site"]/div[3]/div/div[2]/div[1]/ul/li[{position+1}]/h5'
                
            title = driver.find_element_by_xpath(xpath).text
            time, time_type = time_types[title](driver, position+1, 3)
            if time != 'None':
                results[time_type] = time

    return results
        

def getProductMainStoryTime(driver, position, index):
    time_type = 'Main Story'

    try:
        xpath = f'//*[@id="global_site"]/div[{index}]/div/div[2]/div[1]/ul/li[{position}]/div'
        time = driver.find_element_by_xpath(xpath).text
        return time, time_type
    except NoSuchElementException:
        return str(None), str(None)

def getProductMainExtrasTime(driver, position, index):
    time_type = 'Main + Extras'

    try:
        xpath = f'//*[@id="global_site"]/div[{index}]/div/div[2]/div[1]/ul/li[{position}]/div'
        time = driver.find_element_by_xpath(xpath).text
        return time, time_type
    except NoSuchElementException:
        return str(None), str(None)

def getProductCompletionistTime(driver, position, index):
    time_type = 'Completionist'

    try:
        xpath = f'//*[@id="global_site"]/div[{index}]/div/div[2]/div[1]/ul/li[{position}]/div'
        time = driver.find_element_by_xpath(xpath).text
        return time, time_type
    except NoSuchElementException:
        return str(None), str(None)

def getProductAllStylesTime(driver, position, index):
    time_type = 'All Styles'

    try:
        xpath = f'//*[@id="global_site"]/div[{index}]/div/div[2]/div[1]/ul/li[{position}]/div'
        time = driver.find_element_by_xpath(xpath).text
        return time, time_type
    except NoSuchElementException:
        return str(None), str(None)

def getProductSoloTime(driver, position, index):
    time_type = 'Single-Player'

    try:
        xpath = f'//*[@id="global_site"]/div[{index}]/div/div[2]/div[1]/ul/li[{position}]/div'
        time = driver.find_element_by_xpath(xpath).text
        return time, time_type
    except NoSuchElementException:
        return str(None), str(None)

def getProductCoopTime(driver, position, index):
    time_type = 'Co-Op'

    try:
        xpath = f'//*[@id="global_site"]/div[{index}]/div/div[2]/div[1]/ul/li[{position}]/div'
        time = driver.find_element_by_xpath(xpath).text
        return time, time_type
    except NoSuchElementException:
        return str(None), str(None)

def getProductVsTime(driver, position, index):
    time_type = 'Vs.'

    try:
        xpath = f'//*[@id="global_site"]/div[{index}]/div/div[2]/div[1]/ul/li[{position}]/div'
        time = driver.find_element_by_xpath(xpath).text
        return time, time_type
    except NoSuchElementException:
        return str(None), str(None)
