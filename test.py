from api import *


print("Starting test of xcat...")
htlcTrade = initiate()
fund_buyer()
# zXcat.generate(8)

# zXcat.generate(6)
redeem_seller()
zXcat.generate(1)
bXcat.generate(1)
redeem_buyer()


# addr = CBitcoinAddress('tmFRXyju7ANM7A9mg75ZjyhFW1UJEhUPwfQ')
# print(addr)
# # print(b2x('tmFRXyju7ANM7A9mg75ZjyhFW1UJEhUPwfQ'))
# print(b2x(addr))
e