class DuplicateHandler:
    def __init__(self, df):
        self.df = df

    def check_duplicates(self):
        return self.df.duplicated().sum()

    def remove_duplicates(self):
        self.df.drop_duplicates(inplace=True)

    def show_duplicates(self):

        return self.df[self.df.duplicated()]