import re
# me - this DAT
# scriptOp - the OP which is cooking
#
# press 'Setup Parameters' in the OP to call this function to re-create the parameters.

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onSetupParameters(scriptOp):
	scriptOp.copy(scriptOp.inputs[0])

	for i, row in enumerate(scriptOp.rows()):
		for col in scriptOp.cols():
			op('table_rgb').appendRow(col[int(i-1)].val.split())

	# TODO: add library processing indicator
	# page = scriptOp.appendCustomPage('Custom')
	# p = page.appendFloat('Valuea', label='Value A')
	return

# called whenever custom pulse parameter is pushed
def onPulse(par):
	return

def onCook(scriptOp):
	return
