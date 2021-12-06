import sys
import asyncio
import websockets

        
help = """
Usage: test.py [URL] [command]

command list:
    get_volume - get current volume value
    set_volume [number] - set volume, number value range: 0 ~ 100
    toggle_play_pause - toggle play / pause
    next_track - next track
    prev_track - previous track
    toggle_shuffle - toggle shuffle
    toggle_repeat_state - toggle repeat off / single song / whole playlist
    shutdown - shutdown machine
    reboot - rebbot machine
"""

async def send_cmd(url, cmd):
    async with websockets.connect(url) as websocket:
        await websocket.send(cmd)
        recv = await websocket.recv()
        print(f'\n: {recv}\n')

def cmd_parameters():    
    if len(sys.argv) >= 3:
        url = sys.argv[1]
        cmd = ' '.join(sys.argv[2:])
        asyncio.run(send_cmd(url, cmd))
    else:
        print(help)

def main():
    cmd_parameters()

main()
