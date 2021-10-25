# me - this DAT
#
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
#
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

table_pars = op('table_pars')
table_pars_mapped = op('table_pars_mapped')

def onOffToOn(channel, sampleIndex, val, prev):
	return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	for index in range(table_pars.numRows - 1):
		if channel.name == table_pars[index,'par_name']:
			table_pars_mapped[index - 1,0] = table_pars[index,'par_name']
			table_pars_mapped[index - 1,1] = mapRange(val, 0, 1, table_pars[index,'min'], table_pars[index,'max'])

	return

# common functions
def mapRange(value, inMin, inMax, outMin, outMax):
    return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))

def isInteger(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).isInteger()
