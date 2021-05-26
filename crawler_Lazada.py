from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
import pandas as pd 
import time
import csv
import re

binary = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
options = Options()
options.set_headless(headless=False)
options.binary = binary
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True #optional
driver = webdriver.Firefox(firefox_options=options, capabilities=cap, executable_path=r"C:\ProgramData\Anaconda3\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe")

catList = []
subcatList = []
subsubcatList = []
subsublinkList = []
driver.get("https://www.lazada.com.my/#")
categories = driver.find_elements_by_xpath(('//div[@class="lzd-site-nav-menu-dropdown"]//ul[@class="lzd-site-menu-root"]//li[@class="lzd-site-menu-root-item"]//a//span'))

#This part is to crawl all the sub sub category webpage link
i = 1
for cat in categories:
    subcatpath = '//div[@class="lzd-site-nav-menu-dropdown"]//ul[@class="lzd-site-menu-root"]//ul[@class="lzd-site-menu-sub Level_1_Category_No{0}"]//li[@class="lzd-site-menu-sub-item"]/a'.format(str(i))  
    subcat = driver.find_elements_by_xpath(subcatpath)
    o = 0
    for sc in subcat:
        o += 1
        subsubcatpath = '//div[@class="lzd-site-nav-menu-dropdown"]//ul[@class="lzd-site-menu-root"]//ul[@class="lzd-site-menu-sub Level_1_Category_No'+str(i)+'"]//li[@class="lzd-site-menu-sub-item"]//ul[@data-spm="cate_'+str(i)+'_'+str(o)+'"]//li[@class="lzd-site-menu-grand-item"]/a'
        subsubcat = driver.find_elements_by_xpath(subsubcatpath)
        ssclinkpath = '//div[@class="lzd-site-nav-menu-dropdown"]//ul[@class="lzd-site-menu-root"]//ul[@class="lzd-site-menu-sub Level_1_Category_No'+str(i)+'"]//li[@class="lzd-site-menu-sub-item"]//ul[@data-spm="cate_'+str(i)+'_'+str(o)+'"]//li[@class="lzd-site-menu-grand-item"]/a[@href]'
        ssclink = driver.find_elements_by_xpath(ssclinkpath)
        for ssc,sscl in zip(subsubcat,ssclink):
            scitem = sc.get_attribute('text')
            sscitem = ssc.get_attribute('text')
            ssclitem = sscl.get_attribute('href')
            catList.append(cat.text)
            subcatList.append(scitem.strip())
            subsubcatList.append(sscitem.strip())
            subsublinkList.append(ssclitem.strip())
    if i == 1 or i == 4 or i == 12:
        subcatex1 = '//div[@class="lzd-site-nav-menu-dropdown"]//ul[@class="lzd-site-menu-root"]//ul[@class="lzd-site-menu-sub Level_1_Category_No{0}"]//li[@class="sub-item-remove-arrow"]/a'.format(str(i))
        subcatexp1 = driver.find_elements_by_xpath(subcatex1)
        subcatex1linkpath = '//div[@class="lzd-site-nav-menu-dropdown"]//ul[@class="lzd-site-menu-root"]//ul[@class="lzd-site-menu-sub Level_1_Category_No{0}"]//li[@class="sub-item-remove-arrow"]/a[@href]'.format(str(i)) 
        subcatex1link = driver.find_elements_by_xpath(subcatex1linkpath)
        for sce,scel in zip(subcatexp1,subcatex1link):
            sceitem = sce.get_attribute('text')
            scelink = scel.get_attribute('href')
            catList.append(cat.text)
            subcatList.append(sceitem.strip())
            subsubcatList.append("None")
            subsublinkList.append(scelink.strip())
    i += 1

df = pd.DataFrame(list(zip(catList, subcatList, subsubcatList, subsublinkList)), 
               columns =['Category', 'Sub Category', 'Sub Sub Category', 'Link']) 

