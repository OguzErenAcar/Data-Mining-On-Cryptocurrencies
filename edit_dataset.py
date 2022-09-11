import pandas as pd

#
# dataset.drop([0], inplace = True)
# dataset = pd.read_csv("binance_ekim.csv")
# X=dataset.iloc[:,[3,4]].values
#
#
# i=0
# j=0;
# kripto_index=[]
# while k1[0:-2]!="ZRXUSDT":
#         try:
#             k1 = str(kriptolar[i])
#             k2 = str(kriptolar[i+1])
#             k3 = str(kriptolar[i+2])
#         except:
#              break
#         if k1[0:-2]==k2[0:-5] and k1[0:-2]==k3[0:-5]:
#             print(kriptolar[i],i)
#             j = j + 1;
#             i=i+2
#         elif k1[0:-2]==k2[0:-5]:
#             print(k1,i,":)")
#             print(k2,i,":")
#             kripto_index.append(i)
#             kripto_index.append(i+1)
#             i=i+1
#         else:
#             kripto_index.append(i)
#             print(k1,i)
#
#         i=i+1
# for i in range(1,3672,3):
#     dataset.iloc[i,15]=dataset.iloc[i+1,8]
#     print(dataset.iloc[i,15])

#print( dataset)
# dataset.drop(kripto_index, inplace = True)
#

# for i in range(0,3676,3):
#     k1=str(kriptolar[i])
#     for j in range(0,1211):
#         k2=str(dataset_8.iloc[j,[0]].values)
#         if k1[:-2]==k2[: -5]:
#             # dataset.iloc[i+2,12]=dataset_8.iloc[j,6]
#             print(j)
#
# dataset.to_csv("BİNANCE_karma.csv",index=False)
#
# l=0
# t=0
# c=0
# for i in range(0,3673,3):
#     # print(dataset.iloc[i, [0]].values)
#     # print(dataset_8.iloc[i, [0]].values)
#     k1 = str(kriptolar[i])
#     while l<1211:
#         k2 = str(dataset_8.iloc[l,[0]].values)
#         if k1[:-2] == k2[: -5]:
#             print(k1[:-2] , k2[: -5])
#             dataset.iloc[i,13]=dataset_8.iloc[l,6]
#             c=l
#             l=1211
#         l=l+1
#     l=c-1
# for i in range(0,3673,3):
#     dataset.iloc[i+2, [13]]=dataset.iloc[i+1, [6]]

#boş volleri sil
# for i in range(0,3673,3):
# c=0
# for i in range(0,3670):
#      if dataset.iloc[i, [13]].values==0:
#          c=c+1
#          print(dataset.iloc[i, [0]].values,i)
#
# print(c)
# import csv
# with open("BİNANCE_EKİM.csv", newline='') as csvfile:
#
#     spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
#
#     for row in spamreader:
#             print(','.join(row))

# import csv
# n=0
# c=0
# with open("BİNANCE_karma.csv", newline='') as csvfile:
#
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#
#     for row in spamreader:
#         if n==1:
#             print(','.join(row))
#             n=n+1
#         elif 0<=n<2:
#             n=n+1
#         else:
#             n=0
# dataset.to_csv("BİNANCE_karma.csv",index=False)

# diger ayı indir
# gereksiz ilk indisleri sil
# binance karmadaki isim indirilende varsa binance karmaya ordaki volumu ekle
# , lü her ayı ayrı yaz kopyala veya yeni klosere yazdır
# excelle geç 3 dosyanın farklarını al gereksizleri sil 0 ları ayarla
# 3 dosyayı python a at kmeans...
# küme sayılarına göre ortakları bul
# ortakları yazdır