import os
import sys
import csv

# 購入データをCSVから読み込む
with open(os.getcwd() + "\\purchase.csv",  newline='') as pF:
    pDataReader = csv.reader(pF)
#    for row in pDataReader:
#        print(row)


# 当選データをCSVから読み込む
# cSVの並び
# 開催回,日付,第1数字,第2数字,第3数字,第4数字,第5数字,第6数字,BONUS数字,1等口数,2等口数,3等口数,4等口数,5等口数,1等賞金,2等賞金,3等賞金,4等賞金,5等賞金,キャリーオーバー
with open(os.getcwd() + "\\loto6.csv",  newline='') as lF:
    lDataReader = csv.reader(lF)
    for row in lDataReader:
        print(row)

for row in pDataReader:
    print(row)




# 購入データをCSVから読み込む
#purchase = os.getcwd() + "\\purchase.csv"
#with open(purchase, "r") as p:
#    pList = p.read()     

#dataPath = os.getcwd() + "\\loto6.csv"
#if os.path.exists(dataPath) == False:
#    print('ファイルパスが存在しません')
#    sys.exit()

# 当選データをCSVから読み込む
# cSVの並び
# 開催回,日付,第1数字,第2数字,第3数字,第4数字,第5数字,第6数字,BONUS数字,1等口数,2等口数,3等口数,4等口数,5等口数,1等賞金,2等賞金,3等賞金,4等賞金,5等賞金,キャリーオーバー
#with open(dataPath, "r") as d:
#    pData = d.read()       
#    xx = pData.split(",")
#    print(xx[3])


 
 














# 検査する番号をCSVから読み込む

# 検査する

# 当たっていればメールする





