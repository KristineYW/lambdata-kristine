# my_lambdata/my_mod.py

from sklearn.model_selection import train_test_split
import pandas as pd


def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100

# Split a dataframe into train, val, and test sets


def df_split(df, target):
    train1, val = train_test_split(
        df, train_size=0.85, test_size=0.15, stratify=df[target], random_state=42)
    train2, test = train_test_split(
        train1, train_size=0.8, test_size=0.2, stratify=df[target], random_state=42)
    return(train2, val, test)

# Assign datetime datatype to a column and then split into year, month,
# and day columns


def date_split(df, column):
    df[column] = pd.to_datetime(df[column], infer_datetime_format=True)
    new_df = df.copy()
    new_df['year'] = new_df[column].DateTimeIndex(new_df[column]).year
    new_df['month'] = new_df[column].DateTimeIndex(new_df[column]).month
    new_df['day'] = new_df[column].DateTimeIndex(new_df[column]).day
    new_df = new_df.drop(columns=column)
    return(new_df)


# this code breaks our ability to import enlarge from other files, if left
# in the global scope:
if __name__ == "__main__":
    #     # only run the code below IF this script is invoked from the command-line
    #     # not if it is imported from another script
    print("HELLO")
    y = int(input("Please choose a number: "))
    print(y, enlarge(y))
