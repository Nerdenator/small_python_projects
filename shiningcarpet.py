import argparse


def main():
    # initialize parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--x_repeat", help='Number of X axis repeats')
    parser.add_argument("-y", "--y_repeat", help='Number of Y axis repeats')
    args = parser.parse_args()
    if args.x_repeat is None:
        args.x_repeat = 6
    if args.y_repeat is None:
        args.y_repeat = 4
    draw_carpet(int(args.x_repeat), int(args.y_repeat))


def draw_carpet(x, y):
    for i in range(y):
        print(r'_ \ \ \_/ __' * x)
        print(r' \ \ \___/ _' * x)
        print(r'\ \ \_____/ ' * x)
        print(r'/ / / ___ \_' * x)
        print(r'_/ / / _ \__' * x)
        print(r'__/ / / \___' * x)


if __name__ == '__main__':
    main()
