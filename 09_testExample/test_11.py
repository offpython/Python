# 조건문 01

# 실습1
carSpeed = int(input('속도 입력 : '))
limitSpeed = 50

if carSpeed > 50:
    print('안전속도 위반!! 과태료 50,000원 부과 대상!!')
else:
    print('안전속도 준수!!')

# 실습2
msgInput = input('메세지 입력 : ')
msgCnt = len(msgInput)
msgPrice = 50

if len(msgInput) > 50:
    msgPrice = 100
    print('MMS 발송!!')
else:
    msgPrice = 50
    print('SMS 발송!!')

print('메시지 길이 : {}'.format(msgCnt))
print('메시지 발송 요금 : {}원'.format(msgPrice))





