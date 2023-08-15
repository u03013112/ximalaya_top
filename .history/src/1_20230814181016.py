# 作品的留存率，即第101~200集播放次数/1~100集播放次数，后面还可以加上201~300集播放次数/1~100集播放次数，以此类推。

import requests
import json

# 获得指定专辑的前N集的播放次数
# 获得API：https://mobwsa.ximalaya.com/mobile/playlist/album/page?albumId=2780581&pageId=4
# 其中albumId为专辑ID，pageId为页码，从1开始，每页20集，pageId=1 表示第1~20集，pageId=2表示第21~40集，以此类推。

# albumId 需要自己去官网获得，https://www.ximalaya.com/，点开专辑，地址栏中的路径就是专辑ID。比如https://www.ximalaya.com/youshengshu/2780581/
# step是指计算步长，比如step=50，就是计算51~100集的播放次数/1~50集的播放次数，step=100，就是计算101~200集的播放次数/1~100集的播放次数，以此类推。
# 返回值返回一个留存列表，列表的长度为count。

def getAlbumRetentionRate(albumId, step=50, count=2):
    retention_rates = []
    base_url = "https://mobwsa.ximalaya.com/mobile/playlist/album/page?albumId={}&pageId={}"
    total_plays = []

    # 计算基准播放次数
    for i in range(1, (step*(count+1))//20 + 2):
        response = requests.get(base_url.format(albumId, i))
        data = json.loads(response.text)
        for track in data['list']:
            total_plays.append(track['playtimes'])

    # 计算留存率
    for i in range(1, count+1):
        current_plays = sum(total_plays[i*step:(i+1)*step])
        base_plays = sum(total_plays[0:step])
        retention_rate = current_plays / base_plays
        retention_rates.append(retention_rate)

    return retention_rates
