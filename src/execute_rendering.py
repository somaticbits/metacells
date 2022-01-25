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

import os
import subprocess
from subprocess import run, PIPE

from datetime import datetime

# settings
ffmpegPath = os.path.join(os.curdir, 'ffmpeg', 'bin', 'ffmpeg.exe')

# TD ops
isRecording = op('container_ui/container_main_ui/container_ui_infos/buttonToggle_render').par.Value0
content = op('container_ui/container_main_ui/container_ui_infos/text_content')
masterSeed = op('constant_master_seed')
exportNull = op('null_export')

# variables
name = 'serialCore'
counter = 1
seed = 0

def onStart():

	return

def onCreate():
	return

def onExit():
	return

def onFrameStart(frame):
	global counter
	global seed

	seed = int(op('constant_master_seed')['seed'])

	renderFolder = os.path.join(os.curdir, 'render')
	imgFolder = os.path.join(renderFolder, 'img-sequence')
	videoFolder = os.path.join(renderFolder, 'video')
	hashFolder = os.path.join(renderFolder, 'hashes')

	seedFolder = os.path.join(imgFolder, name)
	seedFolder += '.{}'.format(str(seed))

	if isRecording:
		# save individual images on frameStart on second timeline pass
		if counter % 3 == 0 and counter != 1:
			exportNull.save(os.path.join(seedFolder, name) + '.{0}.{1}.tif'.format(str(seed), str(int(frame))), createFolders = True)
			if frame == 1.0:
				content.text += '[✓] saving img sequence: serialCore.{0}\n'.format(seed)

		# render image sequence to video once timeline is finished on second timeline pass
		# iterate to next seed
		if frame == me.time.rangeEnd:
			if counter % 3 == 0 and counter != 1:
				content.text += '[✓] rendering: serialCore.{0}.mp4\n'.format(seed)
				render = '{0} -hide_banner -y -framerate 60 -i {1}.{2}.%d.tif -c:v libx264 -crf 18 -pix_fmt yuv420p {3}.{2}.mp4'\
					.format(ffmpegPath, os.path.join(seedFolder, name), str(seed), os.path.join(videoFolder, name))
				subprocess.run(render, shell=False)

				hash = '{0} -hide_banner -y -i {3}.{1}.mp4 -f hash {2}.{1}.sha256'\
					.format(ffmpegPath, str(seed), os.path.join(hashFolder, name), os.path.join(videoFolder, name))
				subprocess.Popen(hash, shell=False)

				seed += 1
				masterSeed.par.value0 = seed
			counter += 1

	return

def onFrameEnd(frame):
	return

def onPlayStateChange(state):
	global counter
	global seed
	counter = 1

	if isRecording and state:
		project.realTime = False
		content.text += 'Render protocol initiated\nTime: {0}\n'.format(datetime.now())
	else:
		project.realTime = True
		op('constant_master_seed').par.value0 = 0
	return

def onDeviceChange():
	return

def onProjectPreSave():
	return

def onProjectPostSave():
	return
