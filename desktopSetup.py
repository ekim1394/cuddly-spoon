#This program is meant to initialize all programs on my computer
import ctypes, win32gui, subprocess, time
# Open Programs
subprocess.Popen('cmd /c start outlook.exe')
subprocess.Popen("cmd /c start chrome https://www.youtube.com --new-window")
subprocess.Popen("cmd /c start chrome https://www.messenger.com --new-window")
subprocess.Popen("cmd /c start chrome https://www.google.com --new-window")
time.sleep(30)
# Pulls window memory location and name as well as other things.
EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

#Puts memory and name in list array
titles = []
def foreach_window(hwnd, lParam):
    if IsWindowVisible(hwnd):       
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        titles.append((hwnd, buff.value))
    return True
	
EnumWindows(EnumWindowsProc(foreach_window), 0)

def f(l, s):
    for idx, val in enumerate(l):
		if s in val[1].split():
			return idx


# OUTLOOK
email = f(titles, 'Outlook')
ctypes.windll.user32.MoveWindow(titles[email][0], -1925, 0, 1300, 1080, True)

# Messenger
fbm = f(titles, 'Messenger')
ctypes.windll.user32.MoveWindow(titles[fbm][0], -575, 0, 575, 540, True)

#Youtube
yt = f(titles, 'YouTube')
ctypes.windll.user32.MoveWindow(titles[yt][0], -575, 540, 575, 540, True)


