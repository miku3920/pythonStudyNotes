# project 5
import socketserver as socketserver
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import urlparse, unquote
from functools import partial
from os import path
from datetime import datetime, timedelta
import json
import requests


class Model():
    def init(self, url):
        self.url = url
        self.path0 = unquote(urlparse(self.url).path)
        self.query = unquote(urlparse(self.url).query)
        self.YilanCounty = [
            '宜蘭市', '羅東鎮', '蘇澳鎮', '頭城鎮', '礁溪鄉',
            '壯圍鄉', '員山鄉', '冬山鄉', '五結鄉', '三星鄉',
            '大同鄉', '南澳鄉'
        ]
        self.TaoyuanCity = [
            '大園區', '蘆竹區', '觀音區', '龜山區', '桃園區',
            '中壢區', '新屋區', '八德區', '平鎮區', '楊梅區',
            '大溪區', '龍潭區', '復興區'
        ]
        self.HsinchuCounty = [
            '新豐鄉', '湖口鄉', '新埔鎮', '竹北市', '關西鎮',
            '芎林鄉', '竹東鎮', '寶山鄉', '尖石鄉', '橫山鄉',
            '北埔鄉', '峨眉鄉', '五峰鄉'
        ]
        self.MiaoliCounty = [
            '竹南鎮', '頭份市', '三灣鄉', '造橋鄉', '後龍鎮',
            '南庄鄉', '頭屋鄉', '獅潭鄉', '苗栗市', '西湖鄉',
            '通霄鎮', '公館鄉', '銅鑼鄉', '泰安鄉', '苑裡鎮',
            '大湖鄉', '三義鄉', '卓蘭鎮'
        ]
        self.ChanghuaCounty = [
            '伸港鄉', '和美鎮', '線西鄉', '鹿港鎮', '彰化市',
            '秀水鄉', '福興鄉', '花壇鄉', '芬園鄉', '芳苑鄉',
            '埔鹽鄉', '大村鄉', '二林鎮', '員林市', '溪湖鎮',
            '埔心鄉', '永靖鄉', '社頭鄉', '埤頭鄉', '田尾鄉',
            '大城鄉', '田中鎮', '北斗鎮', '竹塘鄉', '溪州鄉',
            '二水鄉'
        ]
        self.NantouCounty = [
            '仁愛鄉', '國姓鄉', '埔里鎮', '草屯鎮', '中寮鄉',
            '南投市', '魚池鄉', '水里鄉', '名間鄉', '信義鄉',
            '集集鎮', '竹山鎮', '鹿谷鄉'
        ]
        self.YunlinCounty = [
            '麥寮鄉', '二崙鄉', '崙背鄉', '西螺鎮', '莿桐鄉',
            '林內鄉', '臺西鄉', '土庫鎮', '虎尾鎮', '褒忠鄉',
            '東勢鄉', '斗南鎮', '四湖鄉', '古坑鄉', '元長鄉',
            '大埤鄉', '口湖鄉', '北港鎮', '水林鄉', '斗六市'
        ]
        self.ChiayiCounty = [
            '大林鎮', '溪口鄉', '阿里山鄉', '梅山鄉', '新港鄉',
            '民雄鄉', '六腳鄉', '竹崎鄉', '東石鄉', '太保市',
            '番路鄉', '朴子市', '水上鄉', '中埔鄉', '布袋鎮',
            '鹿草鄉', '義竹鄉', '大埔鄉'
        ]
        self.PingtungCounty = [
            '高樹鄉', '三地門鄉', '霧臺鄉', '里港鄉', '鹽埔鄉',
            '九如鄉', '長治鄉', '瑪家鄉', '屏東市', '內埔鄉',
            '麟洛鄉', '泰武鄉', '萬巒鄉', '竹田鄉', '萬丹鄉',
            '來義鄉', '潮州鎮', '新園鄉', '崁頂鄉', '新埤鄉',
            '南州鄉', '東港鎮', '林邊鄉', '佳冬鄉', '春日鄉',
            '獅子鄉', '琉球鄉', '枋山鄉', '牡丹鄉', '滿州鄉',
            '車城鄉', '恆春鎮', '枋寮鄉'
        ]
        self.TaitungCounty = [
            '長濱鄉', '海端鄉', '池上鄉', '成功鎮', '關山鎮',
            '東河鄉', '鹿野鄉', '延平鄉', '卑南鄉', '臺東市',
            '太麻里鄉', '綠島鄉', '達仁鄉', '大武鄉', '蘭嶼鄉',
            '金峰鄉'
        ]
        self.HualianCounty = [
            '秀林鄉', '新城鄉', '花蓮市', '吉安鄉', '壽豐鄉',
            '萬榮鄉', '鳳林鎮', '豐濱鄉', '光復鄉', '卓溪鄉',
            '瑞穗鄉', '玉里鎮', '富里鄉'
        ]
        self.PenghuCounty = [
            '白沙鄉', '西嶼鄉', '湖西鄉', '馬公市', '望安鄉',
            '七美鄉'
        ]
        self.KeelungCity = [
            '安樂區', '中山區', '中正區', '七堵區', '信義區',
            '仁愛區', '暖暖區'
        ]
        self.HsinchuCity = [
            '北區', '香山區', '東區'
        ]
        self.ChiayiCity = [
            '東區', '西區'
        ]
        self.TaipeiCity = [
            '北投區', '士林區', '內湖區', '中山區', '大同區',
            '松山區', '南港區', '中正區', '萬華區', '信義區',
            '大安區', '文山區'
        ]
        self.KaohsiungCity = [
            '楠梓區', '左營區', '三民區', '鼓山區', '苓雅區',
            '新興區', '前金區', '鹽埕區', '前鎮區', '旗津區',
            '小港區', '那瑪夏區', '甲仙區', '六龜區', '杉林區',
            '內門區', '茂林區', '美濃區', '旗山區', '田寮區',
            '湖內區', '茄萣區', '阿蓮區', '路竹區', '永安區',
            '岡山區', '燕巢區', '彌陀區', '橋頭區', '大樹區',
            '梓官區', '大社區', '仁武區', '鳥松區', '大寮區',
            '鳳山區', '林園區', '桃源區'
        ]
        self.NewTaipeiCity = [
            '石門區', '三芝區', '金山區', '淡水區', '萬里區',
            '八里區', '汐止區', '林口區', '五股區', '瑞芳區',
            '蘆洲區', '雙溪區', '三重區', '貢寮區', '平溪區',
            '泰山區', '新莊區', '石碇區', '板橋區', '深坑區',
            '永和區', '樹林區', '中和區', '土城區', '新店區',
            '坪林區', '鶯歌區', '三峽區', '烏來區'
        ]
        self.TaichungCity = [
            '北屯區', '西屯區', '北區', '南屯區', '西區',
            '東區', '中區', '南區', '和平區', '大甲區',
            '大安區', '外埔區', '后里區', '清水區', '東勢區',
            '神岡區', '龍井區', '石岡區', '豐原區', '梧棲區',
            '新社區', '沙鹿區', '大雅區', '潭子區', '大肚區',
            '太平區', '烏日區', '大里區', '霧峰區'
        ]
        self.TainanCity = [
            '安南區', '中西區', '安平區', '東區', '南區',
            '北區', '白河區', '後壁區', '鹽水區', '新營區',
            '東山區', '北門區', '柳營區', '學甲區', '下營區',
            '六甲區', '南化區', '將軍區', '楠西區', '麻豆區',
            '官田區', '佳里區', '大內區', '七股區', '玉井區',
            '善化區', '西港區', '山上區', '安定區', '新市區',
            '左鎮區', '新化區', '永康區', '歸仁區', '關廟區',
            '龍崎區', '仁德區'
        ]
        self.LianjiangCounty = [
            '南竿鄉', '北竿鄉', '莒光鄉', '東引鄉'
        ]
        self.KinmenCounty = [
            '金城鎮', '金湖鎮', '金沙鎮', '金寧鄉', '烈嶼鄉',
            '烏坵鄉'
        ]
        self.taiwan = {
            '宜蘭縣': self.YilanCounty,
            '桃園市': self.TaoyuanCity,
            '新竹縣': self.HsinchuCounty,
            '苗栗縣': self.MiaoliCounty,
            '彰化縣': self.ChanghuaCounty,
            '南投縣': self.NantouCounty,
            '雲林縣': self.YunlinCounty,
            '嘉義縣': self.ChiayiCounty,
            '屏東縣': self.PingtungCounty,
            '臺東縣': self.TaitungCounty,
            '花蓮縣': self.HualianCounty,
            '澎湖縣': self.PenghuCounty,
            '基隆市': self.KeelungCity,
            '新竹市': self.HsinchuCity,
            '嘉義市': self.ChiayiCity,
            '臺北市': self.TaipeiCity,
            '高雄市': self.KaohsiungCity,
            '新北市': self.NewTaipeiCity,
            '臺中市': self.TaichungCity,
            '臺南市': self.TainanCity,
            '連江縣': self.LianjiangCounty,
            '金門縣': self.KinmenCounty,
        }
        self.cityApi = {
            '宜蘭縣': 'F-D0047-003',
            '桃園市': 'F-D0047-007',
            '新竹縣': 'F-D0047-011',
            '苗栗縣': 'F-D0047-015',
            '彰化縣': 'F-D0047-019',
            '南投縣': 'F-D0047-023',
            '雲林縣': 'F-D0047-027',
            '嘉義縣': 'F-D0047-031',
            '屏東縣': 'F-D0047-035',
            '臺東縣': 'F-D0047-039',
            '花蓮縣': 'F-D0047-043',
            '澎湖縣': 'F-D0047-047',
            '基隆市': 'F-D0047-051',
            '新竹市': 'F-D0047-055',
            '嘉義市': 'F-D0047-059',
            '臺北市': 'F-D0047-063',
            '高雄市': 'F-D0047-067',
            '新北市': 'F-D0047-071',
            '臺中市': 'F-D0047-075',
            '臺南市': 'F-D0047-079',
            '連江縣': 'F-D0047-083',
            '金門縣': 'F-D0047-087',
        }

    def getPath(self):
        return self.path0

    def getQuery(self):
        return self.query

    def getQueryComponents(self):
        return dict(qc.split("=") for qc in self.query.split("&"))

    def setTitle(self,title):
        self.title=title

    def getTitle(self):
        return self.title

    def getNowTime(self):
        return datetime.now()

    def getDataTime(self, api):
        data = self.getData(api)
        # time = data['cwbopendata']['dataset']['datasetInfo']['update']
        time = data['records']['locations'][0]['location'][0]['weatherElement'][0]['time'][0]['startTime']
        return datetime.strptime(time[0:19], "%Y-%m-%d %H:%M:%S")

    def getWeatherElement(self, api):
        data = self.getData(api)
        return data['records']['locations'][0]['location'][0]['weatherElement']

    def getData(self, api):
        path0 = 'cache/'+api.replace('?locationName=', '-')+'.json'
        if not path.exists(path0):
            data = self.updateData(api)
            return json.loads(data)

        return self.loadData(path0)

    def updateData(self, api):
        path0 = 'cache/'+api.replace('?locationName=', '-')+'.json'
        data = requests.get('https://opendata.cwb.gov.tw/api/v1/rest/datastore/'+api +
                            '&Authorization=?????????&format=JSON').text
        self.saveData(path0, data)
        return data

    def loadData(self, path0):
        with open(path0, 'r', encoding='utf-8') as f:
            return json.load(f)

    def saveData(self, path0, data):
        with open(path0, 'w', encoding='utf-8') as f:
            f.write(data)

