"""
Seaborn.objects statistical plotting custom functions.
boxplot, rangeplot
"""

import seaborn as sns
import seaborn.objects as so


def boxplot(df, x, y, color=None, alpha=0.1, marker="<"):

    if color is None:
        pcolor = "orangered"
        return (
            so.Plot(df, x=x, y=y, color=color)
            .add(so.Dots(alpha=alpha, color=".6"), so.Jitter(), so.Dodge())
            .add(
                so.Range(color=pcolor),
                so.Est("median", errorbar=("pi", 50)),
                so.Dodge(),
            )
            .add(
                so.Dot(pointsize=8, marker=marker, color=pcolor),
                so.Agg("median"),
                so.Dodge(),
            )
            .scale(color="Dark2")
            .theme({**sns.axes_style("whitegrid")})
        )
    else:
        return (
            so.Plot(df, x=x, y=y, color=color)
            .add(so.Dots(alpha=alpha, color=".6"), so.Jitter(), so.Dodge())
            .add(so.Range(), so.Est("median", errorbar=("pi", 50)), so.Dodge())
            .add(so.Dot(pointsize=8, marker=marker), so.Agg("median"), so.Dodge())
            .scale(color="Dark2")
            .theme({**sns.axes_style("whitegrid")})
        )


def rangeplot(df, x, y, color=None, alpha=0.1):

    return (
        so.Plot(df, x=x, y=y, color=color)
        .add(so.Range(), so.Est("median", errorbar=("pi", 50)), so.Dodge())
        .add(so.Dots(pointsize=8, marker="<"), so.Agg("median"), so.Dodge())
        .scale(color="Dark2")
        .theme({**sns.axes_style("whitegrid")})
    )
