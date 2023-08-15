import requests
import json

# 通过 AlbumID 获得Album信息，主要是获得专辑名称，播放次数
# API：https://mobile.ximalaya.com/mobile-album/album/page/ts-2780581?ac=WIFI&albumId=2780581
# 2780581 为专辑ID

def getAlbumInfo(albumId):
    base_url = "https://mobile.ximalaya.com/mobile-album/album/page/ts-{}?ac=WIFI&albumId={}"
    response = requests.get(base_url.format(albumId, albumId))
    data = json.loads(response.text)
    title = data['data']['album']['title']
    playtimes = data['data']['album']['playtimes']
    return title, playtimes

if __name__ == "__main__":
    albumId = 34220825
    title, playtimes = getAlbumInfo(albumId)
    print(title, playtimes)
