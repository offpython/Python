# 실습1
name = '홍길동'
product = '야구글러브'
orderNo = 2342525
payMethod = '신용카드'
productPrice = 110000
payPrice = 100000
usePoint = 10000
payDate = '2023/03/07 21:50:12'
payDiv = 6
payDivCategory = '무'
phone = '02-123-2311'

# 실습2
print(name, '고객님 안녕하세요.')
print(name, '고객님의 주문이 완료되었습니다.')
print('다음은 주문 건에 대한 상세 내역입니다.')
print('-' * 50)
print('상품명\t:', product)
print('주문번호\t:', orderNo)
print('결제방법\t:', payMethod)
print('상품금액\t:', productPrice)
print('결제금액\t:', payPrice)
print('포인트\t:', usePoint)
print('결제일시\t:', payDate)
print('할부\t:', payDiv)
print('할부유형\t:', payDivCategory)
print('문의\t:', phone)
print('-' * 50)
print('저의 사이트를 이용해 주셔서 갑사합니다.')