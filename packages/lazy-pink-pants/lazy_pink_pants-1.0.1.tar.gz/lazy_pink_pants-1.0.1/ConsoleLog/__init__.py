#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time


class ConsoleLog:

    def __init__(self, text: str, start: str = '', end: str = '', verbose: str = 'vv', color: str = None,
                 bgcolor: str = None, underlined: bool = False, bold: bool = False, strikethrough: bool = False,
                 stdout: bool = False, linebrake: bool = True, rewrite_previous_line: bool = False,
                 time_to_read: int = 0):
        style_array = []
        rewrite = ''
        style = ''
        verbose_dict = {'v': 3, 'vv': 2, 'vvv': 1, 'debug': 0}
        verbose_level = verbose_dict[verbose]
        log_level = 2  # NEED TO SPECIFY IN TERMINAL !!!

        if verbose_level <= log_level:
            if color is not None:
                color_dict = {
                    'black': '30',
                    'red': '31',
                    'green': '32',
                    'orange': '33',
                    'blue': '34',
                    'purple': '35',
                    'cyan': '36',
                    'white': '37',
                    'darkgrey': '90',
                    'lightred': '91',
                    'lightgreen': '92',
                    'yellow': '93',
                    'lightblue': '94',
                    'pink': '95',
                    'lightcyan': '96'
                }
                number_of_color = color_dict[color]
                style_array.append(number_of_color)
            if bgcolor is not None:
                bgcolor_dict = {
                    'black': '40',
                    'red': '41',
                    'green': '42',
                    'orange': '43',
                    'blue': '44',
                    'purple': '45',
                    'cyan': '46',
                    'lightgrey': '47'
                }
                number_of_bgcolor = bgcolor_dict[bgcolor]
                style_array.append(number_of_bgcolor)
            if underlined:
                style_array.append('4')
            if bold:
                style_array.append('1')
            if strikethrough:
                style_array.append('9')
            if linebrake:
                end = f'{end}\n'
            if rewrite_previous_line:
                cursor_up_one_line = '\x1b[1A'
                erase_line = '\x1b[2K'
                rewrite = cursor_up_one_line + erase_line

            if len(style_array) != 0:
                for style_element in style_array:
                    style = style + style_element + ';'
                style = style[0:len(style) - 1]  # -1 is to remove the last ;
                print(f'\33[{style}m{rewrite}{start}{text}{end}\33[0m', end='')
            elif stdout:
                print('STDOUT is under developing')
            else:
                print(f'{rewrite}{start}{text}{end}', end='')
        time.sleep(time_to_read)

    def __repr__(self):
        Log.error('<LOG CLASS HAS NO RETURNED OBJECT!>')

    @classmethod
    def success(cls, text: str, verbose: str = 'vv', start: str = '', mark: str = '!', end: str = '',
                rewrite_previous_line: bool = False, time_to_read: int = 0):
        cls(text=f'{start}[{mark}] {text}{end}', verbose=verbose, color='green', bgcolor=None, underlined=False,
            bold=True, strikethrough=False, stdout=False, rewrite_previous_line=rewrite_previous_line,
            time_to_read=time_to_read)

    @classmethod
    def error(cls, text: str, verbose: str = 'vv', start: str = '', mark: str = '-', end: str = '',
              rewrite_previous_line: bool = False, time_to_read: int = 0):
        cls(text=f'{start}[{mark}] {text}{end}', verbose=verbose, color='red', bgcolor=None, underlined=False,
            bold=True, strikethrough=False, stdout=False, rewrite_previous_line=rewrite_previous_line,
            time_to_read=time_to_read)

    @classmethod
    def warning(cls, text: str, verbose: str = 'vv', start: str = '', mark: str = '!', end: str = '',
                rewrite_previous_line: bool = False, time_to_read: int = 0):
        cls(text=f'{start}[{mark}] {text}{end}', verbose=verbose, color='yellow', bgcolor=None, underlined=False,
            bold=True, strikethrough=False, stdout=False, rewrite_previous_line=rewrite_previous_line,
            time_to_read=time_to_read)

    @classmethod
    def system_default(cls, text: str, start: str = '', end: str = '', verbose: str = 'vv',
                       rewrite_previous_line: bool = False, time_to_read: int = 0):
        cls(text=f'{start}{text}{end}', verbose=verbose, color=None, bgcolor=None, underlined=False, bold=False,
            strikethrough=False, stdout=False, rewrite_previous_line=rewrite_previous_line, time_to_read=time_to_read)
