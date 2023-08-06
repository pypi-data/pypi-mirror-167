# Real-Time ROI Display: Scrapes RT data to calculate ROI

'''
Libraries #
'''
import time
import datetime
import board
import finnhub
import urllib.request
import json
import Adafruit_IO as io
import subprocess

'''
SETUP
'''

# Adafruit IO
ADAFRUIT_IO_KEY = 'c36f59e54ca740759d5274d8e5c8cabb'
ADAFRUIT_IO_USERNAME = 'dsblock19'
aio = io.Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
# Feeds
APPshareIO = aio.feeds('investments.appshare')
BitNumberIO = aio.feeds('investments.bitnumber')
BNGOShareIO = aio.feeds('investments.bngoshare')
CCVio = aio.feeds('investments.currentcrypval')
CNBSShareIO = aio.feeds('investments.cnbsshare')
CSVio = aio.feeds('investments.currentstockval')
CTVio = aio.feeds('investments.currenttotalval')
DisShareIO = aio.feeds('investments.disshare')
EthNumberIO = aio.feeds('investments.ethnumber')
FaceShareIO = aio.feeds('investments.faceshare')
CashIO = aio.feeds('investments.cash')
GoShareIO = aio.feeds('investments.goshare')
MicroShareIO = aio.feeds('investments.microshare')
ROIio = aio.feeds('investments.roi')
TesShareIO = aio.feeds('investments.tesshare')
TSio = aio.feeds('investments.totalspent')
TwitShareIO = aio.feeds('investments.twitshare')
WKHSShareIO = aio.feeds('investments.wkhsshare')
YOLOShareIO = aio.feeds('investments.yoloshare')
ARKKShareIO = aio.feeds('investments.arkkshare')
SPYXShareIO = aio.feeds('investments.spyxshare')
ESGVShareIO = aio.feeds('investments.esgvshare')
VGTShareIO = aio.feeds('investments.vgtshare')
VOOShareIO = aio.feeds('investments.vooshare')
CryptoROIio = aio.feeds('investments.cryptoroi')
StockROIio = aio.feeds('investments.stockroi')
TSCio = aio.feeds('investments.totalspentcryp')
TSSio = aio.feeds('investments.totalspentstock')
InflationIO = aio.feeds('investments.inflation')
CarNumberIO = aio.feeds('investments.carnumber')
VNQShareIO = aio.feeds('investments.vnqshare')
VPNShareIO = aio.feeds('investments.vpnshare')
INDSShareIO = aio.feeds('investments.indsshare')

# Delay Time (Min)
T = 3

# CRYPTO
# BITCOIN
BitURL = "https://api.coindesk.com/v1/bpi/currentprice.json"
# ETHEREUM
EthURL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum"

# STOCKS/ETFs
finnhub_client = finnhub.Client(api_key="c224auiad3id53vufgfg")

Inflation = 0

# VALUE EQUATIONS

# CRYPTO SETUP
'''
CB = Market Value (Bitcoin)
CE = Market Value (Ethereum)
BH = Owned Bitcoins
EH = Owned Ethereum
CCV = Current Owned Crypto Value
CCV = (CB * BH) + (CE * EH)
'''
# Constants
BH = 0
EH = 0
CarH = 0
# Variables
CB = 0
CE = 0
CCar = 0
CCV = 0
CryptoROI = 0

# GOLD SETUP
'''
CG = Market Value (Gold Oz)
GH = Owned Gold (oz)
CGV = Current Owned Gold Value
CGV = CG * GH
'''
# Constants
GH = 0
CH = 0
# Variables
CG = 0
CGV = 0

