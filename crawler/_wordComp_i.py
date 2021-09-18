# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20191119
############################
#
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np
import math
import imutils
import sys
import mysql.connector
import re
import shutil
from _dict_meaning import wordmeaning
from _dict_pic import *
from _dict_pinyin_offline import pinyin
import json
import time

localtime_init = time.asctime( time.localtime(time.time()) )

#connect to database
#tmarkdb = mysql.connector.connect( host = "127.0.0.1", user = "root", password = "lehsiao", database = "tmarkdb",  )
#cursor=tmarkdb.cursor()
#cop = re.compile("[^.^/^A-Z^a-z^0-9^-]")
#cop = re.compile("[^\u4e00-\u9fa5^A-Z^a-z^ ^]")
cop = re.compile("[^\u4e00-\u9fa5^]")
copNo = re.compile("[^0-9^]")
word1 = sys.argv[1]
word2 = sys.argv[2]
codeClass = "0" + copNo.sub('', str(sys.argv[2]))[0:2]
string = ""
index = sys.argv[4] 
if word1.find("及圖") > 0:
    word1 = word1[0:word1.find("及")]
elif word1.find("及") > 0 and word1.find("標章") > 0:
    word1 = word2[0:word1.find("及")]
elif word1.find("及") > 0 and word1.find("標章圖") > 0:
    word1 = word1[0:str(word1).find("及")]
elif word1.find("及") == -1 and (word1.find("圖") ==-1 and word1.find("標章") == -1 and word1.find("標章圖")==-1):
    word1 = word1
elif word1.find("及") == -1 and (word1.find("圖") > 0 or word1.find("標章") > 0 or word1.find("標章圖") > 0):
    word1 = "-"
    
if word2.find("及圖") > 0:
    word2 = word2[0:word2.find("及")]
elif word2.find("及") > 0 and word2.find("標章") > 0:
    word2 = word2[0:word2.find("及")]
elif word2.find("及") > 0 and word2.find("標章圖") > 0:
    word2 = word2[0:str(word2).find("及")]
elif word2.find("及") == -1 and (word2.find("圖") ==-1 and word2.find("標章") == -1 and word2.find("標章圖")==-1):
    word2 = word2
elif word2.find("及") == -1 and (word2.find("圖") > 0 or word2.find("標章") > 0 or word2.find("標章圖") > 0):
    word2 = "-"
    
if codeClass == "001":
    string = "化學、合成、氣體、催化、資源、精肥、螯合、化合物、未加工、有機土、純竹炭、添加劑、通用型、營養液、農業生技、過濾材料、複合元素、環保節油劑、BIOCHEMICAL、CARBON、CATALYST、CHELATE、CHEM、CHEMICAL、CHEMISTRY、CLEANER、COATING CHEMICAL、COMPOUND、DIESEL TREATMENT、ELEMENT、ENERGY、ENZYME、GLUE、POLYMERS、LIQUID、MEMBRANE、MICROBE、NATURAL ORGANIC LIQUID FERTILIZER、OIL SYSTEM、PREPARATION、RESOURCES、SOIL、SYNTHESIS"
elif codeClass == "002":
    string = "建材、彩繪、噴砂、透明漆、COLORANT、DYESTUFF、PAINT、PATCH、RUST、VARNISH"
elif codeClass == "003":
    string = "油、炭、香、膏、肌膚、皂物、防曬、亮顏、保濕、炫色、美甲、美白、美妝、美睫、香氛、香品、茶浴、草本、彩妝、煥白、煥膚、嫩白、緊實、蒸氣、裸妝、髮泥、髮舖、髮藝、凝露、雙效、修復露、無瑕透白、美髮沙龍、AGE、AIRBRUSH、AROMA、BEAUTY、BEAUTY LAB、BODY、BODY CARE、BOTANIC、BOTANICAL、CARE、CLEANSING、CLEAR、COMPACT、COOL GEL、CREAM、DEODORANT、DETERGENT、ESSENCE COLLECTION、ESSENTIAL OIL、FRAGRANCE、GEL、GENTLE、HAIR、HAIR CENTER、HAIR EXPERT、HAIR SALON、HANDMADE SOAP、INCENSE、MAKE UP、MAKE-UP STUDIO、MILK、MOIST、OIL、PET、PROTEIN、Q10、RELAX、SKIN、SKINCARE、SPA、SPF(+防曬系數) 、SPRAY、UV、VEIL、WASH"
elif codeClass == "004":
    string = "油品、照明、水素化、高性能技術、CHEM、ENERGY、ILLUMINATING、LIGHTING、RACING、SPEED、TRANSMISSION"
elif codeClass == "005":
    string = "丸、丹、液、散、貼、酵、錠、好菌、益菌、高鈣、滋養、順暢、漢方、製藥、輕食、膠原、膠囊、蔘藥、複方、凝膠、機能、營養、一條根、益生菌、植物性、生機飲食、保健食品、草本精華、健康主張、御醫漢方、膠原蛋白、Ｃ片、BIO PHARMA、BIOTECHNOLOGY FOODS、CALCIUM、CAPSULE、CARE、CHINESE MEDICINE、CURE、DERMA、DIET、DNA、DRUG、FLUID、FORMULA、GEL、GENE、HERBACEOUS PLANT、HERBAL、HYGIENE、LUTEIN、MEDICINE、NUTRITION、NUTRITIONAL、OMEGA-3、PELLET、PHARMA、PHARMACEUTICAL、PILL、PLASTER、POWDER、PREPARATION、Q10、TABLET THERAPEUTIC、TONIC、VANILLA"
