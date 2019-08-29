# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
# 
import tensorflow as tf
import math
import numpy as np


def __is_bounded(direction,range,index,tokens_leng):
    cover = range*direction
    if cover+index<0 or cover+index >= tokens_leng:
        return True
    else:
        return False

def get_context(tokens, window_size):
    context_pair = []
    for i, token in enumerate(tokens):
        for j in range(1, window_size+1):
            if not __is_bounded(1,j,i,len(tokens)):
                context_pair.append((tokens[i],tokens[i+j]))
            if not __is_bounded(-1,j,i,len(tokens)):
                context_pair.append((tokens[i],tokens[i-j]))
    return context_pair

def __get_word_set(tokens):
    word_set = set()
    for token in tokens:
        word_set.add(token)
    return word_set

def __get_word_index(word_set):
    word_index_dic = dict()
    inverse_word_dic = dict()
    for i,word in enumerate(word_set):
        word_index_dic[word] = i
        inverse_word_dic[i] = word
    return word_index_dic,inverse_word_dic

def generate_batch(context_pair,batch_size):
    batch_list =[]
    batch=[]
    for i,pair in enumerate(context_pair):

        if i %batch_size==0 and i !=0:
            batch_list.append(batch)
            batch = []

        batch.append(pair)
    return batch_list

def get_vec(word,session):
    return session.run(embeddings[word_index_dic[word]])

def __dis(vec1, vec2):
    dis = 0.0
    for i in range(0,len(vec1)):
        dis+=math.pow((vec1[i]-vec2[i]),2)
    return dis

def get_cos_similarity(vec1, vec2):
    vec1_leng=0
    for value in vec1:
        vec1_leng+=(value*value)
    vec1_leng=math.sqrt(vec1_leng)
    vec2_leng=0
    for value in vec2:
        vec2_leng+=(value*value)
    vec2_leng=math.sqrt(vec2_leng)
    product=np.dot(vec1,vec2)

    return product/(vec1_leng*vec2_leng)

def __sim(vec1, vec2):
    return (1 - math.acos(get_cos_similarity(vec1,vec2)) / math.pi)


def find_cloest_word(word_set,session,target_word):
    sim = 0.0
    vec1 = get_vec(target_word,session)
    result = ''
    for word in word_set:
        if word == target_word:
            continue
        vec2 = get_vec(word,session)
        tmp_sim=__sim(vec1, vec2)
        print('%s : %s : %s' %(target_word,word,tmp_sim))
        if tmp_sim>sim:
            sim = tmp_sim
            result = word
    return result

