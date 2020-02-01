# 記帳程式
# v0.1 紀錄消費項目跟金額
products = []
while True:
    name = input('請輸入消費項目: ')
    if name == 'q':
        break
    price =  input('請書 入金額: ')
    products.append([name, price])
print(products)

	