# This part is to crawl all the products in each sub sub category        
def check_exists_by_xpath(bb):
    try:
        bb.find_element_by_xpath('.//div[@class="c15YQ9"]//span[@class="c2i43- "]')
        location = bb.find_element_by_xpath('.//div[@class="c15YQ9"]//span[@class="c2i43- "]')
        locationList.append(location.text)
    except NoSuchElementException:
        locationList.append(" ")
        return False
    return True

def find(): 
    done = False
    curr_date = datetime.now()
    tdate = curr_date.strftime("%d-%m-%Y_%H:%M:%S") 
    while not done:
        try:
            content2 = driver.find_element_by_xpath(('//div[@class="c1_t2i"]'))
            return content2
            done = True
        except:
            print("start date time 1:",tdate)          
            time.sleep(120)
            done = False

def find2():
    done = False
    curr_date = datetime.now()
    tdate = curr_date.strftime("%d-%m-%Y_%H:%M:%S") 
    while not done:
        try:
            content2 = driver.find_element_by_xpath(('//div[@class="c1_t2i"]'))
            time.sleep(10)
            contents2 = content2.find_elements_by_xpath(('//div[@class="c2prKC"]'))
            return(contents2)
            done = True
        except:
            print("start date time 2:",tdate)           
            time.sleep(120)
            done = False
            
def link2(cc):                  
    done = False
    curr_date = datetime.now()
    tdate = curr_date.strftime("%d-%m-%Y_%H:%M:%S") 
    while not done:
        try:
            link2 = cc.find_element_by_xpath('.//div[@class="c16H9d"]/a[@href]')
            linkList.append(link2.get_attribute("href"))
            done = True
        except:
            print("start date time 3:",tdate)           
            time.sleep(60)
            done = False

def prod2(cc):
    done = False
    curr_date = datetime.now()
    tdate = curr_date.strftime("%d-%m-%Y_%H:%M:%S") 
    while not done:
        try:
            prod2 = cc.find_element_by_xpath('.//div[@class="c16H9d"]/a')
            prodList.append(prod2.text)
            print(prod2.text)
            done = True
        except:
            print("start date time 4:",tdate)           
            time.sleep(60)
            done = False
            
def price2(cc):
    done = False
    curr_date = datetime.now()
    tdate = curr_date.strftime("%d-%m-%Y_%H:%M:%S") 
    while not done:
        try:
            price2 = cc.find_element_by_xpath('.//div[@class="c3gUW0"]//span')
            priceList.append(price2.text)
            done = True
        except:
            print("start date time 5:",tdate)           
            time.sleep(60)
            done = False
            
def check_exists_by_xpath2(cc):
    try:
        cc.find_element_by_xpath('.//div[@class="c15YQ9"]//span[@class="c2i43- "]')
        location2 = cc.find_element_by_xpath('.//div[@class="c15YQ9"]//span[@class="c2i43- "]')
        locationList.append(location2.text)
    except NoSuchElementException: 
        locationList.append(" ")
        return False
    return True

def discount():
    try:
        discount = driver.find_element_by_xpath(('//div[@class="pdp-product-price"]//div[@class="origin-block"]//span[@class="pdp-product-price__discount"]'))
        discountL.append(discount.text)
        if discount.text == "":
            discountL.append(" ")
    except NoSuchElementException:
        discountL.append(" ")
        return False
    return True

def color():
    try:
        color1 = driver.find_element_by_xpath(('//div[@class="sku-selector"]//div[1]//div[@class="pdp-mod-product-info-section sku-prop-selection"]//div[@class="section-content"]//div[@class="sku-prop-content-header"]//span'))
        colorList.append(color1.text)
        colorlist = driver.find_elements_by_xpath(('//div[@class="sku-selector"]//div[1]//div[@class="pdp-mod-product-info-section sku-prop-selection"]//div[@class="section-content"]//div[@class="sku-prop-content"]//span[@class="sku-variable-img-wrap"]'))
        for eachcolor in colorlist:
            driver.execute_script("arguments[0].click();",eachcolor)
            color = driver.find_element_by_xpath(('//div[@class="sku-selector"]//div[1]//div[@class="pdp-mod-product-info-section sku-prop-selection"]//div[@class="section-content"]//div[@class="sku-prop-content-header"]//span'))
            colorList.append(color.text)
        i = '\n'.join(colorList)
        colorL.append(i)
        print(i)
    except NoSuchElementException:
        colorL.append(" ")
        return False
    return True

