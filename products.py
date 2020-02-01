# 記帳程式
# v0.1 紀錄消費項目跟金額
# v0.2 建立檔案寫入

products = []
while True:
    name = input('請輸入消費項目: ')
    if name == 'q':
        break
    price =  input('請輸入金額: ')
    products.append([name, price])
print('本次輸入資料為')

#這邊在提醒本次輸入的資料
for p in products:
	print('消費項目', p[0], '消費金額', p[1])

# 把檔案存下
with open('products.txt', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')    # 在最後面加上\n表示每一行為一筆資料
print('資料已寫入')