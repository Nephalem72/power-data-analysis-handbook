from __future__ import annotations

import matplotlib.pyplot as plt
import seaborn as sns


COURSE_COLORS = {
    "ink": "#1f3556",
    "accent": "#3f7cac",
    "accent_light": "#89b0d9",
    "highlight": "#d95f02",
    "grid": "#d8deea",
}


def apply_course_plot_theme() -> None:
    """Apply a restrained but distinctive plotting theme for course notebooks."""
    sns.set_theme(style="whitegrid", context="notebook")
    plt.rcParams.update(
        {
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.edgecolor": COURSE_COLORS["grid"],
            "axes.labelcolor": COURSE_COLORS["ink"],
            "axes.titlecolor": COURSE_COLORS["ink"],
            "axes.titlesize": 13,
            "axes.titleweight": "semibold",
            "xtick.color": COURSE_COLORS["ink"],
            "ytick.color": COURSE_COLORS["ink"],
            "grid.color": COURSE_COLORS["grid"],
            "grid.linewidth": 0.8,
            "legend.frameon": False,
        }
    )


def format_axis(
    ax,
    *,
    title: str,
    xlabel: str,
    ylabel: str,
    subtitle: str | None = None,
) -> None:
    """Apply consistent titles and labels to a matplotlib axis."""
    ax.set_title(title, loc="left", pad=14)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if subtitle:
        ax.text(
            0,
            1.02,
            subtitle,
            transform=ax.transAxes,
            ha="left",
            va="bottom",
            fontsize=10,
            color="#50627a",
        )


def annotate_extreme(ax, x, y, label: str) -> None:
    """Annotate a notable point on the chart."""
    ax.scatter([x], [y], color=COURSE_COLORS["highlight"], s=40, zorder=3)
    ax.annotate(
        label,
        xy=(x, y),
        xytext=(8, 10),
        textcoords="offset points",
        color=COURSE_COLORS["highlight"],
        fontsize=9,
    )
