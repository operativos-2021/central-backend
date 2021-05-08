from selenium.common.exceptions import NoSuchElementException

def getHowLongToBeatInfo(driver, url):
    driver.get(url)

    title = getProductTitle(driver)
    platform = getProductPlatform(driver)
    times = getTimes(driver)
    print(times)

    product_info = {
        'ProductTitle': title,
        'ProductPlatform': platform,
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

def getProductPlatform(driver):
    try:
        xpath1 = '//*[@id="global_site"]/div[2]/div/div[2]/div[2]/div/div[4]'
        xpath2 = '//*[@id="global_site"]/div[2]/div/div[2]/div[2]/div/div[3]'
        platform = driver.find_element_by_xpath(xpath1).text
        if "Platforms:" in platform:
            return platform[11:]
        else:
            platform = driver.find_element_by_xpath(xpath2).text
        return platform[11:]
    except NoSuchElementException:
        return str(None)

def getTimes(driver):
    time_types = {'Single-Player': getProductSoloTime, 'Co-Op': getProductCoopTime, 'Vs.': getProductVsTime,
                'Main Story': getProductMainStoryTime, 'Main + Extras': getProductMainExtrasTime,
                'Completionist': getProductCompletionistTime, 'All Styles': getProductAllStylesTime}
    
    results = {'Single-Player': 'None', 'Co-Op': 'None', 'Vs.': 'None', 'Main Story': 'None',
                'Main + Extras': 'None', 'Completionist': 'None', 'All Styles': 'None'}

    title_list = driver.find_elements_by_xpath('//*[@id="global_site"]/div[2]/div/div[2]/div[1]/ul/li')
    print(len(title_list))

    for position in range(len(title_list)):
        xpath = f'//*[@id="global_site"]/div[2]/div/div[2]/div[1]/ul/li[{position+1}]/h5'
        title = driver.find_element_by_xpath(xpath).text
        time, time_type = time_types[title](driver, position+1)
        if time != 'None':
            results[time_type] = time

    return results
        

def getProductMainStoryTime(driver, position):
    time_type = 'Main Story'

    try:
        xpath = f'//*[@id="global_site"]/div[2]/div/div[2]/div[1]/ul/li[{position}]/div'
        time = driver.find_element_by_xpath(xpath).text
        return time, time_type
    except NoSuchElementException:
        return str(None)

def getProductMainExtrasTime(driver, position):
    time_type = 'Main + Extras'

    try:
        xpath = f'//*[@id="global_site"]/div[2]/div/div[2]/div[1]/ul/li[{position}]/div'
        time = driver.find_element_by_xpath(xpath).text
        return time, time_type
    except NoSuchElementException:
        return str(None)

def getProductCompletionistTime(driver, position):
    time_type = 'Completionist'

    try:
        xpath = f'//*[@id="global_site"]/div[2]/div/div[2]/div[1]/ul/li[{position}]/div'
        time = driver.find_element_by_xpath(xpath).text
        return time, time_type
    except NoSuchElementException:
        return str(None)

def getProductAllStylesTime(driver, position):
    time_type = 'All Styles'

    try:
        xpath = f'//*[@id="global_site"]/div[2]/div/div[2]/div[1]/ul/li[{position}]/div'
        time = driver.find_element_by_xpath(xpath).text
        return time, time_type
    except NoSuchElementException:
        return str(None)

def getProductSoloTime(driver, position):
    time_type = 'Single-Player'

    try:
        xpath = f'//*[@id="global_site"]/div[2]/div/div[2]/div[1]/ul/li[{position}]/div'
        time = driver.find_element_by_xpath(xpath).text
        return time, time_type
    except NoSuchElementException:
        return str(None)

def getProductCoopTime(driver, position):
    time_type = 'Co-Op'

    try:
        xpath = f'//*[@id="global_site"]/div[2]/div/div[2]/div[1]/ul/li[{position}]/div'
        time = driver.find_element_by_xpath(xpath).text
        return time, time_type
    except NoSuchElementException:
        return str(None)

def getProductVsTime(driver, position):
    time_type = 'Vs.'

    try:
        xpath = f'//*[@id="global_site"]/div[2]/div/div[2]/div[1]/ul/li[{position}]/div'
        time = driver.find_element_by_xpath(xpath).text
        return time, time_type
    except NoSuchElementException:
        return str(None)
