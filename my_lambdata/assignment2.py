# Create class for new dataframe
import pandas as pd
from scikit-learn.model_selection import train_test_split

class NewDF():
    def __init__(self, df, target, column):
        self.df = df
        self.target = target
        self.column = column
    
    @property
    def ToDF(self):
        self.df = pd.to_DataFrame(self.df)

    @property
    def df_split(self):
        train1, val = train_test_split(
            self.df, train_size=0.85, test_size=0.15, stratify=self.df[self.target], random_state=42)
        train2, test = train_test_split(
            train1, train_size=0.8, test_size=0.2, stratify=self.df[self.target], random_state=42)
        return(train2, val, test)

    @property
    def date_split(self):
        self.df[self.column] = pd.to_datetime(self.df[self.column], infer_datetime_format=True)
        new_df = self.df.copy()
        new_df['year'] = new_df[self.column].DateTimeIndex(new_df[self.column]).year
        new_df['month'] = new_df[self.column].DateTimeIndex(new_df[self.column]).month
        new_df['day'] = new_df[self.column].DateTimeIndex(new_df[self.column]).day
        new_df = new_df.drop(columns=self.column)
        return(new_df)


# if __name__ == "__main__":