def storage():
    try:
        storage1 = driver.find_element_by_xpath(('//div[@class="sku-selector"]//div[2]//div[@class="pdp-mod-product-info-section sku-prop-selection"]//div[@class="section-content"]//div[@class="sku-prop-content-header"]//span'))
        storageList.append(storage1.text)
        storagelist = driver.find_elements_by_xpath(('//div[@class="sku-selector"]//div[2]//div[@class="pdp-mod-product-info-section sku-prop-selection"]//div[@class="section-content"]//div[@class="sku-prop-content"]//span[@class="sku-variable-name"]//span'))
        for eachstorage in storagelist:
            driver.execute_script("arguments[0].click();",eachstorage)
            storage = driver.find_element_by_xpath(('//div[@class="sku-selector"]//div[2]//div[@class="pdp-mod-product-info-section sku-prop-selection"]//div[@class="section-content"]//div[@class="sku-prop-content-header"]//span'))
            storageList.append(storage.text)
        m = '\n'.join(storageList)
        storageL.append(m)
        print(m)
    except NoSuchElementException:
        storageL.append(" ")
        return False
    return True

def quantityLeft():
    try:
        quantityLeft = driver.find_element_by_xpath(('//div[@class="pdp-mod-product-info-section sku-quantity-selection"]//div[@class="section-content"]//span[@class="quantity-content-default"]'))
        temp1 = re.findall(r'\d+', quantityLeft.text)
        for ii in temp1:
            quantityL.append(int(ii))
        if quantityLeft.text == "":
            quantityL.append("")
    except NoSuchElementException:
        quantityL.append(" ")
        return False
    return True

def noOfRating():
    done = False
    curr_date = datetime.now()
    tdate = curr_date.strftime("%d-%m-%Y_%H:%M:%S") 
    while not done:
        try:
            noOfRating = driver.find_element_by_xpath(('//div[@class="count"]'))
            totalRate.append(noOfRating.text) 
            print(noOfRating.text)
            done = True
        except:
            print("start date time 6:",tdate)           
            time.sleep(5)
            done = False

def check_exist_prod():
    try:
        notExistProd = driver.find_element_by_xpath('//div[@class="error-info"]')
        print("Sorry! This product is no longer available")
    except NoSuchElementException:
        print("Product Available")
        return False
    return True    

