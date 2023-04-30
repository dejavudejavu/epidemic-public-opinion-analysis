import json
import jieba
import csv
#安徽词库
anhui_list=[]
with open('Areas/anhui.txt','r',encoding='utf-8') as f1:
    lines = f1.readlines()
    for i in lines:
        word = i.strip()
        anhui_list.append(word)

#北京词库
beijing_list=[]
with open('Areas/beijing.txt','r',encoding='utf-8') as f2:
    lines = f2.readlines()
    for i in lines:
        word = i.strip()
        beijing_list.append(word)

#重庆词库
chongqing_list=[]
with open('Areas/chongqing.txt','r',encoding='utf-8') as f3:
    lines = f3.readlines()
    for i in lines:
        word = i.strip()
        chongqing_list.append(word)

#福建词库
fujian_list=[]
with open('Areas/fujian.txt','r',encoding='utf-8') as f4:
    lines = f4.readlines()
    for i in lines:
        word = i.strip()
        fujian_list.append(word)

#甘肃词库
gansu_list=[]
with open('Areas/gansu.txt','r',encoding='utf-8') as f5:
    lines = f5.readlines()
    for i in lines:
        word = i.strip()
        gansu_list.append(word)

#广东词库
guangdong_list=[]
with open('Areas/guangdong.txt','r',encoding='utf-8') as f6:
    lines = f6.readlines()
    for i in lines:
        word = i.strip()
        guangdong_list.append(word)

#广西词库
guangxi_list=[]
with open('Areas/guangxi.txt','r',encoding='utf-8') as f7:
    lines = f7.readlines()
    for i in lines:
        word = i.strip()
        guangxi_list.append(word)

#贵州词库
guizhou_list=[]
with open('Areas/guizhou.txt','r',encoding='utf-8') as f8:
    lines = f8.readlines()
    for i in lines:
        word = i.strip()
        guizhou_list.append(word)

#海南词库
hainan_list=[]
with open('Areas/hainan.txt','r',encoding='utf-8') as f9:
    lines = f9.readlines()
    for i in lines:
        word = i.strip()
        hainan_list.append(word)

#河北词库
hebei_list=[]
with open('Areas/hebei.txt','r',encoding='utf-8') as f10:
    lines = f10.readlines()
    for i in lines:
        word = i.strip()
        hebei_list.append(word)

#黑龙江词库
heilongjiang_list=[]
with open('Areas/heilongjiang.txt','r',encoding='utf-8') as f11:
    lines = f11.readlines()
    for i in lines:
        word = i.strip()
        heilongjiang_list.append(word)

#河南词库
henan_list=[]
with open('Areas/henan.txt','r',encoding='utf-8') as f12:
    lines = f12.readlines()
    for i in lines:
        word = i.strip()
        henan_list.append(word)

#湖北词库
hubei_list=[]
with open('Areas/hubei.txt','r',encoding='utf-8') as f13:
    lines = f13.readlines()
    for i in lines:
        word = i.strip()
        hubei_list.append(word)

#湖南词库
hunan_list=[]
with open('Areas/hunan.txt','r',encoding='utf-8') as f14:
    lines = f14.readlines()
    for i in lines:
        word = i.strip()
        hunan_list.append(word)

#江苏词库
jiangsu_list=[]
with open('Areas/jiangsu.txt','r',encoding='utf-8') as f15:
    lines = f15.readlines()
    for i in lines:
        word = i.strip()
        jiangsu_list.append(word)

#江西词库
jiangxi_list=[]
with open('Areas/jiangxi.txt','r',encoding='utf-8') as f16:
    lines = f16.readlines()
    for i in lines:
        word = i.strip()
        jiangxi_list.append(word)

#吉林词库
jilin_list=[]
with open('Areas/jilin.txt','r',encoding='utf-8') as f17:
    lines = f17.readlines()
    for i in lines:
        word = i.strip()
        jilin_list.append(word)

