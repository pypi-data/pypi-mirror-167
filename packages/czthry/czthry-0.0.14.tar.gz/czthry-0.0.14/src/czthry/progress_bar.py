from progressbar import ProgressBar
from progressbar import Percentage
from progressbar import AnimatedMarker
from progressbar import Bar
from progressbar import Timer


markers_moon = '🌑🌒🌓🌔🌕🌖🌗🌘'


def make_loading_indicator(marker=None):
    if marker:
        return ProgressBar(widgets=[AnimatedMarker(markers=marker), ' ', Timer()]).start()
    else:
        return ProgressBar(widgets=[AnimatedMarker(), ' ', Timer()]).start()


def make_progress_bar(total, bar_char='.'):
    return ProgressBar(widgets=[Percentage(), ' ', Bar(bar_char), ' ', Timer()], maxval=total).start()


if __name__ == '__main__':
    pass