class View():
    def __init__(self, model):
        self.model = model

    def init(self, writer):
        self.writer = writer

    def doDashboard(self):
        dashboard = self.createDashboard()
        self.doWrite(dashboard)

    def doChart(self, api):
        self.weatherElement = self.model.getWeatherElement(api)
        chart = self.createChart()
        self.doWrite(chart)

    def createDashboard(self):
        return {
            "slices": [
                {
                    "sliceId": 1,
                    "x": 0,
                    "y": 0,
                    "w": 36,
                    "h": 14,
                    "width": 360,
                    "height": 290,
                    "i": "chart1",
                    "chartType": "x-line",
                    "title": "Line"
                }
            ]
        }

    def createChart(self):
        return {
            "title":  self.model.getTitle(),
            "api": {
                "chartType": "x-line",
                "columns": [
                    {
                        "type": "x",
                        "field": "Time",
                        "name": "時間"
                    },
                    {
                        "type": "y",
                        "field": "MaxT",
                        "name": "最高溫度"
                    },
                    {
                        "type": "y",
                        "field": "MinT",
                        "name": "最低溫度"
                    }
                ],
                "rows": self.createData()
            }
        }

    def createData(self):
        weatherElement = self.fixWeatherElement(self.weatherElement)
        weekday = ['一', '二', '三', '四', '五', '六', '日', ]
        data = []
        MaxT = weatherElement['MaxT']['time']
        MinT = weatherElement['MinT']['time']
        PoP12h = weatherElement['PoP12h']['time']
        for i in range(len(MaxT)):
            time = MaxT[i]['startTime']
            formatTime = datetime.strptime(time[0:19], "%Y-%m-%d %H:%M:%S")
            strTime = formatTime.strftime(
                "%m/%d")+'　'+weekday[formatTime.weekday()]
            if int(formatTime.strftime("%H")) < 18:
                strTime += '　白天　' + \
                    PoP12h[i]['elementValue'][0]['value'] + '%'
            else:
                strTime += '　晚上　' + \
                    PoP12h[i]['elementValue'][0]['value'] + '%'

            dist0 = {
                "MaxT": MaxT[i]['elementValue'][0]['value'],
                "MinT": MinT[i]['elementValue'][0]['value'],
                "Time": strTime,
            }
            data.append(dist0)

        return data

    def doWrite(self, data):
        output = json.dumps(data)
        self.writer.write(output.encode("utf-8"))

    def fixWeatherElement(self, weatherElement):
        dist0 = {}
        for item in weatherElement:
            dist0[item['elementName']] = item
        return dist0


