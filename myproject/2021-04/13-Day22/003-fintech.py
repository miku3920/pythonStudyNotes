import comtypes.gen.SKCOMLib as sk
import os
import comtypes.client

comtypes.client.GetModule('SKCOM.dll')
skC = comtypes.client.CreateObject(sk.SKCenterLib, interface=sk.ISKCenterLib)
skOOQ = comtypes.client.CreateObject(sk.SKOOQuoteLib, interface=sk.ISKOOQuoteLib)
skO = comtypes.client.CreateObject(sk.SKOrderLib, interface=sk.ISKOrderLib)
skOSQ = comtypes.client.CreateObject(sk.SKOSQuoteLib, interface=sk.ISKOSQuoteLib)
skQ = comtypes.client.CreateObject(sk.SKQuoteLib, interface=sk.ISKQuoteLib)
skR = comtypes.client.CreateObject(sk.SKReplyLib, interface=sk.ISKReplyLib)

a = skC.SKCenterLib_Login('帳號', '密碼')
b = skQ.SKQuoteLib_EnterMonitor()
c = skQ.SKQuoteLib_RequestStocks('2330')
