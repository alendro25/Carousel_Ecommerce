'''
|---------------------------------------|
|               PERSIAPAN               |
|---------------------------------------|
|Install :                              |
|1. Install PIP                         |
|2. Install Python                      |
|3. Install Selenium                    |
|4. Install Pandas                      |
|5. Install Openpyxl                    |
|---------------------------------------|
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

#driver = webdriver.Edge()
driver = webdriver.Chrome()
driver.get("https://id.carousell.com")

#Judul
#main > div.D_JB > div > section.D_JO > div.D_JT > div > div > div:nth-child(1) > div > div.D_qo.M_lh > a:nth-child(2) > p.D_oJ.M_jt.D_oK.M_ju.D_oO.M_jy.D_oR.M_jA.D_oU.M_jE.D_oW.M_jG.D_oS.M_jB.D_pe
# judul = driver.find_element(By.CSS_SELECTOR, '#main > div.D_IF > div > section.D_IR > div.D_IW > div > div > div > div > div.D_qI.M_lp > a:nth-child(2) > p.D_ok.M_jt.D_ol.M_ju.D_op.M_jy.D_os.M_jA.D_ov.M_jE.D_ox.M_jG.D_ot.M_jB.D_oA').text

#Harga
#main > div.D_JB > div > section.D_JO > div.D_JT > div > div > div:nth-child(1) > div > div.D_qo.M_lh > a:nth-child(2) > div.D_qH.M_l_ > p
# harga = driver.find_element(By.CSS_SELECTOR, 'main > div.D_JB > div > section.D_JO > div.D_JT > div > div > div:nth-child(1) > div > div.D_qo.M_lh > a:nth-child(2) > div.D_qH.M_l_ > p').text


#Kondisi
#main > div.D_JB > div > section.D_JO > div.D_JT > div > div > div:nth-child(1) > div > div.D_qo.M_lh > a:nth-child(2) > p:nth-child(4)
# kondisi = driver.find_element(By.CSS_SELECTOR, 'main > div.D_JB > div > section.D_JO > div.D_JT > div > div > div:nth-child(1) > div > div.D_qo.M_lh > a:nth-child(2) > p:nth-child(4)').text
# print (judul, harga, kondisi)

gadget=[]
datas = driver.find_elements(By.CSS_SELECTOR, value='#FieldSetField-Container-field_2 > div > div > div > div > div.D_qI > a:nth-child(2)')
for data in datas:
    judul = data.find_element(By.CSS_SELECTOR, value = '#FieldSetField-Container-field_2 > div > div > div > div > div.D_qI > a:nth-child(2) > p.D_ok.D_ol.D_op.D_os.D_ov.D_ox.D_ot.D_oA').text
    harga = data.find_element(By.CSS_SELECTOR, value = '#FieldSetField-Container-field_2 > div > div > div > div > div.D_qI > a:nth-child(2) > div.D_rb > p').text
    kondisi = data.find_element(By.CSS_SELECTOR, value = '#FieldSetField-Container-field_2 > div > div > div > div > div.D_qI > a:nth-child(2) > p:nth-child(4)').text
    print(judul, harga, kondisi)
    dt_gadget = {
        'Judul' : judul,
        'Harga' : harga,
        'Kondisi' : kondisi
    }
    gadget.append(dt_gadget)
    
df = pd.DataFrame(gadget)
print(df)
df.to_excel('Output.xlsx', sheet_name='Sheet_1')

driver.quit()