#辽宁词库
liaoning_list=[]
with open('Areas/liaoning.txt','r',encoding='utf-8') as f18:
    lines = f18.readlines()
    for i in lines:
        word = i.strip()
        liaoning_list.append(word)

#内蒙古词库
neimenggu_list=[]
with open('Areas/neimenggu.txt','r',encoding='utf-8') as f19:
    lines = f19.readlines()
    for i in lines:
        word = i.strip()
        neimenggu_list.append(word)

#宁夏词库
ningxia_list=[]
with open('Areas/ningxia.txt','r',encoding='utf-8') as f20:
    lines = f20.readlines()
    for i in lines:
        word = i.strip()
        ningxia_list.append(word)

#青海词库
qinghai_list=[]
with open('Areas/qinghai.txt','r',encoding='utf-8') as f21:
    lines = f21.readlines()
    for i in lines:
        word = i.strip()
        qinghai_list.append(word)

#山东词库
shandong_list=[]
with open('Areas/shandong.txt','r',encoding='utf-8') as f22:
    lines = f22.readlines()
    for i in lines:
        word = i.strip()
        shandong_list.append(word)

#上海词库
shanghai_list=[]
with open('Areas/shanghai.txt','r',encoding='utf-8') as f23:
    lines = f23.readlines()
    for i in lines:
        word = i.strip()
        shanghai_list.append(word)

#山西词库
shanxi1_list=[]
with open('Areas/shanxi1.txt','r',encoding='utf-8') as f24:
    lines = f24.readlines()
    for i in lines:
        word = i.strip()
        shanxi1_list.append(word)

#陕西词库
shanxi3_list=[]
with open('Areas/shanxi3.txt','r',encoding='utf-8') as f25:
    lines = f25.readlines()
    for i in lines:
        word = i.strip()
        shanxi3_list.append(word)

#四川词库
sichuan_list=[]
with open('Areas/sichuan.txt','r',encoding='utf-8') as f26:
    lines = f26.readlines()
    for i in lines:
        word = i.strip()
        sichuan_list.append(word)

#台湾词库
taiwan_list=[]
with open('Areas/taiwan.txt','r',encoding='utf-8') as f27:
    lines = f27.readlines()
    for i in lines:
        word = i.strip()
        taiwan_list.append(word)

#天津词库
tianjin_list=[]
with open('Areas/tianjin.txt','r',encoding='utf-8') as f28:
    lines = f28.readlines()
    for i in lines:
        word = i.strip()
        tianjin_list.append(word)

#新疆词库
xinjiang_list=[]
with open('Areas/xinjiang.txt','r',encoding='utf-8') as f29:
    lines = f29.readlines()
    for i in lines:
        word = i.strip()
        xinjiang_list.append(word)

#西藏词库
xizang_list=[]
with open('Areas/xizang.txt','r',encoding='utf-8') as f30:
    lines = f30.readlines()
    for i in lines:
        word = i.strip()
        xizang_list.append(word)

#云南词库
yunnan_list=[]
with open('Areas/yunnan.txt','r',encoding='utf-8') as f31:
    lines = f31.readlines()
    for i in lines:
        word = i.strip()
        yunnan_list.append(word)

#浙江词库
zhejiang_list=[]
with open('Areas/zhejiang.txt','r',encoding='utf-8') as f32:
    lines = f32.readlines()
    for i in lines:
        word = i.strip()
        zhejiang_list.append(word)

#博文读取
content=[]
with open('test.tsv','r',encoding='utf-8') as f:
    reader=csv.reader(f,delimiter='\t')
    for line in reader:
        content.append(line[0])
words=[]
for dic in content:
    words.append(list(jieba.cut(dic)))

