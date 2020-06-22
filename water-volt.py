import piplates.TINKERplate as TINK
import time

TINK.openMETER(1)           #Create a display meter on the screen

while(True):
	pot=TINK.getADC(0,4)
	TINK.setMETER(pot, 'Level','Water:')
	time.sleep(.5)
	