elif codeClass == "006":
    string = "耐震、氣密、密封、補強、隔震、擠型、鑄造、高安全性、AIR-TIGHT、ANTI-SHOCK、CAST／CASTING、HIGH SECURITY、REINFORCE"
elif codeClass == "007":
    string = "氣動、傳動、電動、鑄造、機器人、AIR、COATING、CUT、DRIVE、ELECTRONIC、FORGE、GEAR、IC、MACHINERY、MILL、REFRIGERATION、ROBOT"
elif codeClass == "008":
    string = "工具、美甲、髮藝、AUTO TOOLS、BARBER、CUTTING、GRIP、HAIR CUT、SET 、TOOLS"
elif codeClass == "009":
    string = "卡、手遊、支付、包膜、行動、串流、保全、桌遊、移動、測量、無線、視光、感知、載體、電氣、精準、劇院、影音、超高清、機器人、虛擬實境、視聽音響、電訊聯盟、數位音頻、4K、AC、ACOUSTIC、ACTIVE、APP、AR、AUDIO、CAD、CAM、CAP、CARD、CHANNEL、CYBER、DC、DRIVE、ELECTRONIC、FILE MANAGER、GPS、HD、IC、INSTRUMENTS、INTERFACE、IP、LASER、LED、MEASUREMENT、MEMORY、MICROELECTRONIC、MOBILE、MODULE、MR、MUSIC、ON WEB、OPTICAL、PAD、PAY、PHONE、PLASMA、PLATFORM、POWERS、PROGRAM、RADIO、RAM、ROBOT、ROM、SAFE、SCREEN PROTECTOR、SEARCH、SERVER、SHARE、SIM、SOLAR、SOLAR POWER、SOUND、SRAM、STREAM、SWITCH、TELECOM、THEATER、TV、VIRTUAL REALITY、VISION、VR、WAVE"
elif codeClass == "010":
    string = "植牙、電位、機器人、情趣用品、ACUPUNCTURE、BONE、CARE、DENTAL、DIAGNOSTIC、ELECTRICAL、HEAT THERAPY、HOMECARE、IMPLANT、INSTRUMENT、LASER、MAGNETISM、MASSAGER、MEDICAL、MEDICAL PRODUCTS、METER、OPTIC、ORTHOPEDIC PRODUCTS、ORTHOPEDICS、PAD、PRESSURE THERAPY、PROSTHETIC、PROTECT、PULSE、ROBOT、SAFETY、SHIATSU、SUPPORTS、THERAPEUTICS、VEIN"
elif codeClass == "011":
    string = "光能、空調、活水、淨水、照明、節能、蒸氣、衛浴、變頻、AIR、AQUA、BRIGHT、CHEF、COOL、FROZEN、GAS、H.I.D.、ILLUMINATED、LIGHTING、PURIFY、REFRIGERATION、SOLAR、SOLAR POWER、SPA、WATER、WATER SAVE"
elif codeClass == "012":
    string = "小折、小摺、車業、省油、動力、太陽能、全地形、電動的、四輪傳動、懸吊系統、ATV、AUTO、AUTOMOTIVE、AVIATION、BIKE、CYCLE、CYCLING、DRIVE、ELECTRONIC、FORGED、GEAR、GENUINE、GOLF、HYBRID、KIDS、LED、MOBILE、MOTOR、OFF-ROAD、OUTDOOR、POWER、RACING、RACING SPEED、RV、SOLAR、SPEED、SPORT、SUSPENSION、SUV、TOOLS、TURBO、VIEW"
elif codeClass == "013":
    string = "防狼、火力強、EXPLODE、EXPLOSIVE"
elif codeClass == "014":
    string = "金飾、純金999、精準、銀樓、金仔店、BEAD、BEAUTY、CRYSTAL、EXCLUSIVE、GEMOLOGY、GEMSTONE、GOLDEN、JEWEL、JEWELLERY、TREASURE、ZIRCONIA"
elif codeClass == "015":
    string = "音樂、管樂、爵士、音樂館、打擊樂團、音樂學校、數位音樂中心、音樂教育系統、音樂文化教育機構、GOOD SOUND、GUITAR STUDIO、JAZZ、JAZZY、MUSIC、MUSICAL EDUCATION OBJECT、PERCUSSION、STRINGS"
elif codeClass == "016":
    string = "卡、袋、報、膜、文具、文理、日報、日語、月刊、出版、包裝、快訊、快報、美語、英文、時報、書局、書法、紙紮、教育、教室、週刊、黃頁、電玩、網咖、製作、數學、樂透、親子、書畫室、腦力開發、BAG、BINDERY、BOOKSTORE、CARD、DAILY、DIGEST、EDUCATION、ENGLISH、JOURNAL、LEARNING、MONTHLY、PACKAGE、PAPER、PHOTO、PRESS、PRINT、PRINTING、PUBLISHING、SEAL、STATIONERY、TICKET、WEEKLY、WRAPPING"
elif codeClass == "017":
    string = "酯、吸音、黏彈性、ACOUSTIC、TPU、VISCOELASTIC"
elif codeClass == "018":
    string = "杖、袋、箱、皮件、皮飾、寵物、CLOTH、COVER、FUNCTIONAL、HOLDER、JEAN、PET、SKIN、STICK、STRAP"
elif codeClass == "019":
    string = "耐震、補強、隔震、ANTI-SHOCK、REINFORCE、SAND"
