import pandas as pd
from sklearn.model_selection import GroupShuffleSplit, train_test_split

def format_raw_df(df: pd.DataFrame) -> pd.DataFrame:
    df["PostTypeId"] = df["PostTypeId"].astype(int)
    df["Id"] = df["Id"].astype(int)
    df["AnswerCount"] = df["AnswerCount"].fillna(-1).astype(int)
    df["OwnerUserId"] = df["OwnerUserId"].fillna(-1).astype(int)
    df.set_index("Id", inplace=True, drop=False)
    df["is_question"] = df["PostTypeId"] == 1

    df = df.join(
        df[["Id", "Title", "body_text", "Score", "AcceptedAnswerId"]],
        on="ParentId",
        how="left",
        rsuffix="_question"
    )

    return df

def get_random_train_test_split(df: pd.DataFrame, test_size=0.2, random_state=42):
    """
    Split the DataFrame into random train and test sets.
    :param df: DataFrame to split.
    :param test_size: Proportion of the dataset to include in the test split.
    :param random_state: Random seed for reproducibility.
    :return: Tuple of train and test DataFrames.
    """
    
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state)
    return train_df, test_df

def get_split_by_author(
        posts, author_id_column="OwnerUserId", test_size=0.2, random_state=42
):
    splitter = GroupShuffleSplit(
        n_splits=1, test_size=test_size, random_state=random_state
    )

    splits = splitter.split(posts, groups=posts[author_id_column])
    train_indices, test_indices = next(splits)
    train_df = posts.iloc[train_indices, :]
    test_df = posts.iloc[test_indices, :]
    return train_df, test_df