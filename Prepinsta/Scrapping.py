"""
1. Visit Website 
2. Select Question
3. Create File with that title of question.py + Give nubmer 
4. Scrapp the website and Visit there 
5. Copy Green file content and copy in python file and save. 

"""
import re
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time 
import os





driver = webdriver.Chrome(executable_path='D:\Projects_new\Whatsapp_Automation\chromedriver.exe')
web_url = 'https://prepinsta.com/top-100-codes/'
driver.get(web_url)
driver.maximize_window()


try: 
    element = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div/section[3]/div[2]/div/div[1]/div/div/div[1]/div/h2"))
    )
    

    lis = driver.find_elements(By.CLASS_NAME,'blue')
    print(type(lis))

    list_of_websites = []
    for i in lis:
        list_of_websites.append(i.get_attribute('href'))
    print("done")
    
    for i in range(140,len(list_of_websites)):
        driver.get(list_of_websites[i])

        try:
            Popup = driver.find_element(By.XPATH,'//*[@id="popup_box_close_1325359"]')
            if Popup:
                Popup.click()
        except Exception as e:
            pass

        try:
            element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[4]/div/div/div[1]/div/div/section[1]/div/div/div[1]/div/div/div[1]/div/div/h2/span'))
                ) 
            c = 1
        except Exception as e:
            c = 0 
        
        if c:
            name = element
            data  = driver.find_element(By.XPATH,'/html/body/div[2]/div[4]/div/div/div[1]/div/div/section[1]/div/div/div[1]/div/div')
        
        else:
            name = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[4]/div/div/div[1]/div/div/section[1]/div/div/div[2]/div/div/div/div/div/h2/span'))
            ) 
            data  = driver.find_element(By.XPATH,'/html/body/div[2]/div[4]/div/div/div[1]/div/div/section[1]/div/div/div[2]/div/div/div/div/div')
        

            
        #name = driver.find_element(By.XPATH,'/html/body/div[2]/div[4]/div/div/div[1]/div/div/section[1]/div/div/div[1]/div/div/div[1]/div/div/h2/span')
        
        
        a = name.text
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        file_name =str(i)+"_"+ a.replace(" ","_")+'.py'
        if(regex.search(file_name) == None):
            file_name =str(i)+"_"+ a.replace(" ","_")+'.py'
        else:
            file_name =str(i)+"_"+ a.replace(" ","_")+'.py'
            file_name = file_name.replace('?','_')
        print(file_name)
        print("8"*8)
        print(data.text)

        with open(file_name,'w') as f:
            f.write("'''\n")
            f.write(list_of_websites[i])

            f.write('\n'+ data.text)
            f.write("\n'''")
        
        print('Not found ')
        
            


except Exception as e:
    print(str(e))