elif codeClass == "020":
    string = "名床、家居、傢飾、寢飾、實木、廚飾、系統傢俱、精緻名床、BEDDING、BOARD、CASA、FITMENT、FURNITURE、HOME COLLECTION、HOUSEHOLD、INFANT、MATTRESS、PALLET、SLEEP、SYSTEM FURNITURE、WARE"
elif codeClass == "021":
    string = "生活、咖啡、美甲、家居、琉璃、彩妝、清潔、陶瓷、廚房、窯燒、鍋物、家庭用具、廚房用具、CHEF、CHINA HOUSE、CHINAWARE、COFFEE、COOL、COSMETICS、CRYSTAL、DRINK、KITCHENWARE、WASHER"
elif codeClass == "022":
    string = "帶、篷、紗網、紡織品、BAND、CHARCOAL、TAPE、TENT"
elif codeClass == "023":
    string = "炭、麻、羊毛、織品、纖維、紡織品、嫘縈織物、FABRIC、FIBERS、FLEECE、HEMP、NYLON、RAYON、SILK、WOOL"
elif codeClass == "024":
    string = "絨、絲、尼龍、竹炭、羊毛、乳膠、家居、紡織、寢具、寢飾、睡眠、製棉、編織、蕾絲、織物、炭元素、備長炭、創意家飾、精緻名床、寢具生活館、睡眠生活館、BEDDING SET、CLOTH、COOL、DECORATION、FABRIC、HOME CARE、HOME COLLECTION、KNITTING、LACE、LASTING、LATEX、NYLON、PEVA、SATEEN、SCREEN、SILK、SLEEPING、SPINNING、WEAVE、WOOL"
elif codeClass == "025":
    string = "麻、棉、絲、羊毛、服飾、速乾、塑身、團服、ATHLETIC、CLOTH、COTTON、DENIM、DRESS、FABRIC、GEAR、JEANS、LINEN、RAYON、SILK、SPORT、UNIFORM、WEAR、WOOL、YARN"
elif codeClass == "026":
    string = "扣、針、帶、絲、鉤、飾品、BAND、BEADS、DARN、EMBROIDERY、HAIR、HOOK、ORNAMENT、SEWING、SNAP"
elif codeClass == "027":
    string = "炭、竹炭、瑜珈、BAMBOO、PE、YOGA"
elif codeClass == "028":
    string = "卡、盒、手遊、娃娃、桌遊、密技、瑜珈、遊戲、運動、體操、體育館、虛擬實境、BIKE、BOARD GAMES、BOXING、CARD、DANCING、DART、DRIVE、GAME、GOLF、INFANT、MOTORSPORT、OUTDOOR、PETS、PLAY、PLAYING FIELD、ROBOT、SPORT、SPORTS、SURFER、VIRTUAL REALITY、VR"
elif codeClass == "029":
    string = "肽、湯、酵、元素、水產、生鮮、冰鎮、串燒、厚切、厚片、厚燒、活菌、益菌、茶事、茶油、酒食、現熬、順暢、漢方、機能、燉品、燒烤、肉脯店、香 QQ、麻辣燙、低溫殺菌、烘焙美食、高纖順暢、黃金泡菜、BAKER、BBQ、BIOTECHNOLOGY FOODS、BRUNCH、DIETARY、FLAVOR COATED、FRAGRANCE、FROZEN、HERBACEOUS PLANT、HONEY、NUTRITION、SANDWICHES、SEAFOOD、SPARKLING、STEAK、VEGETARIAN FOODS、XO、YOGURT"
elif codeClass == "030":
    string = "味、香、脆、茗、酥、辣、酵、燒、饌、お茶、二代、上純、川味、手工、手烘、手搖、日式、外賣、奶香、甘醇、生酮、冰室、冰鎮、多酚、好米、好食、百草、百菓、老茶、西點、串燒、夾心、快餐、佳釀、呷茶、呷涼、果香、油切、法式、空廚、長秈、厚切、厚燒、研磨、美式、美饌、香Ｑ、香茗、凍頂、凍飲、泰式、烘培、素食、茗品、茗茶、茶王、茶事、茶油、茶舍、茶品、茶苑、茶宴、茶庵、茶集、茶飲、茶道、茶點、茶禮、酒食、御廚、御膳、現烤、陳年、麻辣、焙茶、無糖、發酵、粥品、菓子、新茶、義式、蜀味、補給、農法、零食、漢方、碳烤、精釀、製粉、製茶、製菓、製麵、輕飲、樟芝、穀香、窯烤、蔗香、養身、燒烤、燜燒、優糧、薄燒、鮮味、鮮果、點心、一口酥、三合一、天然ㄟ、功夫茶、台灣餅、四物飲、私房菜、芋冰城、味一番、咖啡棧、活力菌、活性菌、活性酶、家鄉味、純黑糖、茶博館、清心茶、陳年釀、植物派、減脂茶、葉黃素、零度C、養生粥、養生鍋、醍醐味、纖體素、手釀原液、日本料理、台灣料理、自家烘焙、自家製麵、忠於原味、活力元氣、活性元素、美食天地、原味燒烤、烘焙美食、祖傳名產、茶色茶香、迴轉壽司、健康主張、健康總匯、專業烘焙、甜而不膩、傳統美食、葡式蛋撻、調味專家、養蜂農場、營養強化、禮餅專家、懷石料理、西點麵包店、純古法釀造、義大利風味、自然生態農場、BAKERY、BAKING、BBQ、BEANS、BEVERAGE、BIOTECHNOLOGY FOODS、BLEND COFFEE、BRUNCH、BURGER、CAFE、CHA、CHIP、COFFEE FARM、CONFECTIONARY、COOKED、COOL、CURRY、DESSERT、DHA、DIET、DIETARY、DRINK、FOODS、FRESH FRUIT、FRUIT、GOURMET、HEALTHY CARE、HERBACEOUS PLANT、HERBAL、HONEY、ICE SHOP、JAPANESE FOOD、KUNG FU TEA、MEAL、NATRUAL HEALTH、NATURAL CHOICE、PASTA、PIE、RAMEN、ROASTER、SABU、SHABU、SMOKY、SOFT、SPARKLING、SUSHI、TAIWANESE CUISINE、TEA、THREE IN ONE、TRI IN ONE、VANILLA、YUMMY"
