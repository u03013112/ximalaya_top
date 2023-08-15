import requests
from lxml import etree

# 基础流程，先获取希望获得的所有专辑ID
# 然后通过专辑ID获取专辑信息，包括专辑名称，播放次数
# 再计算留存率
# 将结果保存到文件中 '../data/1.csv'



# 爬取专辑页类似：
# https://www.ximalaya.com/category/a3_b10880_c1433/
# https://www.ximalaya.com/category/a3_b10880_c1433/p2/
# https://www.ximalaya.com/category/a3_b10880_c1433/p3/
# 至少有50页
# 在页面里找到xpath为：'//li[@class = '_ZV']//div[@class = 'album-wrapper-card T_G']//@href'
# 得到的结果是类似‘/album/75449650’,需要处理一下，得到‘75449650’
# 每一页应该有56个结果，但是最后一页不一定有56个结果

def getAlbumIdList(pageNum):
    album_ids = []
    if pageNum == 1:
        url = "https://www.ximalaya.com/category/a3_b10880_c1433"
    else:
        url = "https://www.ximalaya.com/category/a3_b10880_c1433/p{}".format(pageNum)

    response = requests.get(url)
    print('response:',response)
    html = etree.HTML(response.text)
    hrefs = html.xpath('//li[@class = "_ZV"]//div[@class = "album-wrapper-card T_G"]//@href')

    for href in hrefs:
        album_id = href.split('/')[-1]
        album_ids.append(album_id)

    return album_ids

    
if __name__ == "__main__":
    print(getAlbumIdList(1))