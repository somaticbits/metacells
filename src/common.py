# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

# global variables for base_layer_0
table_pars = op('table_pars')
table_pars_mapped = op('table_pars_mapped')

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