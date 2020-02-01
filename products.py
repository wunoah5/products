# 記帳程式
# v0.1 紀錄消費項目跟金額
# v0.2 建立檔案寫入
# v0.3 增加欄位名稱、檔案改為csv、編碼改為utf-8
# v0.4 讀取檔案、split()切 割資料

products = []

#這邊在讀取檔案
with open('products.csv', 'r', encoding='big5') as f:
    for line in f:
        s = line.strip().split(',')   #先把換行拿掉在做切割
        print(s)

'''
while True:
    name = input('請輸入消費項目: ')
    if name == 'q':
        break
    price =  input('請輸入金額: ')
    products.append([name, price])

#這邊在提醒本次輸入的資料
print('本次輸入資料為')
for p in products:
    print('消費項目', p[0], '消費金額', p[1])

# 把檔案存下
with open('products.csv', 'w', encoding='big5') as f:
    f.write('消費項目,消費金額\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')    # 在最後面加上\n表示每一行為一筆資料
print('資料已寫入')
'''