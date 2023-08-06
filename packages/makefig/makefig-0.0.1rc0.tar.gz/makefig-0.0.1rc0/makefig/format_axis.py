def format_axis(ax):

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_color("black")
    ax.spines["bottom"].set_color("black")

    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")

    ax.grid(False)

    ax.yaxis.label.set_fontsize(10)
    ax.xaxis.label.set_fontsize(10)
    for item in ax.get_yticklabels() + ax.get_xticklabels():
        item.set_fontsize(8)
