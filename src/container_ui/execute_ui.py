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
recordBtn = op('buttonToggle_record')
isRecording = recordBtn.par.Value0
cachingIndicator = op('sliderHorz_caching_indicator')

# variables
counter = 0

def onFrameStart(frame):
	global counter

	if isRecording:
		if frame == me.time.rangeEnd:
			counter += 1

		if counter % 2 == 0:
			cachingIndicator.par.Sliderlabelnames = 'Caching...'
		else:
			cachingIndicator.par.Sliderlabelnames = 'Saving images...'

		cachingIndicator.par.Value0 = (1 / me.time.rangeEnd) * me.time.frame

def onPlayStateChange(state):
	global counter
	counter = 0

	if isRecording:
		cachingIndicator.par.display = 1
	else:
		cachingIndicator.par.display = 0
