import ctypes
import time
import pyautogui

length = 0.1

SendInput = ctypes.windll.user32.SendInput

VK_ALT = 0x12
VK_TAB = 0x09
VK_W = 0x57
VK_CTRL = 0x00
VK_close_tab = 23

PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", PUL)
    ]

class HardwareInput(ctypes.Structure):
    _fields_ = [
        ("uMsg", ctypes.c_ulong),
        ("wParamL", ctypes.c_short),
        ("wParamH", ctypes.c_ushort)
    ]

class MouseInput(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time",ctypes.c_ulong),
        ("dwExtraInfo", PUL)
    ]

class Input_I(ctypes.Union):
    _fields_ = [
        ("ki", KeyBdInput),
        ("mi", MouseInput),
        ("hi", HardwareInput)
    ]

class Input(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ulong),
        ("ii", Input_I)
    ]
def keyDown(keyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(keyCode, 0x48, 0, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def keyUp(keyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(keyCode, 0x48, 0x0002, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def netxTab():
    pyautogui.hotkey('ctrl', 'tab')

def closeTab():
    pyautogui.hotkey('ctrl','w')

def openTab():
    pyautogui.hotkey('ctrl','t')

def previousTab():
    pyautogui.hotkey('ctrl','shift','tab')
