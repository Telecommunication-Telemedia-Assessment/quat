#!/usr/bin/env python3
"""
Unsorted methods
"""
"""
    This file is part of quat.
    quat is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    quat is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with quat. If not, see <http://www.gnu.org/licenses/>.

    Author: Steve Göring
"""

import datetime
import time
import json

from quat.log import *


def timeit(func):
    """
    get the required time for a function call as information on stdout, via lInfo

    example usage:

    .. code-block:: python

        @timeit
        def myfunction():
            return 42

    or

    .. code-block:: python

        def anotherfucntion():
            return 23

        timeit(anotherfucntion())

    """

    def function_wrapper(*args, **kwargs):
        start_time = time.time()
        lInfo("start {}".format(func.__name__))
        res = func(*args, **kwargs)
        overall_time = time.time() - start_time
        lInfo(
            "calculation done for {}: {} s; {}".format(
                func.__name__,
                overall_time,
                str(datetime.timedelta(seconds=overall_time)),
            )
        )
        return res

    return function_wrapper


def p_bar(iterable, total=100):
    """ progress bar
    TODO: mark that this is an internal function
    """
    step = 0
    progress = 0
    print(
        "\r"
        + colorred("[CALC ] ")
        + "[{0}] {1}%".format("#" * (progress // 5), progress),
        end="",
    )

    for i in iterable:
        progress = int(100 * step / total)
        char = "/" if step % 2 == 0 else "\\"
        print(
            "\r"
            + colorred("[CALC{0}] ".format(char))
            + "[{0}] {1}%".format("#" * (progress // 5), progress),
            end="",
        )
        yield i
        step += 1

    progress = 100
    print(
        "\r"
        + colorred("[CALC ] ")
        + "[{0}] {1}%".format("#" * (progress // 5), progress)
    )


def progress_bar(iterable, max=100):
    """ run progress bar on iterable """
    results = []
    for res in p_bar(iterable, max):
        yield res


def powerset(iterable):
    """
    returns powerset of an iterable,

    powerset([1,2,3]) --> () (1) (2) (3) (1,2) (1,3) (2,3) (1,2,3)
    from: https://stackoverflow.com/a/16915734
    """
    xs = list(iterable)
    # note we return an iterator rather than a list
    return chain.from_iterable(combinations(xs, n) for n in range(len(xs) + 1))


def align_vectors(x, y):
    """
    align the length of two vectors `x` and `y` using the min length of both
    """
    min_len = min(len(x), len(y))
    x = x[0:min_len]
    y = y[0:min_len]
    return x, y


def jdump_file(filename, jo, printing=False):
    """
    dump a json file to a filename
    """
    if printing:
        print(json.dumps(jo, indent=4, sort_keys=True))
    with open(filename, "w") as _fp:
        json.dump(jo, _fp, indent=4, sort_keys=True)


def create_colormap(start, mid, end, steps=256):
    """
    creates a color map between three color points using
    `steps` intermediate colors.

    Parameters
    ----------
    start : tuple(int)
        defined start color as tuple (R, G, B)
    mid : tuple(int)
        defined middle color as tuple (R, G, B)
    end : tuple(int)
        defined end color as tuple (R, G, B)

    Returns
    -------
    list of in total `steps` colors statring from start, to mid, to end
    """
    colors = []
    h_steps = steps // 2
    step_size = (
        (mid[0] - start[0]) / h_steps,
        (mid[1] - start[1]) / h_steps,
        (mid[2] - start[2]) / h_steps,
    )

    c_color = start
    for i in range(h_steps):
        colors.append(c_color)
        c_color = [round(c_color[i] + x) for i, x in enumerate(step_size)]

    colors.append(mid)
    step_size = (
        (end[0] - mid[0]) / h_steps,
        (end[1] - mid[1]) / h_steps,
        (end[2] - mid[2]) / h_steps,
    )

    for i in range(h_steps):
        colors.append(c_color)
        c_color = [round(c_color[i] + x) for i, x in enumerate(step_size)]
    return colors
