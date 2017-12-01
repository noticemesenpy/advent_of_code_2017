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
    lst = []

    with open("input.txt", "r") as infile:
        puzzInp = infile.read().strip()

    for i in range(len(puzzInp)):
        lst.append(int(puzzInp[i]))

    a = lst[:len(lst) // 2]
    b = lst[len(lst) // 2:]

    for i in range(len(a)):
        if a[i] == b[i]:
            ans += a[i] * 2

    print(ans)


if __name__ == "__main__":
    main()