# STOCKS/ETFS SETUP
'''
XXXval = Current Price (XXX)
XXH = shares of XXX
CSV = Current Owned Stocks/ETFs Value
CSV = [XXXH * XXXval] + ...
'''
CSV = 0
# Stocks
# Microsoft (MSFT)
MSFTval = 0
MSH = 0.109728
# Tesla (TSLA)
TSLAval = 0
TSH = 0.066026
# Disney(DIS)
DISval = 0
DIH = 0.153614
# Facebook (FB)
FBval = 0
FBH = 0.071656
# Twitter (TWTR)
TWTRval = 0
TWH = 0.304661
# GoPro (GPRO)
GPROval = 0
GPH = 1.69
# BNGO
BNGOval = 0
BNH = 1.6
# WKHS
WKHSval = 0
WKH = 0.774262
# Apple (AAPL)
AAPLval = 0
AAH = 0.035187
# ETFs
# YOLO
YOLOval = 0
YOH = 46
# CNBS
CNBSval = 0
CNH = 37
# ARKK
ARKKval = 0
ARKH = 8
# SPYX
SPYXval = 0
SPYH = 10
# ESGV
ESGVval = 0
ESGH = 13
# VGT
VGTval = 0
VGTH = 3
# VOO
VOOval = 0
VOOH = 4
# VNQ
VNQval = 0
VNQH = 10.0636
# VPN
VPNval = 0
VPNH = 23
# INDS
INDSval = 0
INDSH = 10.0431

StockROI = 0

# ROI SETUP
'''
TS = Total Spent
CV = Current Value
CV = CCV + CGV + CSV
ROI = [CV - TS] / TS
'''
# Constants
TS = 0
# Variables
CTV = 0
ROI = 0


'''
FUNCTIONS
'''

# Current Crypto Value
def CurrentCryptoValue(BH, EH, CarH):
    with urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json") as url:
        data = json.loads(url.read().decode())
    data = data['bpi']
    data = data['USD']
    data = float(data['rate_float'])
    CB = data
    with urllib.request.urlopen("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum") as url:
        dataII = json.loads(url.read().decode())
    dataII = dataII[0]
    dataII = float(dataII['current_price'])
    CE = dataII
    with urllib.request.urlopen("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=cardano") as url:
        dataIII = json.loads(url.read().decode())
    dataIII = dataIII[0]
    dataIII = float(dataIII['current_price'])
    CCar = dataIII
    CCV = (CB * BH) + (CE * EH) + (CCar * CarH)
    return CCV

# Current Stocks/ETFs Value
def CurrentStocksValue(MSH, TSH, DIH, FBH, TWH, GPH, BNH, WKH, AAH, YOH, CNH, ARKKH, SPYH, ESGH, VGTH, VOOH, VNQH, VPNH, INDSH):
    # Microsoft (MSFT)
    MSFTval = finnhub_client.quote('MSFT')
    MSFTval = float(MSFTval['c'])
    # Tesla (TSLA)
    TSLAval = finnhub_client.quote('TSLA')
    TSLAval = float(TSLAval['c'])
    # Disney(DIS)
    DISval = finnhub_client.quote('DIS')
    DISval = float(DISval['c'])
    # Facebook (FB)
    FBval = finnhub_client.quote('FB')
    FBval = float(FBval['c'])
    # Twitter (TWTR)
    TWTRval = finnhub_client.quote('TWTR')
    TWTRval = float(TWTRval['c'])
    # GoPro (GPRO)
    GPROval = finnhub_client.quote('GPRO')
    GPROval = float(GPROval['c'])
    # BNGO
    BNGOval = finnhub_client.quote('BNGO')
    BNGOval = float(BNGOval['c'])
    # WKHS
    WKHSval = finnhub_client.quote('WKHS')
    WKHSval = float(WKHSval['c'])
    # Apple (AAPL)
    AAPLval = finnhub_client.quote('AAPL')
    AAPLval = float(AAPLval['c'])
    # ETFs
    # YOLO
    YOLOval = finnhub_client.quote('YOLO')
    YOLOval = float(YOLOval['c'])
    # CNBS
    CNBSval = finnhub_client.quote('CNBS')
    CNBSval = float(CNBSval['c'])
    # ARKK
    ARKKval = finnhub_client.quote('ARKK')
    ARKKval = float(ARKKval['c'])
    # SPYX
    SPYXval = finnhub_client.quote('SPYX')
    SPYXval = float(SPYXval['c'])
    # ESGV
    ESGVval = finnhub_client.quote('ESGV')
    ESGVval = float(ESGVval['c'])
    # VGT
    VGTval = finnhub_client.quote('VGT')
    VGTval = float(VGTval['c'])
    # VOO
    VOOval = finnhub_client.quote('VOO')
    VOOval = float(VOOval['c'])
    # VNQ
    VNQval = finnhub_client.quote('VNQ')
    VNQval = float(VNQval['c'])
    # VPN
    VPNval = finnhub_client.quote('VPN')
    VPNval = float(VPNval['c'])
    # INDS
    INDSval = finnhub_client.quote('INDS')
    INDSval = float(INDSval['c'])
    # Total Stock/ETF value
    TE1 = (MSFTval * MSH) + (TSLAval * TSH) + (DISval * DIH) + (FBval * FBH) + (TWTRval * TWH)
    TE2 = (GPROval * GPH) + (BNGOval * BNH) + (WKHSval * WKH) + (AAPLval * AAH)
    TE3 = (CNBSval * CNH) + (ARKKval * ARKH) + (SPYXval * SPYH) + (ESGVval * ESGH) + (VGTval * VGTH) + (VOOval * VOOH) + (YOLOval * YOH)
    TE4 = (VNQval * VNQH) + (VPNval * VPNH) + (INDSval * INDSH)
    CSV = TE1 + TE2 + TE3 + TE4
    return CSV

