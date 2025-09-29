# me - this DAT
# 
# frame - the current frame
# state - True if the timeline is paused
# 
# Make sure the corresponding toggle is enabled in the Execute DAT.

def onStart():
	return

def onCreate():
	return

def onExit():
	return

# Execute DAT: exec_plot
def onFrameStart(frame):
    plot_dat = op('plot_update')
    if plot_dat and hasattr(plot_dat, 'module'):
        if hasattr(plot_dat.module, 'make_plot'):
            plot_dat.module.make_plot()
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

	