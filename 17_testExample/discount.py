# 모듈(02)

## 상품 구매 개수에 따라 할인율일 결정되는 모듈을 만들기

def calculatorTotalPrice(gs): #gs=상품

    if len(gs) <= 0:
        print('구매 상품이 없습니다.')
        return

    rate = 25
    totalPrice = 0

    rates = {1:5, 2:10, 3:15, 4:20}  # {1개:5할인}

    if len(gs) in rates: # 할인율 결정
        rate = rates[len(gs)]

    for g in gs:
        totalPrice += g * (1 - rate * 0.01)  # 전체가격

    return[rate, int(totalPrice)]


