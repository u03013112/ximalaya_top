import requests
from lxml import etree

from tool import getAlbumInfo
from f1 import getAlbumRetentionRate

# 爬取专辑页类似：
# https://www.ximalaya.com/category/a3_b10880_c1433/
# https://www.ximalaya.com/category/a3_b10880_c1433/p2/
# https://www.ximalaya.com/category/a3_b10880_c1433/p3/
# 至少有50页
# 在页面里找到xpath为：'//li[@class = '_ZV']//div[@class = 'album-wrapper-card T_G']//@href'
# 得到的结果是类似‘/album/75449650’,需要处理一下，得到‘75449650’
# 每一页应该有56个结果，但是最后一页不一定有56个结果

ablum_ids1 = [34220825,61310701,8695127,75919402,37081450,26085992,51079830,9724463,51626147,14356532,15828621,70969830,12840710,26711700,3011755,4137349,60639121,75920171,57319414,47132142,69706670,3290982,51398953,20047196,54050594,30788238,21981646,18368568,29316562,28731925,55149881,13617430,11469973,24619805,18057491,39714112,12214403,2949823,70481640,73170318,69801677,36096442,57065461,75172083,71331388,28760685,68216490,60639769,20133661,75885102,47410676,76058056,52328089,49405823,2879299,11436346]
ablum_ids2 = [65848442,70965080,75115229,71978389,71367410,24873849,64789616,67844532,23875053,6142095,50716182,3070943,33920963,70522857,69856043,11334318,39820880,74338866,51886654,20134188,54989773,49383263,74788321,54152363,71615281,56466070,45099200,5101446,15385624,13328902,63638584,57062331,6408451,2910083,52626062,51078900,58160236,42467704,48181930,3057947,16765936,53768549,44549805,71664965,21406206,76803582,73454475,7952590,71592768,14471827,64773666,68183468,4614426,26764200,54076235,48373328]

def main1(ablum_ids):
    csvFilename = '../data/main1.csv'
    with open(csvFilename, 'w', encoding='utf-8') as f:
        # 先写一个表头：名字，播放次数，留存率1，留存率2，留存率3，留存率4
        f.write('name,playtimes,retention_rate1,retention_rate2,retention_rate3,retention_rate4\n')
        for albumId in ablum_ids:
            title, playtimes = getAlbumInfo(albumId)
            print(title, playtimes)
            retention_rates = getAlbumRetentionRate(albumId, step=100, count=4)
            print(retention_rates)
            # 写入csv文件
            f.write('{},{},{},{},{},{}\n'.format(title, playtimes, retention_rates[0], retention_rates[1], retention_rates[2], retention_rates[3]))



if __name__ == "__main__":
    ablum_ids = ablum_ids1 + ablum_ids2
    main1(ablum_ids)