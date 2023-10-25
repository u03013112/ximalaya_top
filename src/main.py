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

def getAlbumIds(urlList):
    ablum_ids = []
    for url in urlList:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        r = requests.get(url, headers=headers)

        print('正在爬取{}'.format(url))
        try:
            html = etree.HTML(r.text)
            album_ids = html.xpath('//li[@class = "_ZV"]//div[@class = "album-wrapper-card T_G"]//@href')
            album_ids = [album_id.split('/')[-1] for album_id in album_ids]
            # 将每个URL的结果添加到ablum_ids列表中
            ablum_ids.extend(album_ids)
            print('已经爬取了{}个专辑'.format(len(ablum_ids)))
        except Exception as e:
            print(e)

    return ablum_ids


def main1(ablum_ids):
    csvFilename = '../data/main3.csv'
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
            # 缓存写入
            f.flush()



if __name__ == "__main__":
    urlList = [
        'https://www.ximalaya.com/category/a3_b10880_c1433/',
    ]
    for i in range(2, 51):
        urlList.append('https://www.ximalaya.com/category/a3_b10880_c1433/p{}/'.format(i))

    ablum_ids = getAlbumIds(urlList)
    main1(ablum_ids)