from __future__ import annotations

from typing import Any
import altair as alt


def add_default_spec(spec: dict[str, Any]) -> None:
    print('h1')
    spec['$schema'] = 'https://vega.github.io/schema/vega-lite/v5.json'
    spec['width'] = 700
    spec['height'] = 700
    return spec


def plot(spec: dict[str, Any]) -> Any:
    return alt.Chart.from_dict(add_default_spec(spec)).interactive()