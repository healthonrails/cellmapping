import pandas as pd
import argparse
import os


def read_csv(file_path):
    """
    Read a CSV file and return a DataFrame.

    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing the CSV data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    return pd.read_csv(file_path)


def map_brain_region_ids(all_points_df, brain_regions_df):
    """
    Map brain region IDs from brain_regions_df to all_points_df.

    Parameters:
    all_points_df (pd.DataFrame): DataFrame containing all points.
    brain_regions_df (pd.DataFrame): DataFrame containing brain regions.

    Returns:
    pd.DataFrame: Updated DataFrame with brain_region_id column.
    """
    brain_regions_dict = brain_regions_df.set_index('name')['id'].to_dict()
    all_points_df['brain_region_id'] = all_points_df['structure_name'].map(
        brain_regions_dict)
    return all_points_df


def save_to_csv(df, output_file):
    """
    Save DataFrame to a CSV file.

    Parameters:
    df (pd.DataFrame): DataFrame to save.
    output_file (str): Path to the output CSV file.
    """
    df.to_csv(output_file, index=False)
    print(f"DataFrame saved to {output_file}")


def main(brain_regions_file, all_points_file, output_file):
    """
    Main function to read CSV files, map brain region IDs, and save the updated DataFrame.

    Parameters:
    brain_regions_file (str): Path to the brain regions CSV file.
    all_points_file (str): Path to the all points CSV file.
    output_file (str): Path to the output CSV file.
    """
    brain_regions_df = read_csv(brain_regions_file)
    all_points_df = read_csv(all_points_file)
    updated_df = map_brain_region_ids(all_points_df, brain_regions_df)
    save_to_csv(updated_df, output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Map brain region IDs to all points and save the updated DataFrame.")
    parser.add_argument('brain_regions_file', type=str,
                        help="Path to the AllBrainRegions.csv file")
    parser.add_argument('all_points_file', type=str,
                        help="Path to the all_points.csv file")
    parser.add_argument('output_file', type=str,
                        help="Path to the output CSV file")

    args = parser.parse_args()
    main(args.brain_regions_file, args.all_points_file, args.output_file)
