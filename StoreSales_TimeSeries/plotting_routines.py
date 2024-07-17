import seaborn as sns


def seasonal_plot(X, y, period, freq, ax):
    # Adapted from Kaggle lesson
    palette = sns.color_palette(palette="husl", n_colors=X[period].nunique())
    ax = sns.lineplot(
        x=freq,
        y=y,
        hue=period,
        data=X,
        errorbar=('ci',False),
        ax=ax,
        palette=palette,
        legend=False,
    )

    ax.set_title(f"Seasonal Plot ({period}/{freq})")
    for line, name in zip(ax.lines, X[period].unique()):
        # Get last point on each line to label it on the rhs of the plot
        y_ = line.get_ydata()[-1]
        ax.annotate(
            name,
            xy=(1, y_),
            xytext=(6, 0),
            color=line.get_color(),
            # I think the following changes xy so that x=1 takes you to the extreme rhs of the axes
            xycoords=ax.get_yaxis_transform(),
            # I think the following establishes that he text is relative to the xytext position
            textcoords="offset points",
            size=14,
            va="center"
        )
    return ax