#!/usr/bin/env python3
"""
Helpers for parallel processing
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

from multiprocessing import Pool
import multiprocessing


def run_parallel_by_grouping(items, function, arguments, num_cpus=8):
    """
    devides items to num_cpus groups and
    applies function with each group + arguments in parallel threads
    """
    items = sorted(items)
    # build group of items that are matching number of cpus
    groups = []
    length = len(items) // multiprocessing.cpu_count()
    for x in range(0, len(items), length):
        groups.append(items[x : x + length])
    # add for each group the shared arguments
    params = [tuple([item_group] + list(arguments)) for item_group in groups]
    # run parallel
    pool = Pool(processes=num_cpus)
    return pool.starmap(function, params)


def run_parallel(items, function, arguments=[], num_cpus=8, multi_item=False):
    """
    run a function call parallel, for each item

    Parameters
    ----------
    items : list
        list of items passed to function
    function : function name
        function that should be applied on each item
    arguments : list
        constant arguments that are passed to function
    num_cpus : int
        number of cpu's that should be used
    multi_item : bool
        in case multi_item is true, it is assumed each item is a list

    Returns
    -------
    results of function performed on all items as a list
    """
    if multi_item:
        params = [tuple(list(i) + arguments) for i in items]
    else:
        params = [tuple([i] + arguments) for i in items]
    # run parallel
    pool = Pool(processes=num_cpus)
    res = pool.starmap(function, params)
    return res
