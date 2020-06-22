import piplates.TINKERplate as TINK
import time

TINK.openMETER(1)           #Create a display meter on the screen

while(True):
	pot=TINK.getPOT(0,4)
	TINK.setMETER(pot, ' ','Water Level:')
	time.sleep(.5)
	