maincat = ["Electronic Devices","Electronic Accessories","TV & Home Appliances","Health & Beauty","Babies & Toys","Groceries & Pets","Home & Lifestyle","Women's Fashion","Men's Fashion","Fashion Accessories","Sports & Lifestyle","Automotive & Motorcycles"]
for maincategory in maincat: 
    current_date = datetime.now()
    csv_date = current_date.strftime("%Y%m%d_%H%M%S")
    file = maincategory.replace(" ", "_")
    filename = "Lazada_"+str(file)+"_"+str(csv_date)+".csv"
    with open(filename, 'w', newline='',encoding='utf-8-sig') as myfile:
        wr = csv.writer(myfile)
        fields = ['Category', 'Sub Category', 'Sub Sub Category', 'Link', 'Product Link', 'Product', 'Price', 'Location','Total Rating', 'Discount', 'Color', 'Storage', 'Quantity Left','Product detail','Rating&Reviews(Overall)','5star','4star','3star','2star','1star','Review'] 
        wr.writerow(fields)
        linkList = []
        prodList = []
        priceList = []
        locationList = []
        cat1 = []
        sc1 = []
        ssc1 = []
        sslink1 = []
        totalRate = []
        discountL = []
        colorL = []
        storageL = []
        quantityL = []
        descL = []
        overallRateL = []
        r5L =[]
        r4L =[]
        r3L =[]
        r2L =[]
        r1L =[]
        reviewL = []
        no = 0
        for cat,scat,ssc,olink in zip(df['Category'],df['Sub Category'],df['Sub Sub Category'],df['Link']):
            if cat == maincategory:
                print(cat,scat,ssc,olink)
                driver.get(olink)
                done1 = False
                curr_date1 = datetime.now()
                tdate1 = curr_date1.strftime("%d-%m-%Y_%H:%M:%S") 
                while not done1:
                    try:
                        content = driver.find_element_by_xpath(('//div[@class="c1_t2i"]'))
                        contents = content.find_elements_by_xpath(('//div[@class="c2prKC"]'))
                        done1 = True
                    except:
                        print("start date time 7:",tdate1)           
                        time.sleep(120)
                        done = False

                for bb in contents:
                    cat1.append(cat)
                    sc1.append(scat)
                    ssc1.append(ssc)
                    sslink1.append(olink)
                    link2(bb)
                    prod2(bb)
                    price2(bb)
                    check_exists_by_xpath(bb)
                
                page_number = 2
                while True:
                    try:
                        linktext = driver.find_element_by_link_text(str(page_number))
                    except NoSuchElementException:
                        break
                    driver.execute_script("arguments[0].click();",linktext)
                    time.sleep(5)
                    content2 = find()
                    contents2 = find2()

                    for cc in contents2:
                        cat1.append(cat)
                        sc1.append(scat)
                        ssc1.append(ssc)
                        sslink1.append(olink)

                        link2(cc)
                        prod2(cc)
                        price2(cc)
                        check_exists_by_xpath2(cc)
                    page_number += 1

                print(len(linkList))
                for olink in linkList:
                    driver.get(olink)  
                    if check_exist_prod()==True:
                        totalRate.append("") 
                        discountL.append("")
                        colorL.append("")
                        storageL.append("")
                        quantityL.append("")
                        descL.append("")
                        overallRateL.append("")
                        r5L.append("")
                        r4L.append("")
                        r3L.append("")
                        r2L.append("")
                        r1L.append("")
                        reviewL.append("")
                    else:
                        noOfRating()
                        discount()
                        colorList = []
                        color()
                        storageList = []
                        storage()
                        quantityLeft()

                        desclist = []
                        proddesc = driver.find_elements_by_xpath(('//div[@class="pdp-product-detail"]//div[@class="pdp-product-desc "]//div[@class="html-content pdp-product-highlights"]//ul//li'))
                        for desc in proddesc:
                            desclist.append(desc.text)

                        #some product description have different path
                        if desclist == []:
                            proddesc2 = driver.find_elements_by_xpath(('//div[@class="pdp-product-detail"]//div[@class="pdp-product-desc height-limit"]//div[@class="html-content pdp-product-highlights"]//ul//li'))
                            for desc2 in proddesc2:
                                desclist.append(desc2.text)

                        s = '\n'.join(desclist)
                        descL.append(s)

                        rating = driver.find_element_by_xpath(('//div[@class="score"]//span[1]'))
                        overallRateL.append(rating.text+"/5.0")   

                        rate5 = driver.find_element_by_xpath(('//div[@class="detail"]//ul//li[1]//span[2]'))
                        r5L.append(rate5.text)
                        rate4 = driver.find_element_by_xpath(('//div[@class="detail"]//ul//li[2]//span[2]'))
                        r4L.append(rate4.text)
                        rate3 = driver.find_element_by_xpath(('//div[@class="detail"]//ul//li[3]//span[2]'))
                        r3L.append(rate3.text)
                        rate2 = driver.find_element_by_xpath(('//div[@class="detail"]//ul//li[4]//span[2]'))
                        r2L.append(rate2.text)
                        rate1 = driver.find_element_by_xpath(('//div[@class="detail"]//ul//li[5]//span[2]'))
                        r1L.append(rate1.text)

                        chkhour = "hour"
                        chkhours = "hours"
                        chkmin = "minute"
                        chkmins = "minutes"
                        # This part is to crawl product review within a day 
                        eachReviewL = []
                        def check_exists_by_prodreview():
                            try:
                                review = driver.find_element_by_xpath(('//div[@class="mod-reviews"]'))
                                reviews = review.find_elements_by_xpath(('//div[@class="item"]')) 

                                for dd in reviews:
                                    a_dictionary ={}
                                    date = dd.find_element_by_xpath(('.//div[@class="top"]//span'))
                                    mydate = date.text
                                    if chkhour in mydate or chkhours in mydate:
                                        temp = re.findall(r'\d+', mydate)
                                        for i in temp:
                                            d = datetime.today() - timedelta(hours=int(i))
                                            today_date = datetime.now()
                                            today = today_date.strftime('%Y-%m-%d')
                                            a_dictionary["Date"] = today
                                            time = d.strftime('%H:%M %p')
                                            a_dictionary["Time"] = time

                                        reviewer = dd.find_element_by_xpath(('.//div[@class="middle"]//span[1]'))
                                        a_dictionary["Reviewer"] = reviewer.text

                                        reviewContent = dd.find_element_by_xpath(('.//div[@class="item-content"]//div[@class="content"]'))
                                        a_dictionary["Comment"] = reviewContent.text

                                        contentLike = dd.find_element_by_xpath(('.//div[@class="bottom"]//span[@class="left"]//span//span[2]'))
                                        a_dictionary["Like"] = contentLike.text
                                        eachReviewL.append(a_dictionary.copy())
                                    elif chkmin in mydate or chkmins in mydate:
                                        temp = re.findall(r'\d+', mydate)
                                        for i in temp:
                                            d = datetime.today() - timedelta(minutes=int(i))
                                            today_date = datetime.now()
                                            today = today_date.strftime('%Y-%m-%d')
                                            a_dictionary["Date"] = today
                                            time = d.strftime('%H:%M %p')
                                            a_dictionary["Time"] = time

                                        reviewer = dd.find_element_by_xpath(('.//div[@class="middle"]//span[1]'))
                                        a_dictionary["Reviewer"] = reviewer.text

                                        reviewContent = dd.find_element_by_xpath(('.//div[@class="item-content"]//div[@class="content"]'))
                                        a_dictionary["Comment"] = reviewContent.text

                                        contentLike = dd.find_element_by_xpath(('.//div[@class="bottom"]//span[@class="left"]//span//span[2]'))
                                        a_dictionary["Like"] = contentLike.text
                                        eachReviewL.append(a_dictionary.copy()) 
                                    else:
                                        pass
                            except NoSuchElementException: 
                                eachReviewL.append("") 
                                return False
                            return True

                        check_exists_by_prodreview()

                        def check_exists_by_btn():
                            try:
                                btnno = driver.find_element_by_xpath(('//div[@class="next-pagination next-pagination-normal next-pagination-arrow-only next-pagination-medium medium review-pagination"]//div[@class="next-pagination-pages"]//button[@class="next-btn next-btn-normal next-btn-medium next-pagination-item next"]'))    
                            except NoSuchElementException: 
                                print("no next page")
                                return False
                            return True


                        while check_exists_by_btn()==True:
                            btnno = driver.find_element_by_xpath(('//div[@class="next-pagination next-pagination-normal next-pagination-arrow-only next-pagination-medium medium review-pagination"]//div[@class="next-pagination-pages"]//button[@class="next-btn next-btn-normal next-btn-medium next-pagination-item next"]'))
                            if btnno.is_enabled():
                                driver.execute_script("arguments[0].click();",btnno)
                                time.sleep(5)
                                check_exists_by_prodreview()
                            else:
                                break

                        reviewL.append(eachReviewL)
                        info = []
                        info.append(cat1[no])
                        info.append(sc1[no])
                        info.append(ssc1[no])
                        info.append(sslink1[no])
                        info.append(linkList[no])
                        info.append(prodList[no])
                        info.append(priceList[no])
                        info.append(locationList[no])
                        info.append(totalRate[no])
                        info.append(discountL[no])
                        info.append(colorL[no])
                        info.append(storageL[no])
                        info.append(quantityL[no])
                        info.append(descL[no])
                        info.append(overallRateL[no])
                        info.append(r5L[no])
                        info.append(r4L[no])
                        info.append(r3L[no])
                        info.append(r2L[no])
                        info.append(r1L[no])
                        info.append(reviewL[no])
                        wr.writerow(info)
                        no += 1
