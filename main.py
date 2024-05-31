# nomber =5
# while nomber <10:
#     print(nomber)
#     nomber +=1
# else:
#     print("dastur tohtadi")

# nomber = 0
# while True:
#     print(nomber)
#     nomber += 1
#     if nomber >= 10:
#         break
# else:
#     print("dastur tohtadi")

import random
import string
from qr_code import make_qr
def qr_raddom(nomber):
    for _ in range(nomber):
      malum=[]
      ascii_letters = string.ascii_lowercase + string.ascii_uppercase
      raddr=random.sample(ascii_letters, 10)
      radrs=random.sample(ascii_letters, 5)
      nams=''.join(radrs)
      nik='https://'.join(raddr)
      if raddr not in malum:
          
          make_qr(nik, nams)
          yield make_qr
for i in qr_raddom(10):
   ...

         
