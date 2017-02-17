import volume as v
import time
length = 0.1

VK_MEDIA_PREV_PAUSE = 0xB1
VK_MEDIA_NEXT_TRACK = 0xB0

def Playnext_Music():
	v.keyDown(VK_MEDIA_NEXT_TRACK)
	time.sleep(length)
	v.keyUp(VK_MEDIA_NEXT_TRACK)

def PlayPrevious_Music():
	v.keyDown(VK_MEDIA_PREV_PAUSE)
	time.sleep(length)
	v.keyUp(VK_MEDIA_PREV_PAUSE)
