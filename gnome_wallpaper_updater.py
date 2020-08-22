#!/usr/bin/python3
from requests import get
import os
import subprocess
import sys
import shutil

DESTINATION_FILE = "latest_wallpaper"


def download(url, file_name):
    print(f'Downloading {url} to {file_name}')
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)


def print_lines(lines):
    for line in lines:
        print(line)


def execute(cmd):
    cmd_array = cmd.split()
    return subprocess.Popen(cmd_array,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True)


def print_process_output(process):
    while True:
        process_exit_value = process.poll()
        if process_exit_value is not None:
            print(f'process_exit_value={process_exit_value}')
            print("STDOUT")
            if process_exit_value == 0:
                print_lines(process.stdout.readlines())
            else:
                print_lines(process.stdout.readlines())
                print("STDERR")
                print_lines(process.stderr.readlines())
            return process_exit_value


os.chdir("/tmp")
url = sys.argv[1]
if len(sys.argv) >= 3:
    picture_option = sys.argv[2]
else:
    picture_option = "scaled"

print(f'reset_picture_option={print_process_output(execute("gsettings reset org.gnome.desktop.background picture-options"))}')
scale_cmd = f'gsettings set org.gnome.desktop.background picture-options \'{picture_option}\''
print(f'scale_cmd={scale_cmd}')
scale_process = execute(scale_cmd)
print_process_output(scale_process)
print(f'picture_option={print_process_output(execute("gsettings get org.gnome.desktop.background picture-options"))}')
if scale_process.poll() == 0:
    if not url.startswith("http"):
        shutil.copyfile(url, f'./{DESTINATION_FILE}')
    else:
        download(url, f'./{DESTINATION_FILE}')
    picture_uri_cmd = f'gsettings set org.gnome.desktop.background picture-uri file:///tmp/{DESTINATION_FILE}'
    print(f'picture_uri_cmd={picture_uri_cmd}')
    print_process_output(execute(picture_uri_cmd))


