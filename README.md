# SpotifyPi

1. Update Raspberry Pi OS:
    ```
    $ sudo apt update
    $ sudo apt upgrade
    ```
2. Install Widevine DRM and reboot:
    ```
    $ sudo apt install libwidevinecdm0
    $ sudo reboot
    ```
3. Open Chromium, install `Spotify Web Player Hotkeys` extension, and set shortcuts:
    ![shortcuts](imgs/hotkeys.png)
    - Next track: `alt` + `shift` + `.`
    - Play/Pause: `alt` + `shift` + `p`
    - Previous track: `alt` + `shift` + `,`
    - Toggle repeat off/single song/whole playlist: `alt` + `shift` + `r`
    - Toggle shuffle: `alt` + `shift` + `s`
4. Clone this repo, and `cd` to repo directory:
    ```
    $ git clone https://github.com/wlelab/SpotifyPi.git
    $ cd SpotifyPi
    ```
5. Run `install.sh` and reboot:
    ```
    $ chmod 755 install.sh
    $ sudo ./install.sh
    $ sudo reboot
    ```



