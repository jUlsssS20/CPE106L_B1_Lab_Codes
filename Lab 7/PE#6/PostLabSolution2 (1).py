"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

import pandas as pd
from hoopstatsview import HoopStatsView

def main():
    """Creates the data frame and view and starts the app."""
    stats_frame = pd.read_csv("cleanbrogdonstats.csv")
    print("Input stats:\n", stats_frame)
    stats_frame = clean_stats(stats_frame)
    print("Cleaned stats:\n", stats_frame)
    HoopStatsView(stats_frame)

def clean_stats(stats_frame):
    """
    Cleans the FG, 3PT, and FT columns of the input dataframe by splitting them into FGM and FGA columns.
    """
    unformatted_columns = [stats_frame['FG'], stats_frame['3PT'], stats_frame['FT']]
    stats_frame = stats_frame.drop(['FG', '3PT', 'FT'], axis=1)

    for column in unformatted_columns:
        column = pd.DataFrame(column)
        column_name = str(column.columns.tolist()[0])
        cleaned_columns = []

        column_names = [column_name + "M", column_name + "A"]
        for entry in column.itertuples():
            value = str(tuple(entry)[-1])
            values = value.split('-')
            cleaned_columns.append(values)

        cleaned_columns = pd.DataFrame(cleaned_columns, columns=column_names)

        # Find the index where the new columns should be inserted
        index = stats_frame.columns.tolist().index(column_name[:2] + "%")

        # Insert the new columns into the dataframe
        stats_frame.insert(index, column_names[0], cleaned_columns[column_names[0]])
        stats_frame.insert(index + 1, column_names[1], cleaned_columns[column_names[1]])

    return stats_frame

if __name__ == "__main__":
    main()