#各地计数
anhui_num=0
beijing_num=0
chongqing_num=0
fujian_num=0
gansu_num=0
guangdong_num=0
guangxi_num=0
guizhou_num=0
hainan_num=0
hebei_num=0
heilongjiang_num=0
henan_num=0
hubei_num=0
hunan_num=0
jiangsu_num=0
jiangxi_num=0
jilin_num=0
liaoning_num=0
neimenggu_num=0
ningxia_num=0
qinghai_num=0
shandong_num=0
shanghai_num=0
shanxi1_num=0
shanxi3_num=0
sichuan_num=0
taiwan_num=0
tianjin_num=0
xinjiang_num=0
xizang_num=0
yunnan_num=0
zhejiang_num=0
total=0
for w in words:
    for a in w:
        if a in anhui_list:
            anhui_num = anhui_num + 1
            total = total + 1
            break
    for a in w:
        if a in beijing_list:
            beijing_num = beijing_num + 1
            total = total + 1
            break
    for a in w:
        if a in chongqing_list:
            chongqing_num = chongqing_num + 1
            total = total + 1
            break
    for a in w:
        if a in fujian_list:
            fujian_num = fujian_num + 1
            total = total + 1
            break
    for a in w:
        if a in gansu_list:
            gansu_num = gansu_num + 1
            total = total + 1
            break
    for a in w:
        if a in guangdong_list:
            guangdong_num = guangdong_num + 1
            total = total + 1
            break
    for a in w:
        if a in guangxi_list:
            guangxi_num = guangxi_num + 1
            total = total + 1
            break
    for a in w:
        if a in guizhou_list:
            guizhou_num = guizhou_num + 1
            total = total + 1
            break
    for a in w:
        if a in hainan_list:
            hainan_num = hainan_num + 1
            total = total + 1
            break
    for a in w:
        if a in hebei_list:
            hebei_num = hebei_num + 1
            total = total + 1
            break
    for a in w:
        if a in heilongjiang_list:
            heilongjiang_num = heilongjiang_num + 1
            total = total + 1
            break
    for a in w:
        if a in henan_list:
            henan_num = henan_num + 1
            total = total + 1
            break
    for a in w:
        if a in hubei_list:
            hubei_num = hubei_num + 1
            total = total + 1
            break
    for a in w:
        if a in hunan_list:
            hunan_num = hunan_num + 1
            total = total + 1
            break
    for a in w:
        if a in jiangsu_list:
            jiangsu_num = jiangsu_num + 1
            total = total + 1
            break
    for a in w:
        if a in jiangxi_list:
            jiangxi_num = jiangxi_num + 1
            total = total + 1
            break
    for a in w:
        if a in jilin_list:
            jilin_num = jilin_num + 1
            total = total + 1
            break
    for a in w:
        if a in liaoning_list:
            liaoning_num = liaoning_num + 1
            total = total + 1
            break
    for a in w:
        if a in neimenggu_list:
            neimenggu_num = neimenggu_num + 1
            total = total + 1
            break
    for a in w:
        if a in ningxia_list:
            ningxia_num = ningxia_num + 1
            total = total + 1
            break
    for a in w:
        if a in qinghai_list:
            qinghai_num = qinghai_num + 1
            total = total + 1
            break
    for a in w:
        if a in shanxi1_list:
            shanxi1_num = shanxi1_num + 1
            total = total + 1
            break
    for a in w:
        if a in shanxi3_list:
            shanxi3_num = shanxi3_num + 1
            total = total + 1
            break
    for a in w:
        if a in sichuan_list:
            sichuan_num = sichuan_num + 1
            total = total + 1
            break
    for a in w:
        if a in taiwan_list:
            taiwan_num = taiwan_num + 1
            total = total + 1
            break
    for a in w:
        if a in tianjin_list:
            tianjin_num = tianjin_num + 1
            total = total + 1
            break
    for a in w:
        if a in xinjiang_list:
            xinjiang_num = xinjiang_num + 1
            total = total + 1
            break
    for a in w:
        if a in xizang_list:
            xizang_num = xizang_num + 1
            total = total + 1
            break
    for a in w:
        if a in yunnan_list:
            yunnan_num = yunnan_num + 1
            total = total + 1
            break
    for a in w:
        if a in zhejiang_list:
            zhejiang_num = zhejiang_num + 1
            total = total + 1
            break
