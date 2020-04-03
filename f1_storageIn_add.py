# coding=utf-8
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest


class StorageIn_add(unittest.TestCase):
    driver = webdriver.Chrome()
    def test_addStorageIn(self, driver=driver):
        # login_go(self.driver).login()
        #商品中心--商品管理
        self.driver.get('http://mxdev.storeteam.cn/')#玄掌柜测试环境
        # self.driver.get("http://m.xzg.storeteam.cn/")#玄掌柜线上环境
        self.driver.maximize_window()
        #登录
        self.driver.find_element_by_css_selector("#MerchantNo").send_keys("yx")
        self.driver.find_element_by_css_selector("#UserName").send_keys("admin")
        self.driver.find_element_by_css_selector("#Password").send_keys("123456")
        self.driver.find_element_by_css_selector("#btn_login").click()
        time.sleep(1)
        driver.find_elements_by_class_name("ant-menu-item")[1].click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='ant-menu-submenu-title']/span[.='库存管理']").click()
        time.sleep(1)
        # #新建门票-----------------------------------------------------------------------------------------------------------------------------------------------
        driver.find_element_by_xpath("//a[@href='#/product/stock/in'][span[.='商品入库']]").click()
        # js = 'document.getElementsByClassName("ant-menu-item ant-menu-item-selected")[1].click();'
        # driver.execute_script(js)
        driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']").click()


        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='ant-select-selection-selected-value'][@title='采购入库']").click()
        # driver.find_element_by_class_name("ant-select-selection-selected-value").click()
        time.sleep(1)
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/ul/li[2]").click()
        js = 'document.getElementsByClassName("ant-select-dropdown-menu-item")[2].click();'
        driver.execute_script(js)
        time.sleep(1)
        driver.find_element_by_css_selector("div.ant-row:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li[2]").click()
        # js = 'document.getElementsByClassName("ant-select-dropdown-menu-item")[2].click();'
        # driver.execute_script(js)
        #选择商品
        driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']").click()
        driver.find_element_by_xpath("//input[@class='ant-input']").send_keys("雪碧Auto")
        # 输入雪碧
        time.sleep(3)
        driver.find_element_by_xpath("//button[@class='ant-btn ant-input-search-button ant-btn-primary']").click()
        # 点击搜索"
        driver.find_element_by_xpath("//span[@class='ant-checkbox-inner'][1]").click()
        time.sleep(2)
        # 点击勾选
        driver.find_element_by_xpath("//button[@class='ant-btn btn_form___34Q9c ant-btn-primary']").click()
        # 点击确定
        driver.find_element_by_xpath("//input[@class='ant-input-number-input']").send_keys('0')
        time.sleep(2)
        # 输入数量10
        #页面下拉（通过定位元素）
        driver.find_element_by_css_selector("button.ant-btn:nth-child(1)").click()

        driver.quit()



