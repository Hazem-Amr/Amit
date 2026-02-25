import pandas as pd

class MissingValuesHandler:
    def __init__(self, df):
        self.df = df

    def check_nulls(self):
        """
        Return a table with null counts and null ratios (%)
        """
        null_count = self.df.isnull().sum()
        null_ratio = (null_count / len(self.df)) * 100

        return pd.DataFrame({
            'null_count': null_count,
            'null_ratio_%': null_ratio
        })

    def handle_nulls(self, column, strategy):
        """
        Handle nulls for a specific column

        strategy options:
        - 'drop'
        - 'mean'
        - 'median'
        - 'mode'
        """

        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found in dataframe")

        if strategy == 'drop':
            self.df = self.df.dropna(subset=[column])

        elif strategy == 'mean':
            self.df[column] = self.df[column].fillna(self.df[column].mean())

        elif strategy == 'median':
            self.df[column] = self.df[column].fillna(self.df[column].median())

        elif strategy == 'mode':
            self.df[column] = self.df[column].fillna(self.df[column].mode()[0])

        else:
            raise ValueError(
                "Invalid strategy. Use 'drop', 'mean', 'median', or 'mode'"
            )