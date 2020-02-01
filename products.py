# 記帳程式
# v0.1 紀錄消費項目跟金額
# v0.2 建立檔案寫入
# v0.3 增加欄位名稱、檔案改為csv、編碼改為utf-8
# v0.4 讀取檔案、split()切 割資料
# v0.5 continue跳到下回
# v0.6 檢查檔案是否存在

import os

#這邊在檢查檔案是否存在，在的話讀取檔案
products = []
if os.path.isfile('products.csv'):    #檢查檔案是否存在
	with open('products.csv', 'r', encoding='big5') as f:
	    for line in f:
	        if '消費項目,消費金額' in line:
	            continue
	        name, price = line.strip().split(',')    #先把換行拿掉在做切割，把拿到的資料分別寫入name,price
	        products.append([name, price])    #將切割出來的資料加到produxts清單中，方便之後使用
	print(products)
else:
	print('找不到檔案...')

#這邊在請使用者輸入的資料
while True:
    name = input('請輸入消費項目: ')
    if name == 'q':
        break
    price =  input('請輸入金額: ')
    products.append([name, price])

#印出所有資料
print('所有資料為')
for p in products:
    print('消費項目', p[0], '消費金額', p[1])

# 把檔案存下
with open('products.csv', 'w', encoding='big5') as f:
    f.write('消費項目,消費金額\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')    # 在最後面加上\n表示每一行為一筆資料
print('資料已寫入')