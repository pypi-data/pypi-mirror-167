# SPDX-FileCopyrightText: 2022-present niits <38934471+niits@users.noreply.github.com>
#
# SPDX-License-Identifier: MIT
from typing import List, Tuple

import numpy as np
from nptyping import Int, NDArray, Shape


def consecutive(
    data: NDArray[Shape["*"], Int], step_size: int = 0
) -> NDArray[Shape["*, *"], Int]:
    return np.split(data, np.where(np.diff(data) != step_size)[0] + 1)


def find_range(data: NDArray[Shape["*"], Int]) -> List[Tuple[int, int]]:
    index = 0
    ranges = []
    for element_range in consecutive(data):
        if element_range[0]:
            ranges.append((index, index + len(element_range)))
        index += len(element_range)
    return ranges


def sort_by_line(
    data: NDArray[Shape["*, 4, 2"], Int], height: int
) -> List[NDArray[Shape["*, 4, 2"], Int]]:

    if len(data) == 0:
        return [data]

    vertical_ruler = np.zeros(height)

    y_max_list = np.array([])
    for poly in data:
        _, y_min = np.min(poly, axis=0)
        _, y_max = np.max(poly, axis=0)
        vertical_ruler[y_min:y_max] = 1
        y_max_list = np.append(y_max_list, y_max)

    lines = find_range(vertical_ruler)

    line_groups = []

    for (_, y_max) in lines:
        indexes = y_max_list <= y_max

        boxes = data[indexes]
        boxes = sorted(boxes, key=lambda x: np.min(x, axis=0)[0])
        line_groups.append(boxes)

        data = data[~indexes]
        y_max_list = y_max_list[~indexes]
    return line_groups