elif codeClass == "031":
    string = "花市、花店、高冷、超大、園藝、溫室、鮮切、鮮味、鮮果、寵物、蘭園、蘭藝、野菜村、水族量販、休閒農場、活蝦之家、農特產品、綠色生機、FRESH FRUIT、FRESH GARDEN、GARDENING、HERBACEOUS PLANT、PETFOOD、TROPICAL"
elif codeClass == "032":
    string = "酵、冰泉、冰鎮、好水、保鮮、活水、凍飲、純水、酒食、淨水、飲料、精釀、鍺水、檸檬、大悲水、六角水、甘露水、果汁吧、活氧水、纖果粒、ALOE、BEVERAGES、BREWERY、BREWING、BRUNCH、COLLAGEN、DRY、ENERGY、ENZYME、FOODS、FRESH JUICE、HERBACEOUS PLANT、JUICE BAR、LIGHT、MALT、MEDIUM-DRY、MINERAL、NATURAL HEALTH、NON-ALCOHOLIC、OXYGEN、O2、PURE WATER、Q10、SEA WATER、SEMI-DRY、SPARKLING、STRAWBERRY、WINEMAKER"
elif codeClass == "033":
    string = "醇、古酒、冰鎮、名酒、酒場、酒窖、酒廠、酒藏、窖藏、精釀、蒸餾、釀製、長壽酒、葡萄園、陳年老酒、越陳越香、酒精濃度（38度）、ALCOHOLIC DRINKS、ALCOHOLIC BEVERAGES、BREWERY、BREWING、CASK、CELLAR、DISTILLED、DRY、HERBACEOUS PLANT、MEDIUM-DRY、SEMI-DRY、SINGLE MALT、SPARKLING、VANILLA、VINEYARD、WINE CELLAR、WINE HOUSE、WINEMAKER、WINERY"
elif codeClass == "034":
    string = "菸酒、慢燃、濃煙、活性碳、手工煙斗、DENSE、FILTER、RIPENED TOBACCO、SLIMS、SMOKING"
elif codeClass == "035":
    string = "水產、市場、夜市、花店、建經、量販、會展、網購、藥粧、人文館、名品城、百貨店、伴手禮、金仔店、人力銀行、生活工坊、生活百貨、國際貿易、就業情報、線上購物、親子購物、3C、AD.、HR、BIG SALE、BUY、CONSULT、CONSULTANT、DISTRIBUTION、EXHIBITS、MANPOWER、MERCHANT、PAY、POINTS、PRODUCE、PROMOTIONS、SHOPPING"
elif codeClass == "036":
    string = "人壽、公寓、日租、比價、地產、房屋、法拍、金流、金融、致富、財富、基金、理財、產物、產險、票券、眾籌、票券、資本、權證、投資銀行、物業管理、國際地產、產物保險、理財金三角、BROKER、CAPITAL PARTNERS、CROWD FUNDING、EXCHANGE、FINANCIAL、FINANCIAL SOLUTIONS、FUND、FUTURES、INCUBATOR、INTERNATIONAL PROPERTY、INVESTOR、LOAN、PAY、REALTY、REWARDS、RISK MANAGEMENT、SECURITY、STOCK、TAX、WEALTH MANAGEMENT"
elif codeClass == "037":
    string = "包膜、快修、速修、造景、景觀、節能、鋼構、自助洗車、車體美容、室內裝修、維修中心、ARCHITECT DEVELPOMENT、ARCHITECTURE & INTERIOR、AUTO SERVICE、AUTOMOTIVE BEAUTY、BUILDER、CAR BEAUTY、CAR SPA、DECO、DEVELPOMENT、HOUSING"
elif codeClass == "038":
    string = "報、有線、副刊、移動、報導、無線、新聞、漫遊、網聯、寬頻、數據、頻道、旅遊台、部落格、電視台、人造衛星、行動上網、電訊聯盟、數位行動通訊、4G、5G、BLOG、CABLE、CALL、CHANNEL、CLOUD、CONNECT、GPS、HD、LTE、MOBILE、PAY、RADIO、REPORT、SIM、STREAM、TELECOM、TV、WAP、WIRED、WIRELESS"
elif codeClass == "039":
    string = "叫車、打車、壯遊、快車、快送、車隊、便利、客運、倉庫、旅行、航空、假期、商船、捷旅、速遞、無線、郵輪、遊艇、遊輪、運通、慢遊、聯運、觀光、自由行、旅遊台、迷你倉、遊覽車、衛星車隊、AIR、AIRLINE、AVIATION、CAB、CARGO、CRUISE、CRUISE LINE、GPS、HARBOUR、HOLIDAY、JOURNEY、MINI STORAGE、PARK、PARKING、RESERVATION、SHIPPING、SOLAR POWER、SPEED、TAXI、TRANSPORT、VACATION、YACHT"