example=[]
example.append({'name':'安徽','value':anhui_num,'scale':format(anhui_num/total*100,'.2f')+'%'})
example.append({'name':'北京','value':beijing_num,'scale':format(beijing_num/total*100,'.2f')+'%'})
example.append({'name':'重庆','value':chongqing_num,'scale':format(chongqing_num/total*100,'.2f')+'%'})
example.append({'name':'福建','value':fujian_num,'scale':format(fujian_num/total*100,'.2f')+'%'})
example.append({'name':'甘肃','value':gansu_num,'scale':format(gansu_num/total*100,'.2f')+'%'})
example.append({'name':'广东','value':guangdong_num,'scale':format(guangdong_num/total*100,'.2f')+'%'})
example.append({'name':'广西','value':guangxi_num,'scale':format(guangxi_num/total*100,'.2f')+'%'})
example.append({'name':'贵州','value':guizhou_num,'scale':format(guizhou_num/total*100,'.2f')+'%'})
example.append({'name':'海南','value':hainan_num,'scale':format(hainan_num/total*100,'.2f')+'%'})
example.append({'name':'河北','value':hebei_num,'scale':format(hebei_num/total*100,'.2f')+'%'})
example.append({'name':'黑龙江','value':heilongjiang_num,'scale':format(heilongjiang_num/total*100,'.2f')+'%'})
example.append({'name':'河南','value':henan_num,'scale':format(henan_num/total*100,'.2f')+'%'})
example.append({'name':'湖北','value':hubei_num,'scale':format(hubei_num/total*100,'.2f')+'%'})
example.append({'name':'湖南','value':hunan_num,'scale':format(hunan_num/total*100,'.2f')+'%'})
example.append({'name':'江苏','value':jiangsu_num,'scale':format(jiangsu_num/total*100,'.2f')+'%'})
example.append({'name':'江西','value':jiangxi_num,'scale':format(jiangxi_num/total*100,'.2f')+'%'})
example.append({'name':'吉林','value':jilin_num,'scale':format(jilin_num/total*100,'.2f')+'%'})
example.append({'name':'辽宁','value':liaoning_num,'scale':format(liaoning_num/total*100,'.2f')+'%'})
example.append({'name':'内蒙古','value':neimenggu_num,'scale':format(neimenggu_num/total*100,'.2f')+'%'})
example.append({'name':'宁夏','value':ningxia_num,'scale':format(ningxia_num/total*100,'.2f')+'%'})
example.append({'name':'青海','value':qinghai_num,'scale':format(qinghai_num/total*100,'.2f')+'%'})
example.append({'name':'山东','value':shandong_num,'scale':format(shandong_num/total*100,'.2f')+'%'})
example.append({'name':'上海','value':shanghai_num,'scale':format(shanghai_num/total*100,'.2f')+'%'})
example.append({'name':'山西','value':shanxi1_num,'scale':format(shanxi1_num/total*100,'.2f')+'%'})
example.append({'name':'陕西','value':shanxi3_num,'scale':format(shanxi3_num/total*100,'.2f')+'%'})
example.append({'name':'四川','value':sichuan_num,'scale':format(sichuan_num/total*100,'.2f')+'%'})
example.append({'name':'台湾','value':taiwan_num,'scale':format(taiwan_num/total*100,'.2f')+'%'})
example.append({'name':'天津','value':tianjin_num,'scale':format(tianjin_num/total*100,'.2f')+'%'})
example.append({'name':'新疆','value':xinjiang_num,'scale':format(xinjiang_num/total*100,'.2f')+'%'})
example.append({'name':'西藏','value':xizang_num,'scale':format(xizang_num/total*100,'.2f')+'%'})
example.append({'name':'云南','value':yunnan_num,'scale':format(yunnan_num/total*100,'.2f')+'%'})
example.append({'name':'浙江','value':zhejiang_num,'scale':format(zhejiang_num/total*100,'.2f')+'%'})
with open('Area.json','w',encoding='utf-8') as g:
    json.dump(example,g,ensure_ascii=False)