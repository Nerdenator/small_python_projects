try:
    import pyperclip
except ImportError:
    pass


def spongecase(text_string):
    spongetext = []
    last = 'lower'  # always start with a capital
    for char in text_string:
        if char.isalpha():
            if last == 'lower':
                spongetext.append(char.upper())
                last = 'upper'
            elif last == 'upper':
                spongetext.append(char.lower())
                last = 'lower'
        else:
            spongetext.append(char)
    spongetext = ''.join(spongetext)
    print(spongetext)
    try:
        pyperclip.copy(spongetext)
        print('CoPiEd SpOnGeTeXt To ClIpBoArD')
    except:
        pass
    return


if __name__ == '__main__':
    text = input('sPoNgEcAsE tHiS tExT: ')
    spongecase(text)