elif codeClass == "040":
    string = "代工、加工、油壓、塗裝、鍍膜、CHIP、COATING、TAILOR"
elif codeClass == "041":
    string = "塾、誌、大學、才藝、戶外、手遊、文理、文藝、休閒、年會、有氧、武術、美術、美語、英文、音樂、拳擊、書法、桌遊、氣功、教室、會展、瑜珈、義塾、數學、樂園、樂團、閱讀、學舍、學校、學院、學堂、親子、戲院、賽事、藝苑、藝能、露營、人文館、出版社、合唱團、紀念館、美術館、健康館、釣蝦場、渡假村、照相館、電音節、歌舞團、舞蹈團、翻譯社、人力發展、文教機構、休閒廣場、品格教育、音樂中心、留學中心、健身中心、教育中心、教學系統、森林樂園、運動中心、運動平台、運動空間、運動訓練、語言學坊、數位學堂、藝術特區、文理補習班、學習實驗室、ABROAD、ACADEMIA、ANNUAL MEETING、ART CENTER、BAND、BOOKS、BOOKSTORE、BOXING、CAMPING、CASINO、CHOIR、DANCE、DANCE THEATRE、DRAMA、EDUCATION INSTITUTE、FESTIVAL、GOLF、LANGUAGE WORKSHOP、LEARNING LAB、LEISURE、MEMORIAL HALL、MUSIC、NATIONAL PARK、ONWEB、OUTDOOR、PROMOTIONS、PUBLISHING、RACING SPORT、TICKET、UNIVERSITY、VACATION、VIDEO、VIRTUAL REALITY、VR、YOGA"
elif codeClass == "042":
    string = "生物、研發、部落格、系統傢俱、空間創作、視覺設計、雲端計算、ANALYSIS、ARCHITECT DEVELPOMENT、ARCHITECTURE & INTERIOR、BLOG、CAD、CLOUD、CONNECT、DECO、DESIGN STUDIO、ECOSYSTEM、QUALITY ASSURANCE、UPDATE"
elif codeClass == "043":
    string = "丼、饌、小站、川味、手搖、文旅、日式、水產、火烤、主廚、外賣、民宿、全素、冰鎮、托育、托嬰、早點、行旅、行館、串燒、私廚、定食、法式、青旅、厚切、厚燒、炭燒、美式、食補、泰式、烘焙、素食、茶事、茶舍、茶室、茶庵、茶集、茶齋、酒食、御廚、御膳、捷旅、麻辣、越菜、飯包、意麵、會展、義式、蜀味、團膳、輕食、輕旅、輕飲、廚藝、熱炒、窯烤、蔬食、燒肉、燒烤、燒臘、親子、餐旅、鍋物、鍋燒、鮮味、鮮食、鮮萃、簡餐、早午餐、自助餐、宴會廳、家常菜、臭臭鍋、麻辣燙、渡假村、獨享鍋、鴛鴦鍋、麵食館、鐵板燒、自家製麵、私房美饌、青年旅館、烘焙美食、健康湯鍋、國際行館、森林樂園、渡假飯店、港式飲茶、港式燒臘、港式點心、溫泉拉麵、精品旅店、複合餐飲、懷石料理、墨西哥料理、B&B、BAKER、BAKERY、BANQUET、BBQ、BED & BREAKFAST、BRUNCH、BUFFET、BURGER、BUSINESS HOTEL、CAFÉ、CAPSULE INN、CHEF、CUISINE、CURRY、DINER、EATERY、EXPRESS HOTEL、FOOD、FOOD STAND、FRIED CHICKEN、GOURMET、GRILL、HAND-PICKED、HOME STAY、HOSPITALITY、JUICE BAR、LOUNGE、NOODLES、PIZZA、POT、ROASTER、SEAFOOD、SABU、SHABU、SHABU SHABU、SNACK STATION、SPA、STEAK、SUITE、SUSHI、TEA BAR、TEPPANYAKI、THE BAKERY、VACATION、VILLA、YUMMY"
elif codeClass == "044":
    string = "月嫂、芳療、美白、紋身、紋繡、湯屋、新秘、雷射、髮藝、醫美、超音波、微整型、養生館、整復所、醫生館、月子中心、安養中心、長照中心、紀念醫院、美容世界、專業彩妝、彩妝造型、造型團隊、創意髮型、愛犬沙龍、養護中心、寵物沙龍、藝術指甲、護髮中心、足體養生館、美容美體館、足體養生會館、健康諮詢中心、產後護理之家、AESTHETIC MEDICINE、BARBER、BEAUTY CARE、BEAUTY SPA、CARE、CLINICAL DIAGNOSTICS、DERMA、EYELASH SALON、FOOT MASSAGE & SPA、HAIR、HAIR CUT、HAIR EXPERT、HAIR SALON、HAIR STYLE、LASER、LONG-TERM CARE、MAKE UP、NAIL SPA、OPTICS、PET SALON、POSTPARTUM CARE CENTER、SHOWER、SPA、SURGERY、TATTOO、THERAPEUTICS、VET"
elif codeClass == "045":
    string = "壇、生命、宗壇、婚友、婚紗、婚禮、徵信、囍事、禮儀社、生命事業、物業管理、法律事務所、HOME CARE、WEDDING"

