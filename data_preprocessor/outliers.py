import matplotlib.pyplot as plt

class OutlierHandler:
    def __init__(self, df):
        self.df = df

    def boxplot(self, column, title=None):
        plt.figure()
        self.df.boxplot(column=column)
        plt.title(title or f'Boxplot of {column}')
        plt.show()

    # def boxplot(self, column, title=None):
    #     fig, ax = plt.subplots()
    #     self.df.boxplot(column=column, ax=ax)
    #     ax.set_title(title or f"Boxplot of {column}")

    #     return fig
    

    def cap_iqr(self, column):
        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        self.df.loc[self.df[column] < lower, column] = lower
        self.df.loc[self.df[column] > upper, column] = upper
