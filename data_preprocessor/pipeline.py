from .datatypes import DataTypeHandler
from .missing import MissingValuesHandler
from .outliers import OutlierHandler
from .duplicates import DuplicateHandler

class PreprocessingPipeline:
    def __init__(self, df):
        self.df = df
        self.dtypes = DataTypeHandler(df)
        self.missing = MissingValuesHandler(df)
        self.outliers = OutlierHandler(df)
        self.duplicates = DuplicateHandler(df)

    def get_data(self):
        return self.df