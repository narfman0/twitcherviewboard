#! /usr/bin/env python3

import webview


def main():
    webview.create_window('Twitch Stream Manager', 'https://dashboard.twitch.tv/stream-manager')
    webview.start()

if __name__ == "__main__":
    main()