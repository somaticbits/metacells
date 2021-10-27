# me - this DAT
# scriptOp - the OP which is cooking
#
# press 'Setup Parameters' in the OP to call this function to re-create the parameters.

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

palette = parent().par.Palette

def onSetupParameters(scriptOp):
	return

# called whenever custom pulse parameter is pushed
def onPulse(par):
	return

def onCook(scriptOp):
	scriptOp.clear()

	table_rgb = scriptOp.inputs[0]

	# add colors
	scriptOp.appendRows(table_rgb.rows(palette * 4,palette * 4+1,palette * 4+2,palette * 4+3,palette * 4+4))
	#scriptOp.appendRows(table_rgb.rows([palette * 4 + i for i in range(5)]))
	# add indices
	scriptOp.insertCol([x * 0.1 for x in range(0,10,2)])
	# add alpha
	scriptOp.appendCol([1. for x in range(5)])
	# add headers
	scriptOp.insertRow(['pos','r','g','b','a'])

	return
