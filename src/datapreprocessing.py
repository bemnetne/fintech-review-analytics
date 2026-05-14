import pandas as pd
from IPython.display import display
from pathlib import Path
def remove_nulls(df):
    """Remove rows that have any missing values. Print a summary of what was removed."""
    before = len(df)
    display(df.isna().sum())
    df = df.dropna()
    after = len(df)
    removed = before - after
    if removed > 0:
        print(f"Removed {removed} row(s) with missing values. {after} rows remaining.")
    else:
        print(f"No missing values found. All {after} rows kept.")
    return df
def fill_nulls(df):
    """
    Fill missing values using forward fill.
    """

    if df.isnull().values.any():

        missing_count = df.isnull().sum().sum()

        print(
            f"Found {missing_count} missing values. "
            "Filling with forward fill."
        )

        df = df.ffill()

    else:
        print("No missing values found.")

    return df
def show_duplicates(df):
    """Remove rows that have any missing values. Print a summary of what was removed."""
    # dup_count = df.duplicated().sum()
    dup_count = df.duplicated().sum()
    print("Number of duplicate rows:", dup_count)
    duplicates = df[df.duplicated(keep=False)]
    print(duplicates)
    return df
def remove_duplicates(df):
    """
    Remove duplicate reviews using review_id.
    """

    initial_count = len(df)

    df = df.drop_duplicates(subset=["review_id"])

    removed_count = initial_count - len(df)

    print(f"Removed {removed_count} duplicate reviews.")

    return df
def handle_missing_values(df):
    """
    Remove rows with missing review text or rating.
    """

    initial_count = len(df)

    df = df.dropna(subset=["review_text", "rating"])

    removed_count = initial_count - len(df)

    print(f"Removed {removed_count} rows with missing values.")

    return df


def normalize_dates(df):
    """
    Convert review dates to YYYY-MM-DD format.
    """

    df["review_date"] = pd.to_datetime(df["review_date"])

    df["review_date"] = df["review_date"].dt.strftime("%Y-%m-%d")

    return df


def rename_columns(df):
    """
    Rename columns according to project requirements.
    """

    df = df.rename(columns={
        "review_text": "review",
        "review_date": "date",
        "bank_name": "bank"
    })

    return df


# -----------------------------------
# Save Dataset Function
# -----------------------------------

def save_dataset(df, filename):
    """
    Save DataFrame to CSV.
    """
    print(filename)
    df.to_csv(f"../data/{filename}", index=False)
    # df.to_csv(f"../data/{filename}", index=False)

    print(f"\nDataset saved as {filename}")
# def save_dataset(df, filename):

#     path = Path("../data") / filename

#     df.to_csv(path, index=False)

#     print(f"Saved to: {path.resolve()}")