"""A labeled seven-segment display, with each segment labeled A to G:
 __A__
|     |    Each digit in a seven-segment display:
F     B     __       __   __        __   __  __   __   __
|__G__|    |  |   |  __|  __| |__| |__  |__    | |__| |__|
|     |    |__|   | |__   __|    |  __| |__|   | |__|  __|
E     C
|__D__|
"""

def get_sev_seg_str(number, min_width=0):
    """
    Return a seven-segment display string of number. The returned string will be padded with zeros
    if it is smaller than min_width.
    """
    # Convert number to string in case it's an int or float:
    number = str(number).zfill(min_width)

    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == '.':  # render the decimal point
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue    # Skip the space in between digits.
        elif numeral == '-':    # render the negative sign:
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0':    # Render the zero
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':    # Render the one
            rows[0] += '   |'
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2':    # Render the two
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == '3':    # Render the three
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4':    # Render the four
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':    # Render the five
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == '6':    # Render the six
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numeral == '7':    # Render the seven
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8':    # Render the eight
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':    # Render the nine
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'
        # add a space (for the space in between numerals) if this isn't the last numeral:
        if i != len(number) - 1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '
    return '\n'.join(rows)

# If this program isn't being imported, display the numbers 00 to 99.
if __name__ == '__main__':
    print('This module is meant to be imported rather than run.')
    print('For example, this code:')
    print('    import sevseg')
    print('    my_number = sevseg.get_sev_seg_str(42, 3)')
    print('    print(my_number)')
    print()
    print('...will print 42, zero-padded to three digits:')
    print(' __        __ ')
    print('|  | |__|  __|')
    print('|__|    | |__ ')
