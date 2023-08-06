import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime

from makefig.config import (
    default_standard_axes,
    default_axis_positions,
    default_label_positions,
)
from makefig.format_axis import format_axis

date_str = datetime.now().strftime("%Y%m%d")

mm_per_point = 0.352778
inches_per_mm = 0.0393701
a4_size = (8.27, 11.69)


def a4figure(ori="portrait"):

    if ori == "portrait":
        h_fig = plt.figure(figsize=a4_size)
    else:
        h_fig = plt.figure(figsize=a4_size[::-1])

    return h_fig


def create_axis(axis_position=None, fig=None):

    # create figure
    if fig is None:
        fig = a4figure()
    else:
        plt.figure(fig.number)

    if axis_position is None:
        axis_position = [65, 118.5, 80, 60]

    ax_pos = mmpos2normpos(axis_position)
    ax = fig.add_axes(ax_pos)

    return fig, ax


def mm2inches(mm):
    return inches_per_mm * mm


def mmpos2normpos(pos):

    from_left_mm, from_bottom_mm, width_mm, height_mm = pos

    from_left_inches = mm2inches(from_left_mm)
    from_bottom_inches = mm2inches(from_bottom_mm)
    width_inches = mm2inches(width_mm)
    height_inches = mm2inches(height_mm)

    from_left_norm = from_left_inches / a4_size[0]
    from_bottom_norm = from_bottom_inches / a4_size[1]
    width_norm = width_inches / a4_size[0]
    height_norm = height_inches / a4_size[1]

    return [from_left_norm, from_bottom_norm, width_norm, height_norm]


def add_figure_labels(h_fig, labels):
    for letter in labels:
        pos = mmpos2normpos(labels[letter])
        h_fig.text(
            pos[0],
            pos[1],
            letter,
            color="k",
            horizontalalignment="left",
            verticalalignment="bottom",
            fontsize=18,
            fontweight="bold",
        )


def add_axes(h_fig, axis_positions):
    axes_dict = dict.fromkeys(axis_positions)
    for panel_id in axis_positions:
        ax_pos = mmpos2normpos(axis_positions[panel_id])
        axes_dict[panel_id] = h_fig.add_axes(ax_pos)
    return axes_dict


def make_figure(
    label_positions=default_label_positions,
    axis_positions=default_axis_positions,
    axes=default_standard_axes,
):

    mpl.rcParams[
        "pdf.fonttype"
    ] = 42  # save text elements as text and not shapes
    mpl.rcParams["font.sans-serif"] = "Arial"
    mpl.rcParams["font.family"] = "sans-serif"

    h_fig = a4figure()
    add_figure_labels(h_fig, label_positions)
    axes_dict = add_axes(h_fig, axis_positions)

    if axes is not None:
        for panel_id in axes:
            format_axis(axes_dict[panel_id])

    return h_fig, axes_dict
