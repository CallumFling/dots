#!/bin/bash
if ip link show wg > /dev/null 2>&1; then
    # waybar will only take very specific format results string for format-icons, and it's easier to just return our icon as text...
    echo "{\"text\": \"<span color='#0DB9D7'>󰳌</span>\", \"tooltip\": \"wg status: Up\" }"
else
    echo "{\"text\": \"<span color='#c53b53'>󰦜</span>\", \"tooltip\": \"wg status: Down\" }"
fi
