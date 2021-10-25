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

console = op('text_console')
masterSeed = op('constant_master_seed')
exportNull = op('null_export')
name = 'serialCore'

counter = 0
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

	rootFolder = os.path.realpath(str(op('folder1').par.rootfolder))
	seedFolder = os.path.join(rootFolder, name + '.')
	seedFolder += str(seed)

	if counter % 2 != 0:
		exportNull.save(os.path.join(seedFolder, name) + '.' + str(seed) + '.' + str(int(frame)) + '.tif', createFolders = True)
		if frame == 1.0:
			console.par.text += '[✓] saving img sequence: serialCore.{0}\n'.format(seed)

	if frame == me.time.rangeEnd:
		if counter % 2 != 0:
			console.par.text += '[✓] rendering: serialCore.{0}.mp4'.format(seed)
			cmd = "./ffmpeg/bin/ffmpeg.exe -y -framerate 60 -i " + seedFolder + "/serialCore." + str(seed) +".%d.tif -c:v libx264 -crf 18 -pix_fmt yuv420p ./render/video/serialCore." + str(seed) + ".mp4"
			process = subprocess.Popen(cmd, shell=False)
			seed += 1
			masterSeed.par.value0 = seed
			# result = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True)
			# print(result.returncode, result.stdout, result.stderr)'
		counter += 1

	return

def onFrameEnd(frame):
	return

def onPlayStateChange(state):
	return

def onDeviceChange():
	return

def onProjectPreSave():
	return

def onProjectPostSave():
	return