class Controller():
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def setWriter(self, writer):
        self.view.init(writer)

    def setUrl(self, url):
        self.model.init(url)

    def run(self):
        model = self.model
        view = self.view

        if model.getPath() == '/dashboard':
            view.doDashboard()
        elif model.getPath() == '/chart_data':
            api = 'F-D0047-091?locationName=臺北市'
            if model.getQuery():
                query_components = model.getQueryComponents()
                if 'q' in query_components:
                    api = self.getApi(query_components["q"])
            if self.isDateShouldUpdate(api):
                model.updateData(api)
            view.doChart(api)

    def getApi(self, q):
        listQ = q.split()

        if len(listQ) == 0:
            self.model.setTitle('臺北市')
            return 'F-D0047-091?locationName=臺北市'

        city = ''
        q = listQ[0].replace('台', '臺')

        cityName = self.getCityName(q)
        if len(listQ) >= 2:
            city = cityName
            q = listQ[1].replace('台', '臺')

        cityName2, cityApi, townName = self.getCityApiAndTownName(city, q)

        if cityApi:
            self.model.setTitle(cityName2+' '+townName)
            return cityApi+'?locationName='+townName

        if cityName:
            self.model.setTitle(cityName)
            return 'F-D0047-091?locationName='+cityName

        self.model.setTitle('臺北市')
        return 'F-D0047-091?locationName=臺北市'

    def getCityName(self, q):
        for cityName in self.model.cityApi:
            if q in cityName:
                return cityName
        return False

    def getCityApiAndTownName(self, city, q):
        if city:
            for townName in self.model.taiwan[city]:
                if q in townName:
                    return city, self.model.cityApi[city], townName

        for cityName, townList in self.model.taiwan.items():
            for townName in townList:
                if q in townName:
                    return cityName, self.model.cityApi[cityName], townName
        
        return False, False, False

    def isDateShouldUpdate(self, api):
        model = self.model
        dataTime = model.getDataTime(api)
        nowTime = model.getNowTime()
        deltaTime = timedelta(hours=12)
        return dataTime+deltaTime <= nowTime


class MyHandler(RequestHandler):
    def __init__(self, controller, *args, **kwargs):
        self.controller = controller
        super().__init__(*args, **kwargs)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self):
        self.do_HEAD()

        self.controller.setUrl(self.path)
        self.controller.setWriter(self.wfile)
        self.controller.run()


model = Model()
view = View(model)
controller = Controller(view, model)
handler = partial(MyHandler, controller)

socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', 8000), handler)
httpd.serve_forever()
