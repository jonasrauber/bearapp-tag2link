#!/usr/bin/env python3
import argparse
import urllib.parse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tag")
    args = parser.parse_args()
    print(link2tag(args.tag))


def link2tag(tag):
    stripped_tag = tag.strip("#")
    encoded_tag = urllib.parse.quote(stripped_tag, safe="")
    return f"[`{tag}`](bear://x-callback-url/open-tag?name={encoded_tag})"


if __name__ == "__main__":
    main()
