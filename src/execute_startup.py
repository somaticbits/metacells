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

import queue

# load module
common = mod('./common')

find = op('opfind1')
content = op('container_ui/container_ui_infos/text_content')

layers = {}

master_noise_layer = ''

# initialise, setup and connect
def onStart():
	content.clear()
	content.text += 'Powering up serialCore protocol:\n'
	init()
	content.text += '[✓] initialised\n'
	setLayers()
	content.text += '[✓] layers set\n'
	setNoiseResolution()
	content.text += '[✓] noise resolutions set\n'
	for layer in range(0, find.numRows - 1):
		connectPars(layer)
		content.text += '[✓] layer {0} pars connected\n'.format(layer)
	return

# initialise by assigning expressions to the individual seeds and loading table_pars
def init():
	for layer in range(0, find.numRows - 1):
		op('base_layer_{0}/noise1'.format(layer)).par.seed.expr = 'parent(2).op(\'constant_master_seed\').par.value0'
		op('base_layer_{0}/table_pars'.format(layer)).par.file = 'src/base_layer_{0}/table_pars.py'.format(layer)

# collect base_layer_0 in a dictionary
def setLayers():
	for layer in range(0, find.numRows - 1):
		layers['{0}'.format(layer)] = op('base_layer_{0}'.format(layer))
		layers['{0}_table'.format(layer)] = op('base_layer_{0}/table_pars'.format(layer))
		layers['{0}_noise'.format(layer)] = op('base_layer_{0}/noise1'.format(layer))
		layers['{0}_noise_pars'.format(layer)] = op('base_layer_{0}/null_pars_noise'.format(layer))

# set noise resolution equivalent to number of parameters
def setNoiseResolution():
	for noise in range(0, find.numRows - 1):
		layers['{0}_noise'.format(noise)].par.resolutionw = layers['{0}_table'.format(noise)].numRows - 1

# connect all pars from table to corresponding ops
def connectPars(layerNumber):
	try:
		for index in range(1, layers['{0}_table'.format(layerNumber)].numRows):
			op_base = str(layers[str(layerNumber)])
			op_sub = str(layers['{0}_table'.format(layerNumber)][index,'op'])
			par = str(layers['{0}_table'.format(layerNumber)][index,'par'])
			par_name = str(layers['{0}_table'.format(layerNumber)][index,'par_name'])
			op(op_base + '/' + op_sub).par[par].expr = 'op(\'null_pars_noise\')[\'' + par_name + '\']'
	except AttributeError:
		print('Variables undefined in base_layer_{0}'.format(layerNumber))
