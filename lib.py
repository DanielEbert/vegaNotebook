from __future__ import annotations

from typing import Any
import altair as alt


def add_default_spec(spec: dict[str, Any]) -> None:
    spec['$schema'] = 'https://vega.github.io/schema/vega-lite/v5.json'
    spec['width'] = 700
    spec['height'] = 700
    return spec


def plot(spec: dict[str, Any]) -> Any:
    return alt.Chart.from_dict(add_default_spec(spec)).interactive()


def find_smallest_square(x1, y1, x2, y2, padding: int = 2):
    # width and height of output rectangle
    width = x2 - x1
    height = y2 - y1

    side_length = max(width, height)

    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2

    square_x1 = center_x - side_length / 2 - padding
    square_x2 = center_x + side_length / 2 + padding
    square_y1 = center_y - side_length / 2 - padding
    square_y2 = center_y + side_length / 2 + padding

    return (square_x1, square_y1, square_x2, square_y2)


def same_xy_scaling(spec: dict[str, Any], data: Any) -> dict[str, Any]:
    min_x, min_y, max_x, max_y = find_smallest_square(min(data['x']), min(data['y']), max(data['x']), max(data['y']))

    spec['encoding']['x']['scale'] = {'domain': [min_x, max_x]}
    spec['encoding']['y']['scale'] = {'domain': [min_y, max_y]}

    return spec
