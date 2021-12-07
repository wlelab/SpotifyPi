import os
import re
import asyncio
import subprocess
import websockets
import pyautogui


#
# tools
#
def system_call(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')

def analyze_amixer_result(text):
    strings = [str.strip() for str in text.split('\n')]
    for s in strings:
        m = re.match(r'Front Left: Playback.+?\[(\d+?)%\]', s)
        if (m is not None) and len(m.groups()) > 0:
            print(m.group(1))
            return m.group(1)
    return 'missing'


#
# commands
#
def get_volume():
    out_text = system_call(['amixer', 'sget', 'Master'])
    result = analyze_amixer_result(out_text)
    print(f'get_volume: {result}')
    return result

def set_volume(volume):
    out_text = system_call(['amixer', 'sset', 'Master', f'{volume}%'])
    result = analyze_amixer_result(out_text)
    print(f'set_volume: {result}')
    return result

def toggle_play_pause():
    print('toggle_play_pause')
    pyautogui.hotkey('alt', 'shift', 'p')
    
def next_track():
    print('next_track')
    pyautogui.hotkey('alt', 'shift', '.')

def prev_track():
    print('prev_track')
    pyautogui.hotkey('alt', 'shift', ',')
    
def toggle_shuffle():
    print('toggle_shuffle')
    pyautogui.hotkey('alt', 'shift', 's')

def toggle_repeat_state():
    print('toggle_repeat_state')
    pyautogui.hotkey('alt', 'shift', 'r')

def shutdown():
    print('shutdown')
    os.system('sudo shutdown -h now')

def reboot():
    print('reboot')
    os.system('sudo reboot')


#
# run command
#
def run_cmd(cmd):
    print(f'cmd: {cmd}')
    if len(cmd) == 0:
        return '[error](missing)'
    name = cmd[0]
    if name == 'get_volume':
        result = get_volume()
        return f'[volume]({result})'
    elif name == 'set_volume':
        if len(cmd) == 1:
            return '[error](missing)'
        result = set_volume(cmd[1])
        return f'[volume]({result})'
    elif name == 'toggle_play_pause':
        toggle_play_pause()
        return '[toggle_play_pause](ok)'
    elif name == 'next_track':
        next_track()
        return '[next_track](ok)'
    elif name == 'prev_track':
        prev_track()
        return '[prev_track](ok)'
    elif name == 'toggle_shuffle':
        toggle_shuffle()
        return '[toggle_shuffle](ok)'
    elif name == 'toggle_repeat_state':
        toggle_repeat_state()
        return '[toggle_repeat_state](ok)'
    elif name == 'shutdown':
        shutdown()
        return '[shutdown]'
    elif name == 'reboot':
        reboot()
        return '[reboot]'
    return '[error](not_found)'


#
# websocket
#
async def handle_connection(websocket):
    try:
        connected_list.append(websocket)
        async for message in websocket:
            print(f'\nmessage: "{message}"')
            cmd = message.split()
            result = run_cmd(cmd)
            if result != '[shutdown]' or result != '[reboot]':
                for connected in connected_list:
                    await connected.send(result)
    except websockets.exceptions.ConnectionClosedError:
        print('> ConnectionClosedError')
    finally:
        connected_list.remove(websocket)

async def main():
    async with websockets.serve(handle_connection, "0.0.0.0", 9487):
        await asyncio.Future()  # run forever


#
# setup and start
#
connected_list = []
pyautogui.FAILSAFE = False
asyncio.run(main())