# Send Data
def SendIO(CCV, CSV, CTV, ROI, CryptoROI, StockROI, Inflation, CH, TS, AAH, BNH, CNH, DIH, FBH, GPH, MSH, TSH, TWH, WKH, YOH, ARKH, SPYH, ESGH, VGTH, VOOH, VNQH, VPNH, INDSH):
    # print('Sending Data')
    aio.send_data(CCVio.key, CCV)
    aio.send_data(CSVio.key, CSV)
    aio.send_data(CTVio.key, CTV)
    aio.send_data(ROIio.key, ROI)
    aio.send_data(CryptoROIio.key, CryptoROI)
    aio.send_data(StockROIio.key, StockROI)
    aio.send_data(InflationIO.key, Inflation)
    aio.send_data(CashIO.key, CH)
    aio.send_data(TSio.key, TS)

    aio.send_data(APPshareIO.key, AAH)
    aio.send_data(BNGOShareIO.key, BNH)
    aio.send_data(CNBSShareIO.key, CNH)
    aio.send_data(DisShareIO.key, DIH)
    aio.send_data(FaceShareIO.key, FBH)
    aio.send_data(GoShareIO.key, GPH)
    aio.send_data(MicroShareIO.key, MSH)
    aio.send_data(TesShareIO.key, TSH)
    aio.send_data(TwitShareIO.key, TWH)
    aio.send_data(WKHSShareIO.key, WKH)
    aio.send_data(YOLOShareIO.key, YOH)
    aio.send_data(ARKKShareIO.key, ARKH)
    aio.send_data(SPYXShareIO.key, SPYH)
    aio.send_data(ESGVShareIO.key, ESGH)
    aio.send_data(VGTShareIO.key, VGTH)
    aio.send_data(VOOShareIO.key, VOOH)
    aio.send_data(VNQShareIO.key, VNQH)
    aio.send_data(VPNShareIO.key, VPNH)
    aio.send_data(INDSShareIO.key, INDSH)