string00 = "上選、天然、手作、手感、手繪、平價、本草、正宗、正港、生化、生技、生態、生機、生醫、全效、名店、名物、名品、好味、有機 、老牌、技術、私房、良品、防水、典藏、奈米、納米 、長效、便宜、持久、珍品、珍藏、珍饌、科技、科學、美味、美食、訂製、原味、原創、時尚、特賞、特優、祕傳、祖傳、純粹、配方、高級、健康、專家、專業、強效、御品、御選、頂級、頂極、創新、復古、智能、絕品、超值、超級、傳承、傳統、新鮮、極品、極致、經典、道地、隔音、團購、精品、精純、精密、精華、精緻、精選、綠能、酵素、潮流、調理、養生、臻品、選物、選品、優等、優質、環保、環境、鮮作、謹製、懷舊、嚴選、五星級、加強型、古早味、正台灣、正老牌、好味道、老字號、純手工、一級棒、第一家、在地風味、在地嚴選、綠能科技、百年老店、3D、ACCESSORY、ALL IN ONE、ANTIQUE、AUTHENTIC、AUTOMATIC、BESPOKE、BEST、BIO、BIOCHEMISTRY、BIOMEDICAL、BIOPHARM、BIOTECH、BIO-TECHNOLOGY、BIOTHERAPEUTICS、CERAMIC、CLASSIC、CLAY、CLEAN、COLLECTION、DELICIOUS、DELUXE、DIY、ECO、ENVIRONMENTAL PROTECTION、EXCELLENCE、EXCELLENT、EXPERT、EXPORT、FASHION、FASHIONABLE、FINEST、FIT、FITNESS、FITTING、FRESH、FRESH MADE、GLASS、GOOD QUALITY、GREEN、GREEN TECH、HANDCRAFTED、HANDMADE、HEALTH、HEALTHY、HERB、HOMEMADE、HOMESERVICES、I CHI BAN、INNOVATION、KIDS、LEATHER、LUXURY、MATERIALS、METAL、NANO 、NATURAL、NATURAL & HERBAL、NATURE、ORGANIC 、ORIGINAL、PARTS、HEALTHY、PERFORMANCE、PLASTIC、PRECIOUS、PREMIUM、PREMIUM QUALITY、PRO、PROFESSIONAL、SCIENTIFIC、SELECT、SOLUTION、SOUND-PROOF、SPECIALTY、SUPERIOR、TECHNOLOGY、TECH、TEK、TEX、TEXTILE、TEXTURE、WATER-PROOF、WOODEN"
string01 = "匠、大師、師父、師傅、高手、專家、博士、達人、職人、醫生、王、Doctor"
string02 = "牌、工藝、手創、文創、主題、布藝、企劃、系列、系統、和風、美學、風格、設計、創意、創藝、製品、藝品、藝術、空間設計、時尚生活、創意設計、AESTHETICS、ART、ART & DESIGN、BRAND、COLLECTION、CRAFT、CREATION、CULTURAL AND CREATIVE、DESIGN、INNOVATION、INTERIOR DESIGN、LABEL、MATERIAL、PRODUCT、PRODUCTION、REDESIGN、SERIES、SPACE DESIGN、STYLE、SYSTEM"
string03 = "共購、在線、宅配、行銷、直播、連鎖、視訊、視頻、雲端、電販、網路、數位、線上、手機版、多媒體、複合式、互動媒體、行動商務、行動聯網、平台、創意行銷、電子商務、網路書店、網路商城、網際網路、數位策略、整合行銷、DIGITAL、DIGITAL STRATEGY、E-COMMERCE、ESHOP、EXPO、INTERNET、IoT、LINK、MARKETING、MEDIA、MULTIMEDIA、NET、NETWORK、ON APP、ON LINE、ONLINE、SYMPOSIUM、WEB、WIFI"
string04 = "工程、工業、五金、文化、文教、文創、生技、生醫、企業、光電、光學、全球、印刷、百貨、技研、投資、投顧、沙龍、事業、協會、房產、牧業、物流、物產、物業、金控、建設、建築、科技、食品、娛樂、展業、旅遊、書店、租車、租賃、紙業、能源、茶業、商旅、商務、商貿、商業、商辦、國際、控股、產業、通信、通訊、通運、創投、媒體、棉業、貿易、開發、集團、傳媒、傳播、會社、資訊、資產、農產、電子、電信、電訊、電商、電腦、電機、電競、團隊、實業、精機、銀行、影視、影業、影像、鞋業、機械、機電、機構、興業、餐飲、營建、營造、環球、聯合、聯盟、禮儀、不動產、多媒體、房地產、基金會、生命禮儀、生物科技、物流開發、能源科技、集團控股、管理顧問、數位通訊、應用科技、.COM、AEROSPACE、ALLIANCE、ARCHITECTURE、ASSET、ASSOCIATION、BANK、BIOTECH、BIOTECHNOLOGY、BUSINESS、CAPITAL、COMMUNICATION、CONSTRUCTION、CONSULTING、CULTRUAL CREATIVE、CULTURE、DEVELOPMENT、ELECTRIC、ENGINEERING、ENTERPRISE、ENTERTAINMENT、eSports、ESTATE、EXPRESS、EXPRESS & LOGISTICS、FACTORY、FLORIST、FOUNDATION、FREIGHT、GLOBAL、GROUP、HOLDING、INDUSTRIAL、INDUSTRY、INFORMATION、INSTITUTE、INSTITUTION、INSURANCE、INTERNATIONAL、INTERNATIONAL TRADE、INVESTMENT、LAND DEVELOPMENT、LAW OFFICE、LEASE、LOGISTIC PROPERTY、LOGISTICS、MACHINE、MANUFACTURING、MATERIAL TECHNOLOGY、METAL INDUSTRY、NEWS、OPTO、OPTOELECTRONIC、ORGANIZATION、PARTNERSHIP、PHOTOGRAPHY、PROPERTY、REAL ESTATE、RENTAL、SALON、TEAM、TECHNIC、TECHNOLOGY、TECH、TEK、TELECOMMUNICATION、TOUR、TOURISM、TRAVEL、TRIP"
string05 = "庄、行、坊、局、店、房、社、舍、亭、室、屋、苑、家、記、軒、院、堂、庵、莊、堡、場、園、號、網、樓、館、齋、小棧、小廚、小舖、小館、山莊、工坊、工房、工場、工廠、中心、天地、市集、本舖、冰城、冰站、冰舖、老店、老街、老舖、店舖、果園、果舖、牧場 、花坊、花園、客棧、洋行、食坊、食府、食堂、香舖、料亭、旅店、旅棧、書坊、書房、書城、書屋、書院、書齋、茶行、茶坊、茶社、茶屋、茶站、茶軒、茶堂、茶莊、茶棧、茶園、茶鋪、茶舖、茶館、草堂、酒坊、酒店、酒莊、酒棧、酒館、酒舖、酒樓、商行、商城、商場、商號、莊園、貨舖、魚舖、漁舖、園區、會館、當鋪、農莊、農場、農園、道院、道場、精舍、餅店、餅家、餅舖、劇場、廚坊、廚房、廣場、影城、學苑、學園、餐館、館子、講堂、藝坊、藝廊、藥局、麵屋、麵館、麵攤、工作坊、工作室、工務所、工程行、工藝坊、中藥行、手作坊、手作屋、文化館、水果店、生活館、事務所、便利店、風味館、娛樂城、娛樂場、宴會館、時尚館、桑拿屋、烘焙坊、商店街、專門店、專賣店、御膳坊、甜品屋、創始店、創藝坊、渡假莊、飲品館、實驗室、旗艦店、演藝坊、精品店、精品館、製香舖、製麵所、廚藝坊、碾米廠、養生坊、養生舖、養蜂場、親子館、錄音室、餐酒館、點心坊、麵飯館、露營社、體驗館、手作食坊、文化廣場、主題公園、生活商場、生態茶場、生態農場、行動商城、料理食堂、烘焙教室、訓練中心、商務中心、國際商城、婚宴會館、甜點工坊、都會旅店、創始本舖、森林農場、渡假山莊、渡假酒店、渡假會館、結婚會舘、農產小舖、暢貨中心、精選酒店、網路商城、養生世界、養身會館、購物廣場、藝術工坊、藝術中心、露天農場、顧問中心、觀光酒店、手作文創店、手烘咖啡坊、茶飲專賣店、健康生活館、造型工作室、飲品專賣店、數位生活館、趣味生活館、ACADEMY、BAR、BEAUTY HOUSE、BISTRO、BOUTIQUE、BUTCHER'S SHOP、CANTEEN、CENTER、CINEMA、CLINIC、CLUB、COLLEGE、COMPOUND RESTAURANT、DELI、DELICATESSEN、DEVELOPMENT CENTER、EDUCATIONAL CENTER、ESHOP、FARM、FOOD COURT、FRUIT GARDEN、FUSION RESTAURANT、GALLERY、GARDEN、GOURMET STORE、GROCERY、GYM、HAIR STUDIO、HOME、HOTEL、HOUSE、HUB、INDUSTRIAL PARK、INN、IZAKAYA、KIDS MALL、KITCHEN、LAB、LABORATORY、LAW FIRM、LIFE HOUSE、LIFE MALL、LIVING CENTER、LIVING MALL、MALL、MARKET、MART、MUSEUM OF ART、NATIONAL MALL、NIGHT MARKET、ORCHARD、OUTLET、PHARMACY、PIZZERIA、PLAZA、PUB、RANCH 、RESORT、RESORT HOTEL、RESTAURANT、SCHOOL、SERVICE AREA、SHOP、SHOPPING CENTER、SHOPPING MALL、SQUARE、STATION、STEAKHOUSE、STORAGE、STORE、STUDIO、SUPER MARKET、TEA FACTORY、TEA GARDEN、TEA HOUSE、TEA SHOP、TEAROOM、TOAST SHOP、VILLAGE、WEDDING STUDIO 、WORK SHOP、WORLD、ZONE"
string06 = "阿門、哈利路亞、南無阿彌陀佛、NAMO AMITABHA"
string07 = "設計 設計字 設計圖 標章 墨色 圖型 圖形 股份有限公司 有限公司 集團 logo Logo LOGO"