text =['歐幾 里         西元前   三世   紀的   古希臘   數學家       現在     認為     幾何   之父       此畫   拉斐爾     作品       雅典   學院       數學         利用   符號語言   研究   數量       結構       變化     空間     概念     一門   學科         某種   角度看   屬     形式   科學     一種       數學   透過   抽象化     邏輯   推理     使用       計數       計算       數學家   拓展     概念         數學   基本概念     完善       早     古埃及           古希臘           嚴謹     處理                 數學     發展     持續   不斷     小幅   進展       世紀     文藝   復   興 時期       致使   數學     加速   發展       直至   今日       今日       數學   使用         領域   中       包括   科學       工程       醫學       經濟學     金融   學等         時亦會   激起   新     數學   發現       導致   全新   學科     發展       數學家     研究   純數學         數學       實質性   內容             實際   應用     目標         許多   研究   以純   數學             過程   中     發現   許多   應用   處       詞源       西方   語言   中       數學       一詞   源自     古希臘 語         其有       學習       學問       科學       數學   研究             語源           形容   詞       意思           學習           用功         亦           指       數學             英語   中   錶 面       複   數   形式           法語   中     錶 面   複   數   形式       可溯     拉丁文     中性   複   數         西塞羅   譯自 希臘文   複   數         希臘語     亞里士多德   拿來   指       萬物 皆數         概念       漢字   表示         數學       一詞     產生     中國   宋元   時期       多指   象數   之學           時     含有   今天       數學   意義             秦九韶         數學   九章       永樂   大典       數書   九章           宋代   周密   所著         癸   辛雜識       記   爲       數學         數學   通軌       明代   柯尚   遷著       數學   鑰       清代   杜知   耕著       數學 拾   遺       清代   丁取忠   撰       直到         中國   數學 名   詞   審查   委員會   研究       算學       數學       兩詞     使用   狀況   後       確認         數學       表示   今天   意義     數學   含義       歷史       奇普       印加   帝國 時     使用     計數   工具       瑪雅   數字       數學   有著   久遠     歷史       中國   古代     六藝             數學   一詞     西方     希腊 語   詞源       mathematik   ó   s       意思         學問     基礎       源於       m   á   thema       科學       知識       學問       時間     長   短     抽象     數量 關   係         時間   單位     日       季節     年         算術       加減   乘除         自然而然   產生         歷史     曾     過許         記數   系統         最初     歷史   記錄             瞭解   數字 間   的關   係           測量   土地             預測   天文   事件     形成         結構       空間     時間   方面     研究               世紀       算術       微積分     概念       此時   形成         數學   轉向   形式化       從古   至今       數學     一直   不斷     延展           科學     豐富     相互作用           發展     受惠             歷史         許多   數學   發現         直至   今日     不斷       新     發現         mikhail       sevryuk         月     期刊   中   說       數學   評論     創刊   年份       現已   超過     一百九十   萬份         每年     增加   超過   七萬   五千   份       形成       純數學     應用   數學   美學       牛頓       微積分     發明者             涉及   數量       結構       空間     變化     方面     困難   問題   時           往往     拓展     數學     研究   範疇             數學     運用       貿易       土地   測量       後     天文   學       今日         數學     亦   給出     許多     問題       牛頓     萊布尼茲     微積分     發明者       費曼   發明     費曼 路徑   積分       這是   推理     物理   洞察   二者     產物         今日     弦   理論   亦   引申   出新     數學       一些   數學   只     生成       領域               解答     領域         問題           成為       數學   概念               最純         數學   通常   亦     實際     用途       此一   非比   尋常     事實       年 諾貝爾   物理   獎   得主   維格納 稱         如同     數的   研究   領域       主要     分歧     純數學     應用   數學         應用   數學           分成   兩大   領域         變成           學科       統計學     電腦   科學       許 多數   學家   談論   數學         優美       其內       美學   美       簡單       一般化       即為   美的   一種         亦   包括   巧妙     證明             加快   計算     數值   方法         快速   傅立葉   變換       高   德菲       哈羅德       哈代         一個   數學家     自白       符號       語言     精確性         現代     符號   中       此一圖     產生     x       cos       arccos       sin   〡       arcsin       cos   〡       世紀 後     發明           在此之前       數學   文字     形式   書寫         這種   形式     限制     數學     發展         初學者   卻         望而卻步               壓縮       少量     符號   包含     大量     訊息       如同   音樂   符號         現今     數學   符號     明確     語法         有效     訊息 作   編碼       這是     書寫   方式   難以   做到         符號化     形式化     數學   迅速   發展       數學   語言   亦     初學者     感到   困難       亦   困惱     初學者         開放         字     數學 裡       特別     意思       數學 術語   亦   包括           胚       可積性       等專   有名   詞       數學   需要     日常   用語         精確性       嚴謹           現實   應用   中       定理       希臘   人期   許著   仔細     論證           牛頓     時代         使用     方法   則較     嚴謹       牛頓     瞭解   決 問題     做     定義       今日         大量     計算   難以   被驗   證時       證明   亦     難   說     足夠     嚴謹       公理     傳統     思想   中是       不證   自明     真理         這種   想法       問題           形式         公理     一串   符號         依據   哥德   爾     完備   定理       儘               意義 下       數學 作     科學       卡爾       弗里德里希       高斯       卡爾       弗里德里希       高斯   稱數   學為       科學     皇后         拉丁   原文         德語       對應         科學         單字     意思   皆     知識       領域         實際         科學         認為   科學     只   指   物理     世界   時       數學         至少     純數學           一門   科學       愛   因斯   坦曾     描述       數學   定律   越     現實           越     確定             確定     話           現實   越                 卡爾       波普爾 所定   義的   科學               年代   時         波普爾   推斷       大部份     數學   定律         物理     生物   學         假設   演繹           它現           接近                 思想家       如較   著名     拉   卡托斯         一觀   點則       科學   領域       理論   物理           公理   嘗試     符合   現實     數學       而事   實上       理論   物理   學家   齊曼       john       ziman         認為   科學     一種   公眾   知識         亦   包含   數學             情況   下       減輕     數學     使用   科學   方法     缺點         史蒂芬       沃爾夫   勒姆       年     著作       一種   新科   學       中     提出       數學家         態度   並不   一致                 哲學家         低估     美學   方面     重要性         創造       藝術               發現       科學         爭議       大學   院系   劃分   中   常見       科學     數學系       實際             細節     卻     分開       數學       領域       有如   反映     中國 算盤                   瞭解   數字 間   的關   係       測量   土地     預測   天文   事件       四種   需要         數量       結構       空間     變化       算術       代數       幾何     分析         數學   廣泛     子   領域   相關   連著         上述   主要     關 註   之外         邏輯         集合         基礎           科學     經驗       數學       應用   數學           近代       不確   定性     嚴格   研究       基礎     哲學           闡明   數學   基礎         研究     一架   構             數學   邏輯           現代 邏輯     分成   遞歸論       模型   論和證   明論       千禧年   大獎   難題   中     p       px       px       數學   邏輯       集合         範疇           數學       數量       數量     研究   起於數       孿生   質數   猜想     哥德巴赫猜想       當數系   更進   一步   發展   時       整數     視為   有理   數的   子集         有理   數則   包含     實數   中       連續     量         實數     表示         實 數則       進   一步   廣義   化成   複   數         自然   數亦     推廣   超限   數         形式化     計數     無限     這一   概念         一個   研究     領域     大小       阿列   夫數       自然   數       整數       有理   數       實數       複   數       結構         物件     結構   性質     探討     群       zh       cn       zh       tw         抽象   系統   中       該些   物件   事實             系統       此為   代數     領域             一個     重要     概念         廣義 化     向量   空間     向量           線   性 代數   中     研究       數量       結構     空間         變化         數學         研究   抽象   結構     理論       結構       布爾   巴基   學派   認為         三種       抽象   結構       代數   結構       序   結構       偏序       全序       拓撲   結構       鄰域       極限       連通性       維數       px       px       px       px       數論       群論       圖論       序 理論       空間       空間     研究   源自     幾何       尤其     歐幾裡得   幾何       三角   學則   結合     空間   及數         包含     著名     勾股定理       非歐   幾里     幾何       及拓   撲學       數和 空間     解析   幾何       結合     數和 空間     概念       亦     著拓   撲   群     研究       結合     結構     空間       李群         研究   空間       結構     變化           許多   分支   中         包含     存在   已 久     龐加萊   猜想           爭議     四色   定理       龐加萊   猜想   已         年   確認     俄羅斯   數學家   格裡   戈里       佩雷爾曼   證明         四色   定理   已         年   由凱   尼斯       阿佩爾     沃夫岡       哈肯   電腦   證明                   人力   來驗   證過       px       px       px       px       px       px       幾何       三角   學       微分   幾何       拓撲學       zh       cn       分形       zh       tw       碎形       測度論       變化         微積分       研究   變化     有利   工具       函數   誕生           做     描述   變化     量     核心   概念         複   分析   則為   複   數的     價 領域       黎曼   猜想       數學   最       未決   問題         便是     複   分析     描述         泛函   分析   註 重     函數             無限 維       空間           這在   微分方程   中     研究       px       px       px       px       px       px       微積分       向量分析       微分方程       動   力系   統       混沌   理論       複   分析       離散   數學         包含       計算 理論       計算   複   雜   性理   論及   資訊 理論         包含   現知   最   有力     模型       圖靈機       儘     電   腦   硬   體     快速   進步       最   後             壓縮     熵     概念         一相       新     領域       離散   數學     許多       未解   問題         最   有名       p       np   問題       千禧年   大獎   難題           相信     問題     解答     否定         px       px       px       組合   數學       計算 理論       密碼學       圖論       應用   數學       工商   業       領域       現實   問題       應用   數學   中       重要   領域     統計學       分析     預測       大部份     實驗             覺得     合作   團體     一份   子       數值   分析   研究     計算   方法       file       gravitation       space       source       png       數學   物理       file       svg       數學   流體   力學       file       composite       trapezoidal       rule       illustration       small       svg       數值   分析       file       maximum       boxed       png       最佳化       file       two       red       dice       svg       概率論       file       oldfaithful       png       統計學       file       market       data       index       nya       on       utc       png       計量   金融       file       arbitrary       gametree       solved       svg       zh       tw       賽局   理論       zh       cn       博弈論       file       front       pareto       svg       數理   經濟學       file       signal       transduction       pathways       zh       cn       svg       生物   數學       file       linear       programming       example       graph       zh       png       作業   研究       file       simple       feedback       control       loop       svg       控制         數學   獎項       菲爾   茲   獎牌   正面       數學 獎   通常       科學     獎項   分開       數學     最   有名     獎為   菲爾 茲獎       創立           四年   頒獎   一次       創立             頒獎     特定     工作   主題       著名           問題       稱為   希爾伯特           問題       年   德國   數學家   大衛       希爾伯特     提出         一新     七個   重要   問題       稱為   千禧年   大獎   難題       發表               一個   問題       黎曼   猜想         希爾伯特     問題   重   複       菲爾   茲獎         四年   頒獎   一次       頒       卓越貢獻     年輕   數學家       每次   最多四人   得獎       得獎者   須       年   元旦   前   未滿   四十歲         年   輕數   學家     獲得     最大   獎項             加拿大   數學家   約翰       查爾斯       菲爾   茲     要求   設立         菲爾   茲   獎     視為       數學       界     諾貝爾獎       沃爾夫   獎         沃爾夫   基金會   頒發         基金會         年     以色列   創立       年     頒獎       創始人   里卡多       沃爾夫     外交家       實業家     慈善家       阿貝爾   獎       每年   頒發   一次         紀念       年   挪威   著名   數學家   尼爾斯       亨利   克       阿貝爾   二百   周年   誕辰       挪威政府   宣佈       頒發   此種   獎金       獎金     數額       諾貝爾獎   相近       年   挪威政府   撥款       億   挪威克朗     啟動資金       擴大   數學     影響       參見       數學   哲學       數學 遊戲       數學家   列表       教育       算經十書       數學   競賽       數學題       註   記       參考書目       benson       donald       the       moment       of       proof       mathematical       epiphanies       oxford       university       press       usa       new       ed       edition       december       isbn       boyer       carl       history       of       mathematics       wiley       edition       march       isbn       concise       history       of       mathematics       from       the       concept       of       number       to       contemporary       mathematics       courant       and       robbins       what       is       mathematics       an       elementary       approach       to       ideas       and       methods       oxford       university       press       usa       edition       july       isbn       davis       philip       and       hersh       reuben       the       mathematical       experience       mariner       books       reprint       edition       january       isbn       gentle       introduction       to       the       world       of       mathematics       eves       howard       an       introduction       to       the       history       of       mathematics       sixth       edition       saunders       isbn       gullberg       jan       mathematics       from       the       birth       of       numbers       norton       company       st       edition       october       isbn       an       encyclopedic       overview       of       mathematics       presented       in       clear       simple       language       hazewinkel       michiel       ed       數學   百科   全書       kluwer       academic       publishers       translated       and       expanded       version       of       soviet       mathematics       encyclopedia       in       ten       expensive       volumes       the       most       complete       and       authoritative       work       available       also       in       paperback       and       on       cd       rom       and       online       jourdain       philip       the       nature       of       mathematics       in       the       world       of       mathematics       james       newman       editor       dover       isbn       kline       morris       mathematical       thought       from       ancient       to       modern       times       oxford       university       press       usa       paperback       edition       march       isbn       牛津   英語   詞典       second       edition       ed       john       simpson       and       edmund       weiner       clarendon       press       isbn       the       oxford       dictionary       of       english       etymology       reprint       isbn       pappas       theoni       the       joy       of       mathematics       wide       world       publishing       revised       edition       june       isbn       peterson       ivars       mathematical       tourist       new       and       updated       snapshots       of       modern       mathematics       owl       books       isbn       參考   網址       rusin       dave       the       mathematical       atlas       英文版       現代   數學   漫游       weisstein       eric       world       of       mathematics       一個   在線     數學   百科全書       數學         一個   在線     數學   百科全書       mathforge       一個   包含   數學       物理       epistemath       數學知識       香港科技大學       數學網       一個     數學史   為主     網站         研習   純數學       或統   計學       本科     基礎   研究   課程   參考   書目       數學   文化       主要   面向   大學生       大學老師     研究生         中學老師     學生       數學   學習   資源       互聯網     數學   學習   資源     教學   視頻       英漢   對照   數學   用語       archive       英漢   對照   數學   用語       albany       bureau       of       bilingual       education       see       profile       at       archive ']
window_size = 5
embedding_size = 5
num_sampled = 3

