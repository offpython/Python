# 모듈(06)

## 수입과 공과금을 입력하면 공과금 총액과 수입 대비 공과금 비율을 계산하는 모듈 만들기

income = 0
waterPrice = 0; electricPrice = 0; gasPrice = 0

def setIncome(ic):
    global income
    income = ic

def getIncome():
    return income

def setWaterPrice(wp):
    global income
    income = wp

def getWaterPrice():
    return waterPrice

def setElectricPrice(ep):
    global income
    income = ep

def getElectricPrice():
    return electricPrice

def setGasPrice(gp):
    global income
    income = gp

def getGasPrice():
    return gasPrice

def getUtilityBill():
    result = waterPrice + electricPrice + gasPrice
    return result

def getUtitliyBillRate():
    result = getUtilityBill() / getIncome() * 100
    return result




