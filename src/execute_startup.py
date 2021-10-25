# me - this DAT
#
# frame - the current frame
# state - True if the timeline is paused
#
# Make sure the corresponding toggle is enabled in the Execute DAT.

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

op_find = op('opfind1')
layers = {}

master_noise_layer = ''

# initialise, setup and connect
def onStart():
	init()
	print('✓ initiated')
	setLayers()
	print('✓ layers set')
	setNoiseResolution()
	print('✓ noise resolutions set')
	for layer in range(0, op_find.numRows - 1):
		connectPars(layer)
		print('✓ layer {0} pars connected'.format(layer))

	return

# initialise by assigning expressions to the individual seeds
def init():
	for layer in range(0, op_find.numRows - 1):
		op('base_layer_{0}/noise1'.format(layer)).par.seed.expr = 'parent(2).op(\'constant_master_seed\').par.value0'


# collect base_layer_0 in a dictionary
def setLayers():
	for layer in range(0, op_find.numRows - 1):
		layers['{0}'.format(layer)] = op('base_layer_{0}'.format(layer))
		layers['{0}_table'.format(layer)] = op('base_layer_{0}/table_pars'.format(layer))
		layers['{0}_noise'.format(layer)] = op('base_layer_{0}/noise1'.format(layer))
		layers['{0}_noise_pars'.format(layer)] = op('base_layer_{0}/null_pars_noise'.format(layer))

# set noise resolution equivalent to number of parameters
def setNoiseResolution():
	for noise in range(0, op_find.numRows - 1):
		layers['{0}_noise'.format(noise)].par.resolutionw = layers['{0}_table'.format(noise)].numRows - 1

# connect all pars from table to corresponding ops
def connectPars(layerNumber):
	for index in range(1, layers['{0}_table'.format(layerNumber)].numRows):
		op_base = str(layers[str(layerNumber)])
		op_sub = str(layers['{0}_table'.format(layerNumber)][index,'op'])
		par = str(layers['{0}_table'.format(layerNumber)][index,'par'])
		par_name = str(layers['{0}_table'.format(layerNumber)][index,'par_name'])
		print(index, par, par_name)
		op(op_base + '/' + op_sub).par[par].expr = 'op(\'null_pars_noise\')[\'' + par_name + '\']'
