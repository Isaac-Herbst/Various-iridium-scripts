import subprocess
import argparse
import os

def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]
    return urls

def open_urls_in_iridium(urls, iridium_path):
    try:
        subprocess.Popen([iridium_path, '--new-instance', '--new-window'] + urls, shell=True)
    except FileNotFoundError:
        print(f"Error: Could not find the Iridium executable at '{iridium_path}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Open URLs in Iridium Browser")
    parser.add_argument('file_path', help="Path to the file containing URLs")
    parser.add_argument('iridium_path', help="Full path to the Iridium executable")
    args = parser.parse_args()
    
    if not os.path.isfile(args.iridium_path):
        print(f"Error: Iridium executable not found at '{args.iridium_path}'")
    elif not os.path.isfile(args.file_path):
        print(f"Error: File not found at '{args.file_path}'")
    else:
        urls = read_urls_from_file(args.file_path)
        if urls:
            open_urls_in_iridium(urls, args.iridium_path)
            print(f"Opened {len(urls)} URLs in a single new window in Iridium.")
        else:
            print("No URLs found in the file.")
