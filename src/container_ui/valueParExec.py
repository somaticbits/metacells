# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
#
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

# reset and start timeline on render
def onValueChange(par, prev):
	# use par.eval() to get current value
	if par:
		me.time.frame = 0
		me.time.play = 1
	else:
		me.time.frame = 0
		me.time.play = 0
	return
