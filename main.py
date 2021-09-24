# # # # ez a sor kód azt csinálja, hogy kiírja a terminalra, hogy Hello!
# # # # print('Hello!')

# # # iranyitoszam = input('Irányítószám: ')
# # # varos = input('város: ')
# # # kozteruletNeve =input('közterület neve: ')
# # # kozteruletJellege = input('közterület jellege: ')
# # # hazszam = input('házszám: ')

# # # print(f'{iranyitoszam} {varos}, {kozteruletNeve} {kozteruletJellege} {hazszam}.')

# # vezetekNev1 = input('első vezetéknév: ')
# # vezetekNev2 = input('második vezetéknév: ')
# # keresztNev1 = input('első keresztnév: ')
# # keresztNev2 = input('második keresztnév: ')

# # print(f'{vezetekNev1} {keresztNev1}')
# # print(f'{vezetekNev1} {keresztNev2}')
# # print(f'{vezetekNev2} {keresztNev1}')
# # print(f'{vezetekNev2} {keresztNev2}')

# haviFizetes = int(input('írd be a havi fizetésed: '))
# print(f'éves fizetés: {12 * haviFizetes} Ft')

# euroArfolyama = float(input('euro árfolyama: '))
# ennyiEuroVan = int(input('ennyi euro-m van: '))
# ennyiForintotEr = ennyiEuroVan * euroArfolyama
# print(f'Ennyi forintot ér a pénzem: {ennyiForintotEr}')



# sugar = int(input('add meg a kör sugarát: '))
# print(f'kör kerülete: {2 * sugar * math.pi}')
# print(f'kör területe: {sugar * sugar * math.pi}')
# print(math.sqrt(16))
# print(math.pow(2, 10))

import math
magassag = float(input('ennyi cm magas vagy: ')) / 100
suly = float(input('ennyi kg-os vagy: '))
tti = suly / math.pow(magassag, 2)
print('a testsúlykategóriád: ')
if tti < 16: print('súlyos soványság')
elif tti < 17: print('mérsékelt soványság')
elif tti < 18.5: print('enyhe soványság')
elif tti < 25: print('normális testsúly')
elif tti < 30: print('túlsúlyos')
elif tti < 35: print('I. fokú elhízás')
elif tti < 40: print('II. fokú elhízás ')
else: print('III. fokú (súlyos) elhízás')

x = int(input('szám: '))

if x > 10:
  print('x nagyobb mint 10')
else: 
  if x == 10: 
    print('x egyenlő 10el')
  else:
    print('x nem nagyobb mint 10')

print('szép nap van')