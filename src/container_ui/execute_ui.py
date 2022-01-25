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

# TD ops
toggleRender = op('container_ui_infos/buttonToggle_render')
isRecording = toggleRender.par.Value0
cachingIndicator = op('container_ui_infos/sliderHorz_caching_indicator')

# variables
counter = 1

def onStart():
	return

def onFrameStart(frame):
	global counter

	if isRecording:
		if frame == me.time.rangeEnd:
			counter += 1

		if counter % 3 != 0 and counter % 2 != 0:
			cachingIndicator.par.Sliderlabelnames = 'caching...1/2'
		if counter % 3 != 0 and counter % 2 == 0:
			cachingIndicator.par.Sliderlabelnames = 'caching...2/2'
		if counter % 3 == 0:
			cachingIndicator.par.Sliderlabelnames = 'saving...'

		cachingIndicator.par.Value0 = (1 / me.time.rangeEnd) * me.time.frame
	return

def onPlayStateChange(state):
	global counter
	counter = 1

	# if not state:
	# 	toggleRender.par.Value0 = 0

	if isRecording:
		cachingIndicator.par.display = 1
	else:
		cachingIndicator.par.display = 0
	return
