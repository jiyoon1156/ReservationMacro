import pyautogui as pag
import time

#2시만 조진다
x, y = pag.position()
print(x, y)

x = [274, 400, 550]
pag.moveTo(139, 390)
pag.click()
pag.click()
#subscribe
pag.moveTo(662, 482)
pag.click()
#cancel
pag.moveTo(567, 515)
pag.click()
for i in x :
	pag.moveTo(i, 390)
	pag.click()
	#subscribe
	pag.moveTo(662, 482)
	pag.click()
	#cancel
	pag.moveTo(563, 487)
	pag.click()
	#time.sleep(1)

#무한반복했을때 subscribe 된거 cancel 안하게 못함
#화면구성 나랑 똑같아야함