if __name__ == '__main__':
    context_pair=[]
    word_set = set()

    for sentence in text:
        tokens = sentence.lower().split(' ')
        context_pair += get_context(tokens,window_size)
        tmp_word_set = __get_word_set(tokens)
        for word in tmp_word_set:
            word_set.add(word)
    word_index_dic,inverse_word_dic=__get_word_index(word_set)
    word_size = len(word_set)
    batch_size = len(context_pair)
    inputs = [word_index_dic[x[0]] for x in context_pair]
    labels = [[word_index_dic[x[1]]] for x in context_pair]

    train_inputs = tf.placeholder(tf.int32, shape=[batch_size])
    train_labels = tf.placeholder(tf.int32, shape=[batch_size, 1])
    embeddings = tf.Variable(
        tf.random_uniform([word_size, embedding_size], -1.0, 1.0))
    embed = tf.nn.embedding_lookup(embeddings, train_inputs)
    nce_weights = tf.Variable(
        tf.truncated_normal([word_size, embedding_size],
                            stddev=1.0 / math.sqrt(embedding_size)))
    nce_biases = tf.Variable(tf.zeros([word_size]))

    loss = tf.reduce_mean(
        tf.nn.nce_loss(weights=nce_weights,
                       biases=nce_biases,
                       labels=train_labels,
                       inputs=embed,
                       num_sampled=num_sampled,
                       num_classes=word_size))

    optimizer = tf.train.GradientDescentOptimizer(learning_rate=1.0).minimize(loss)
    session = tf.Session()
    init = tf.global_variables_initializer()
    session.run(init)
    for iteration in range(0,10000):
        total_loss = 0

        feed_dict = {train_inputs: inputs, train_labels: labels}
        _, cur_loss = session.run([optimizer, loss], feed_dict=feed_dict)
        print('%s: loss: %s' %(iteration,cur_loss))
    print(find_cloest_word(word_set,session,'數學'))

