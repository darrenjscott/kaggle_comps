import seaborn as sns
import pandas as pd


def fix_series(X, col_name, period, freq):
    X = X.to_frame(name=col_name)

    X[period] = getattr(X.index, period)
    X[freq] = getattr(X.index, freq)
    return X


def seasonal_plot(X, y, period, freq, ax):
    # Adapted from Kaggle lesson
    if isinstance(X, pd.Series):
        X = fix_series(X, y, period, freq)

    palette = sns.color_palette(palette="husl", n_colors=X[period].nunique())
    ax = sns.lineplot(
        x=freq,
        y=y,
        hue=period,
        data=X,
        errorbar=('ci', False),
        ax=ax,
        palette=palette,
        legend=False
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


# Just for testing purposes
if __name__ == '__main__':
    data = {
        'values': [1.0, 0.0, 0.0, 2.0, 3.0, 0.0, 0.0, 0.0, 4.0, 5.0, 0.0, 6.0]
    }
    index = pd.period_range(start='2012-01-01', periods=len(data['values']), freq='D')
    df = pd.DataFrame(data, index=index)
    ser = df.squeeze()

    seasonal_plot(ser, 'new_col', 'week', 'dayofweek',None)
