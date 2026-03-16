#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


def run_menu():
    keys = (
        "\uf186   Suspend",
        "\uf023   Lock",
        "󰗽   Logout",
        "\uf021   Reboot",
        "\uf021   UEFI Firmware",
        "\uf011   Shutdown",
    )

    actions = (
        "systemctl suspend",
        "hyprctl --instance 0 'dispatch exec hyprlock'",
        "hyprctl dispatch exit",
        "systemctl reboot",
        "systemctl reboot --firmware-setup",
        "systemctl poweroff",
    )

    options = "\n".join(keys)
    choice = (
        os.popen(
            "echo -e '"
            + options
            + "' | wofi -d -i -p 'Power Menu' -W 600 -H 300 -k /dev/null"
        )
        .readline()
        .strip()
    )
    if choice in keys:
        os.popen(actions[keys.index(choice)])


run_menu()
