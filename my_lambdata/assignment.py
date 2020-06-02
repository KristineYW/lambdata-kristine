# TODO: Abbreviate states and un-abbreviate them in a pandas dataframe. 
import pandas as pd

def add_state_names_column(my_df):
    """
    Add a column of correspondent state names to a dataframe

    Parameters (my_df) is a Dataframe with a column called "abbrev"
    that has state abbreviations

    We are assuming that the dataframe we pass in contains a column 
    named "abbrev"

    Returns a copy of the rogiinal dataframe, with an extra column.
    """

    new_df = my_df.copy()

    names_map ={"CA": "California", 
                "CO":"Colorado", 
                "CT": "Connecticut",
                "DC":"District of Columbia",
                "TX":"Texas"}

    new_df["name "] = new_df["abbrev"].map(names_map)

    return new_df

if __name__ == "__main__":

    df = pd.DataFrame({"abbrev": ["CA","CO","CT","DC","TX"]})
    print(df.head())

    mapped_df = add_state_names_column(df)
    print(mapped_df.head())