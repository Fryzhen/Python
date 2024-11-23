# -*- coding: utf-8 -*-

import sys


def main(args):
    if len(args) < 2 or not args[1]:
        raise Exception("You must specify a number: python main.py 123")

    number = args[2]
    theme_name = args[1][2:]
    print("LCD display: ", number)

    themes = {
        'modern': modern,
        'classic': classic,
        'letters': letters,
        'numbers': numbers,
    }

    selected_theme = themes[theme_name]
    if not selected_theme:
        raise Exception('Unknown theme: ' + theme_name)

    lines = selected_theme(number)
    for line in lines:
        print(line)


def modern(number):
    line1 = ""
    line2 = ""
    line3 = ""
    for i in number:
        i = int(i)
        if 0 == i:
            line1 += "┌─┐ "
            line2 += "│ │ "
            line3 += "└—┘ "

        elif i == 1:
            line1 += "  ┐ "
            line2 += "  │ "
            line3 += "  │ "

        elif i == 2:
            line1 += "┌─┐ "
            line2 += "┌─┘ "
            line3 += "└—┘ "

        elif i == 3:
            line1 += "—─┐ "
            line2 += "—─┤ "
            line3 += "——┘ "

        elif i == 4:
            line1 += "││  "
            line2 += "└┼— "
            line3 += " │  "

        elif i == 5:
            line1 += "┌─┐ "
            line2 += "└─┐ "
            line3 += "└—┘ "

        elif i == 6:
            line1 += "┌─┐ "
            line2 += "├─┐ "
            line3 += "└—┘ "

        elif i == 7:
            line1 += "—─┐ "
            line2 += "  │ "
            line3 += "  │ "

        elif i == 8:
            line1 += "┌─┐ "
            line2 += "├─┤ "
            line3 += "└—┘ "

        elif i == 9:
            line1 += "┌─┐ "
            line2 += "└─┤ "
            line3 += "└—┘ "
    return [line1, line2, line3]


def classic(number):
    line1 = ""
    line2 = ""
    line3 = ""
    for i in number:
        i = int(i)
        if 0 == i:
            line1 += "._. "
            line2 += "|.| "
            line3 += "|_| "

        elif i == 1:
            line1 += "... "
            line2 += "..| "
            line3 += "..| "

        elif i == 2:
            line1 += "._. "
            line2 += "._| "
            line3 += "|_. "

        elif i == 3:
            line1 += "._. "
            line2 += "._| "
            line3 += "._| "

        elif i == 4:
            line1 += "... "
            line2 += "|_| "
            line3 += "..| "

        elif i == 5:
            line1 += "._. "
            line2 += "|_. "
            line3 += "._| "

        elif i == 6:
            line1 += "._. "
            line2 += "|_. "
            line3 += "|_| "

        elif i == 7:
            line1 += "._. "
            line2 += "..| "
            line3 += "..| "

        elif i == 8:
            line1 += "._. "
            line2 += "|_| "
            line3 += "|_| "

        elif i == 9:
            line1 += "._. "
            line2 += "|_| "
            line3 += "._| "
    return line1, line2, line3


def letters(number):
    line1 = ""
    line2 = ""
    line3 = ""
    for i in number:
        i = int(i)
        if 0 == i:
            line1 += "_____"
            line2 += "zero "
            line3 += "_____"

        elif i == 1:
            line1 += "____"
            line2 += "one "
            line3 += "____"

        elif i == 2:
            line1 += "____"
            line2 += "two "
            line3 += "____"

        elif i == 3:
            line1 += "______"
            line2 += "three "
            line3 += "______"

        elif i == 4:
            line1 += "_____"
            line2 += "four "
            line3 += "_____"

        elif i == 5:
            line1 += "_____"
            line2 += "five "
            line3 += "_____"

        elif i == 6:
            line1 += "____"
            line2 += "six "
            line3 += "____"

        elif i == 7:
            line1 += "______"
            line2 += "seven "
            line3 += "______"

        elif i == 8:
            line1 += "______"
            line2 += "eight "
            line3 += "______"

        elif i == 9:
            line1 += "_____"
            line2 += "nine "
            line3 += "_____"
    return [line1, line2, line3]


def numbers(number):
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""
    for i in number:
        i = int(i)
        if 0 == i:
            line1 += "00000  "
            line2 += "0   0  "
            line3 += "0   0  "
            line4 += "0   0  "
            line5 += "00000  "

        elif i == 1:
            line1 += "   11  "
            line2 += "  1 1  "
            line3 += "    1  "
            line4 += "    1  "
            line5 += "    1  "

        elif i == 2:
            line1 += "22222  "
            line2 += "    2  "
            line3 += "22222  "
            line4 += "2      "
            line5 += "22222  "

        elif i == 3:
            line1 += "33333  "
            line2 += "    3  "
            line3 += "33333  "
            line4 += "    3  "
            line5 += "33333  "

        elif i == 4:
            line1 += "4  4   "
            line2 += "4  4   "
            line3 += "44444  "
            line4 += "   4   "
            line5 += "   4   "

        elif i == 5:
            line1 += "55555  "
            line2 += "5      "
            line3 += "55555  "
            line4 += "    5  "
            line5 += "55555  "

        elif i == 6:
            line1 += "66666  "
            line2 += "6      "
            line3 += "66666  "
            line4 += "6   6  "
            line5 += "66666  "

        elif i == 7:
            line1 += "77777  "
            line2 += "    7  "
            line3 += "   7   "
            line4 += "  7    "
            line5 += " 7     "

        elif i == 8:
            line1 += "88888  "
            line2 += "8   8  "
            line3 += "88888  "
            line4 += "8   8  "
            line5 += "88888  "

        elif i == 9:
            line1 += "99999  "
            line2 += "9   9  "
            line3 += "99999  "
            line4 += "    9  "
            line5 += "99999  "

    return [line1, line2, line3, line4, line5]


if __name__ == "__main__":
    print(sys.argv[:])
    main(sys.argv)