str0 = string.split("、")
string00 = string00.split("、")
string01 = string01.split("、")
string02 = string02.split("、")
string03 = string03.split("、")
string04 = string04.split("、")
string05 = string05.split("、")
string06 = string06.split("、")
string07 = string07.split("、")
string0 = str0+string00+string01+string02+string03+string04+string05+string06+string07
# 2 to 7
weight_l = [[0.6,0.4,0,0,0,0],[0.45,0.3,0.25,0,0,0],[0.35,0.25,0.2,0.2,0,0],[0.35,0.25,0.14,0.13,0.12,0.11],[0.35,0.25,0.1,0.1,0.1,0.1],[0.35,0.25,0.1,0.1,0.1,0.05,0.05]]
#to remove the descriptive words
for i in string0:
    if word1.find(i)>0:
        #print(word1.find(i))
        word1 = word1[0:word1.find(i)]
    else:
        continue

for i in string0:
    if word2.find(i)>0:
        print(word2)
        #print(word1.find(i))
        word2 = word2[0:word2.find(i)]
    else:
        continue

#------------
result = []

# compare two words first
num = 0
subword = ""
print("申請案:" + word1)
print("前案:" + word2)
#decision logic
if len(word1)<=len(word2):
    num = len(word1)
else:
    num = len(word2)