# Get Data
def GetIO():
    # print('Getting Data')
    MSH = aio.receive(MicroShareIO.key).value
    MSH = float(MSH)
    TSH = aio.receive(TesShareIO.key).value
    TSH = float(TSH)
    DIH = aio.receive(DisShareIO.key).value
    DIH = float(DIH)
    FBH = aio.receive(FaceShareIO.key).value
    FBH = float(FBH)
    TWH = aio.receive(TwitShareIO.key).value
    TWH = float(TWH)
    GPH = aio.receive(GoShareIO.key).value
    GPH = float(GPH)
    BNH = aio.receive(BNGOShareIO.key).value
    BNH = float(BNH)
    WKH = aio.receive(WKHSShareIO.key).value
    WKH = float(WKH)
    AAH = aio.receive(APPshareIO.key).value
    AAH = float(AAH)
    YOH = aio.receive(YOLOShareIO.key).value
    YOH = float(YOH)
    CNH = aio.receive(CNBSShareIO.key).value
    CNH = float(CNH)
    BH = aio.receive(BitNumberIO.key).value
    BH = float(BH)
    CH = aio.receive(CashIO.key).value
    CH = float(CH)
    EH = aio.receive(EthNumberIO.key).value
    EH = float(EH)
    ARKKH = aio.receive(ARKKShareIO.key).value
    ARKKH = float(ARKKH)
    SPYH = aio.receive(SPYXShareIO.key).value
    SPYH = float(SPYH)
    ESGH = aio.receive(ESGVShareIO.key).value
    ESGH = float(ESGH)
    VGTH = aio.receive(VGTShareIO.key).value
    VGTH = float(VGTH)
    VOOH = aio.receive(VOOShareIO.key).value
    VOOH = float(VOOH)
    TSC = aio.receive(TSCio.key).value
    TSC = float(TSC)
    TSS = aio.receive(TSSio.key).value
    TSS = float(TSS)
    Inflation = aio.receive(InflationIO.key).value
    Inflation = float(Inflation)
    CarH = aio.receive(CarNumberIO.key).value
    CarH = float(CarH)
    VNQH = aio.receive(VNQShareIO.key).value
    VNQH = float(VNQH)
    VPNH = aio.receive(VPNShareIO.key).value
    VPNH = float(VPNH)
    INDSH = aio.receive(INDSShareIO.key).value
    INDSH = float(INDSH)
    return BH, CH, EH, MSH, TSH, DIH, FBH, TWH, GPH, BNH, WKH, AAH, YOH, CNH, ARKKH, SPYH, ESGH, VGTH, VOOH, VNQH, VPNH, INDSH, TSC, TSS, Inflation, CarH


'''
LOOP
'''

def ROpI():
    loop = 1
    while True:
        try:
            print('\nLoop Start')

            # Get Data
            BH, CH, EH, MSH, TSH, DIH, FBH, TWH, GPH, BNH, WKH, AAH, YOH, CNH, ARKKH, SPYH, ESGH, VGTH, VOOH, VNQH, VPNH, INDSH, TSC, TSS, Inflation, CarH = GetIO()

            # Stock/ETF
            CSV = CurrentStocksValue(MSH, TSH, DIH, FBH, TWH, GPH, BNH, WKH, AAH, YOH, CNH, ARKKH, SPYH, ESGH, VGTH, VOOH, VNQH, VPNH, INDSH)
            print('Current Stock/ETF Value: $' + str(CSV))
            StockROI = ((CSV - TSS) / TSS) * 100
            print(' Stock/ETF ROI: ' + str(StockROI) + '%')
            # Crypto
            CCV = CurrentCryptoValue(BH, EH, CarH)
            print('Current Crypto Value: $' + str(CCV))
            CryptoROI = ((CCV - TSC) / TSC) * 100
            print(' Crypto ROI: ' + str(CryptoROI) + '%')
            # Total
            CTV = CSV + CCV + CH
            TS = TSC + TSS + CH
            print('Current Total Value: ' + str(CTV))
            ROI = ((CTV - TS) / TS) * 100
            print(' ROI: ' + str(ROI))

            # Send Data
            print('Send Data')
            SendIO(CCV, CSV, CTV, ROI, CryptoROI, StockROI, Inflation, CH, TS, AAH, BNH, CNH, DIH, FBH, GPH, MSH, TSH, TWH, WKH, YOH, ARKH, SPYH, ESGH, VGTH, VOOH, VNQH, VPNH, INDSH)

            # Write Data
            print('Write Data')
            date = datetime.datetime.now().strftime('%m/%d/%Y,%H:%M:%S')
            D1 = str(TS) + ',' + str(TSS) + ',' + str(TSC)
            D2 = str(ROI) + ',' + str(StockROI) + ',' + str(CryptoROI)
            D3 = str(CTV) + ',' + str(CSV) + ',' + str(CCV)
            DataString = date + ',' + str(Inflation) + ',' + D1 + ',' + D2 + ',' + D3
            with open('/home/pi/FinTech/Data/InvestmentData.csv', 'a') as Dat:
                Dat.write(DataString + '\n')

            print('End Loop ' + str(loop))
            loop = loop + 1
            time.sleep(60 * T)


        except (Exception) as e:
            print("\nSome error occured - ", e)
            time.sleep(10)
