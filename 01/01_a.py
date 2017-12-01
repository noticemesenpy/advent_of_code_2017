#!/usr/bin/env python3
"""
filename.py

copyright 2017 noticemesen.py

gitlab: gitlab.com/noticemesenpy
github: github.com/noticemesenpy

********************************************************************************



********************************************************************************
"""


def main():
    """the main function"""
    ans = 0

    with open("input.txt", "r") as infile:
        puzzInp = infile.read().strip()

    for i in range(len(puzzInp) - 1):
        if int(puzzInp[i]) == int(puzzInp[i + 1]):
            ans += int(puzzInp[i])

    if int(puzzInp[-1]) == int(puzzInp[0]):
        ans += int(puzzInp[-1])

    print(ans)


if __name__ == "__main__":
    main()