# total number of character of the longer word
if len(word1)>=len(word2):
    leng_word = len(word1)
else:
    leng_word = len(word2)
if (len(word1) == 1 and len(word2) == 1 and word1 == word2) or (len(word1) == 2 and len(word2) == 2 and word1 == word2):
    print("完全相同")
elif (len(word1) == 1 and len(word2) == 1 and word1 != word2):
    picsim= pic(word1,word2)
    print("total " + str(picsim) + "%")
elif (len(word1) == 2 and len(word2) == 2 and word1 != word2):
    word1_l = []
    word2_l = []
    #decide how many characters
    if (word1[0:1] != word2[0:1] and word1[1:2] != word2[1:2]) and (word1[0:1] != word2[1:2] and word1[1:2] != word2[0:1]):
        print("total " + str(0.0) + "%")
    else:
        for i in range(0,2):
            word1_l.append(word1[i:i+1])
        for i in range(0,2):
            word2_l.append(word2[i:i+1])
        same = False
        for i in word1_l:
            for j in word2_l:
                if i == j:
                    subword = i
                    flag = False
                    npos1 = word1.find(subword)
                    npos2 = word2.find(subword)
                    if npos1 == npos2:
                        same = True
                        if npos1 == 0:
                            picsim = pic(word1[1:2],word2[1:2], index)
                            if picsim < 60:
                                a = 100. * 0.6 * 1.
                                picsim= picsim * 0.1 * 0.4 * 1.
                                print("total " + str(60+picsim) + "%")
                            else:
                                a = 100. * 0.6 * 1.
                                picsim= (picsim - 50) * 2.5 * 0.4 * 1.
                                print("total " + str(60+picsim) + "%")
                        else:
                            picsim = pic(word1[0:1],word2[0:1], index)
                            if picsim < 60:
                                a = 100. * 0.4 * 1.
                                picsim= picsim * 0.1 * 0.6 * 1.
                                print("total " + str(40+picsim) + "%")
                            else:
                                a = 100. * 0.4 * 1.
                                picsim= (picsim - 50) * 2.5 * 0.6 * 1.
                                print("total " + str(40+picsim) + "%")
                    break               
            if not flag:
                break
        if same == False:
            print("total " + str(54) + "%")
elif ((len(word1) >= 2 and len(word2) == 2) or (len(word1) == 2 and len(word2) >= 2) or (len(word1) > 2 and len(word2) > 2)) and word1 != word2:
     #seperate word to lists
    word1_l = []
    word2_l = []
    #decide how many characters
    for i in range(len(word1),1,-1):
    #decide the first position
        for j in range(0,len(word1)-i+1):
            word1_l.append(word1[j:j+i])
    for i in range(len(word2),1,-1):
        for j in range(0,len(word2)-i+1):
            word2_l.append(word2[j:j+i])
    #to find out the word
    same = False
    for i in word1_l:
        for j in word2_l:
            if i == j:
                subword = i
                flag = False
                same = True
                npos1 = word1.find(subword)
                npos2 = word2.find(subword)
                leng_subword = len(subword)
                # Compare the total the same words
                if npos1 == npos2:
                    a = 0
                    for i in range(leng_subword):
                        a = a + weight_l[num-2][i]
                    a = 1. * a * 1.
                else:
                    a = 0
                    for i in range(leng_subword):
                        a = a + weight_l[num-2][i]
                    a = 1. * a * 0.9
                # y words list
                # left hand side
                nb = 0
                if npos1 >= npos2:
                    head = npos2
                else:
                    head = npos1
                b = 0.
                index = 0
                for i in range(head,0,-1):
                    tmp = pic(word1[npos1-1-index:npos1-index],word2[npos2-1-index:npos2-index], index)
                    index = index + 1
                    b = b + (tmp * weight_l[num-2][i-1])
                    nb = nb + 1
                #right hand side
                if (len(word1)-npos1-leng_subword)>=(len(word2)-npos2-leng_subword):
                    remains = len(word2)-npos2-leng_subword
                else:
                    remains = len(word1)-npos1-leng_subword
                index = 0
                for i in range(0,remains):
                    tmp = pic(word1[npos1+leng_subword+index:npos1+leng_subword+index+1],word2[npos2+leng_subword+index:npos2+leng_subword+index+1], index)
                    index = index + 1
                    b = b + (tmp * weight_l[num-2][i+leng_subword])
                    nb = nb + 1
                # calculate the similarity
                score = (a*100. + b)*(leng_subword+nb)*1.3/leng_word
                print("total " + str(round(score,2)) + "%")
                break
    if same == False:
        score = 0. 
        if num<=7:
            for i in range(0,num):
                score = score + (pic(word1[i:i+1],word2[i:i+1], index) * weight_l[num-2][i])
            score = score * num *1.3/leng_word
            print("total " + str(round(score,2)) + "%")
        else:
            for i in range(0,7):
                score = score + (pic(word1[i:i+1],word2[i:i+1], index) * weight_l[num-2][i])
            score = score * num *1.3/leng_word
            print("total " + str(round(score,2)) + "%")
else:
    print("total " + str(0.0) + "%")
