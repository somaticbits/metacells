# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

# math functions
def mapTableRange(channel, val, table, mapped_table):
	for index in range(1, table.numRows):
		if channel.name == table[index, 'par_name']:
			mapped_table[index - 1, 0] = table[index, 'par_name']
			if isInteger(table[index, 'min']):
				mapped_table[index - 1, 1] = int(
					round(mapRange(val, 0, 1, table[index, 'min'], table[index, 'max'])))
			else:
				mapped_table[index - 1, 1] = mapRange(val, 0, 1, table[index, 'min'], table[index, 'max'])

def mapRange(value, inMin, inMax, outMin, outMax):
	return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))

def isInteger(n):
	try:
		float(n)
	except ValueError:
		return False
	else:
		return float(n).is_integer()


