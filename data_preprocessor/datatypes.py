import pandas as pd

class DataTypeHandler:
    def __init__(self, df):
        self.df = df

    def check_dtypes(self, dtypes=None):
        """
        Return dataframe dtypes or columns filtered by dtype(s)

        Parameters
        ----------
        dtypes : str or list of str, optional
            Examples: 'object', 'int64', 'float64', 'datetime64[ns]'

        Returns
        -------
        pandas.Series or pandas.Index
        """
        # Case 1: no dtype passed → return all dtypes
        if dtypes is None:
            return self.df.dtypes

        # Case 2: dtype(s) passed → return column names
        return self.df.select_dtypes(include=dtypes).columns

    def convert_dtype(self, column, dtype):
        """
        Convert a column to a specified dtype
        Example dtype: 'category', 'int', 'float', 'datetime'
        """
        if dtype == 'datetime':
            self.df[column] = pd.to_datetime(self.df[column], errors='coerce')
        else:
            self.df[column] = self.df[column].astype(dtype)


    def get_columns_dtypes(self, columns):
        """
        Return data types for specific column(s)

        Parameters
        ----------
        columns : str or list of str

        Returns
        -------
        pandas.Series
        """
    # Convert single column to list
        if isinstance(columns, str):
            columns = [columns]

        # Validate columns
        missing = [col for col in columns if col not in self.df.columns]
        if missing:
            raise ValueError(f"Column(s) not found: {missing}")

        return self.df[columns].dtypes