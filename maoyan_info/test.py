# -*- coding = utf-8 -*-
# @Time : 2022/7/1 10:19
# @Author : CQU20205644
# @File : test.py
# @Software : PyCharm
import time,random,hashlib,requests,jsonpath,re,ddddocr,io,uuid
from fontTools.ttLib import TTFont
from PIL import ImageFont, Image, ImageDraw

ocr = ddddocr.DdddOcr()

def main():
    uid=uuid.uuid4()
    ts=time.time()*1000
    key='A013F70DB97834C0A5492378BD76C53A'
    ua='TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMS4wLjQ5NTEuNjQgU2FmYXJpLzUzNy4zNiBFZGcvMTAxLjAuMTIxMC41Mw=='
    index=int(1000*random.random()+1)
    enstr=f'method=GET&timeStamp={ts}&User-Agent={ua}&index={index}&channelId=40009&sVersion=2&key={key}'
    signkey=hashlib.md5(enstr.encode(encoding='UTF-8')).hexdigest()
    url=f'https://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid={uid}&timeStamp={ts}&User-Agent={ua}&index={index}&channelId=40009&sVersion=2&signKey={signkey}'
    headers={
        'Accept':'application/json, text/plain, */*',
        'Referer':'https://piaofang.maoyan.com/dashboard',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
    }
    html=requests.get(url,headers=headers,verify=False)
    print(html.json())
    fonturl='http:'+re.search('opentype"\),url\("(//.*?\.woff)"',html.json()['fontStyle']).group(1)
    print('fonturl'+fonturl)
    r = requests.get(fonturl)
    with open('temp.woff', 'wb') as f:
        f.write(r.content)
        f.close
    tfont = TTFont("temp.woff")
    uni_list = tfont.getGlyphOrder()[2:]
    print('uni列表：',uni_list)

    charList = []
    font = ImageFont.truetype("temp.woff", 40)
    #将10个uni字符画到im，进而使用ocr识别获得对应数字
    for uchar in uni_list:
        unknown_char = f"\\u{uchar[3:]}".encode().decode("unicode_escape")
        im = Image.new(mode='RGB', size=(42, 40), color="white")
        draw = ImageDraw.Draw(im=im)
        draw.text(xy=(0, 0), text=unknown_char, fill=0, font=font)
        img_byte = io.BytesIO()
        im.save(img_byte, format='JPEG')
        charList.append(ocr.classification(img_byte.getvalue()))
    print('对应字符：',charList)

    #解析获取需要的数据
    moviename=jsonpath.jsonpath(html.json(),'$.movieList.data.list..movieInfo.movieName')
    movieInfo = jsonpath.jsonpath(html.json(), '$.movieList.data.list..movieInfo.releaseInfo')
    sumBoxDesc = jsonpath.jsonpath(html.json(), '$.movieList.data.list..sumBoxDesc')
    boxRate = jsonpath.jsonpath(html.json(), '$.movieList.data.list..boxRate') #票房占比
    showCount = jsonpath.jsonpath(html.json(), '$.movieList.data.list..showCount') #排片场次
    enNum=jsonpath.jsonpath(html.json(), '$.movieList.data.list..boxSplitUnit.num')
    enNumDw=jsonpath.jsonpath(html.json(), '$.movieList.data.list..boxSplitUnit.unit')

    namelist=[]
    zonghepiaofang=[]
    paipiancishu=[]

    #解析票房信息
    for j in range(len(moviename)):
        tmpstr=enNum[j].split(';')
        rstr=''
        for i in tmpstr:
            if i =='': continue
            tmp = 'uni' + i.replace('&#x', '', 1).replace('.','').upper()
            for k in range(len(uni_list)):
                if tmp == uni_list[k]:
                    if '.' in i:
                        rstr = rstr + '.'+charList[k]
                    else:
                        rstr = rstr + charList[k]
                        #print(rstr)
                    break
        print(f'{moviename[j]}\t{movieInfo[j]}\t{sumBoxDesc[j]}\t综合票房：{rstr}{enNumDw[j]}\t票房占比：{boxRate[j]}\t排片场次：{showCount[j]}')
        namelist.append(moviename[j])
        zonghepiaofang.append(rstr)
        paipiancishu.append(showCount[j])
    # print(namelist)
    # print(zonghepiaofang)
    # print(paipiancishu)


if __name__ == '__main__':
    main()