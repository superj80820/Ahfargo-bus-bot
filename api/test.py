import re
if None != re.search('附近站牌/\d+.\d+,\d+.\d+/','附近站牌/21.2312,123.12323/'):
    print(re.search('\d+.\d+,\d+.\d+','附近站牌/21.2312,123.12323/').group())
    aa = re.search('\d+.\d+,\d+.\d+','附近站牌/21.2312,123.12323/').group()
    bb = aa.split(',')
    cc={}
    cc['lat'] = bb[0]
    cc['lon'] = bb[1]
    print(cc)