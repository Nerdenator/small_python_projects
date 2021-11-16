import random, time

BAR = chr(9608)


def get_progress_bar(progress, total, bar_width=40):
    """
    Returns a string that represents a progress bar that has bar width bars and has
    progressed progress amount out of a total amount
    :param progress:
    :param total:
    :param bar_width:
    :return: string
    """
    progress_bar = ''
    progress_bar += '['  # create the left end of the progress bar

    # Make sure that the amount of progress is between 0 and total:
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    # Calculate the number of "bars" to display:
    number_of_bars = int((progress / total) * bar_width)

    progress_bar += BAR * number_of_bars  # Add the progress bar.
    progress_bar += ' ' * (bar_width - number_of_bars)  # add empty space
    progress_bar += ']'  # Add the right end of the progress bar.

    # Calculate the percentage complete:
    percent_complete = round(progress / total * 100, 1)
    progress_bar += ' ' + str(percent_complete) + '%'  # Add percentage

    # Add the numbers:
    progress_bar += ' ' + str(progress) + '/' + str(total)

    return progress_bar  # return the progress bar string


def main():
    bytes_downloaded = 0
    download_size = 4096
    # simulate a download
    while bytes_downloaded < download_size:
        bytes_downloaded += random.randint(0, 100)
        # get the progress bar string for this amount of progress
        bar_str = get_progress_bar(bytes_downloaded, download_size)
        # Don't print a newline at the end, and immediately flush the printed string
        # to the screen
        print(bar_str, end='', flush=True)
        time.sleep(0.2)  # Pause for a little bit
        # Print backspaces to move the text cursor to the line's start:
        print('\b' * len(bar_str), end='', flush=True)


# if the program is run (instead of imported), run the "game":
if __name__ == '__main__':
    main()
