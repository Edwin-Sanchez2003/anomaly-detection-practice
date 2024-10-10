"""
    Edwin Sanchez
    
    Dataset Loader
    
    This module has functions to load the dataset.
"""

import os
from tqdm import tqdm
import pandas as pd
import numpy as np

import torch
from sklearn.preprocessing import LabelEncoder

def main() -> None:
    # test that the data is loaded correctly
    load_dataset ( dataset_dir = "./CIC-IDS2017/" )


# loads the dataset as a pandas dataframe with file names
def load_dataset_pd ( dataset_dir : str ) -> tuple [ list [ str ], list [ pd.DataFrame ] ]:
    # validate that the directory exists
    if os.path.isdir ( dataset_dir ) == False:
        raise FileNotFoundError(
            f"The directory given '{ dataset_dir }' does not exist - have you downloaded & unzipped the dataset into `./CIC-IDS2017` yet?")
    
    # load all csv files found in the folder into a list of dataframes
    file_paths : list [ str ] = []
    dfs : list [ pd.DataFrame ] = []
    
    print ( f"Loading CSV file data from the directory '{dataset_dir}'." )
    for file_name in tqdm( os.listdir ( dataset_dir ) ):
        # validate it's a csv file
        root, ext = os.path.splitext ( os.path.basename ( file_name ) )
        if ext != ".csv":
            raise print ( f"Skipping: { file_path } | Only CSV files allowed..." )
        
        # get the full file path
        file_path : str = os.path.join ( dataset_dir, file_name )
        file_paths.append ( file_path )
        
        # load csv file into a dataframe
        df : pd.DataFrame = pd.read_csv ( file_path )
        dfs.append ( df )

    # after collecting file paths and dataframes, return them in a tuple
    return ( file_paths, dfs )


# loads the dataset for model training
def load_dataset ( 
    dataset_dir : str, 
    num_high_traffic_ports : int = 5 
) -> tuple [ list [ torch.Tensor ], 
             list [ torch.Tensor ], 
             list [ torch.Tensor ], 
             list [ torch.Tensor ] ]:
    # load dataset into pandas dataframes
    file_paths, dfs = load_dataset_pd ( dataset_dir = dataset_dir )
    
    # Initialize the LabelEncoder
    label_encoder = LabelEncoder()
    
    true_label_set : list [ torch.Tensor ] = []
    label_set : list [ torch.Tensor ] = []
    true_feature_set : list [ torch.Tensor ] = []
    feature_set : list [ torch.Tensor ] = []
    for df in tqdm(dfs):
        # slice off labels & add to list of labels for each csv.
        labels : pd.DataFrame = df[ ' Label'].copy(deep=True)
        labels[' Label_Numeric'] = label_encoder.fit_transform(df[' Label'])
        numeric_labels = torch.tensor(labels[' Label_Numeric'], dtype=torch.float16)
        true_label_set.append(numeric_labels)
        
        # slice off the ports - we're using them to do stuff...
        top_ports : pd.Series = df[' Destination Port'].value_counts()[0:num_high_traffic_ports]
        top_ports[' Destination Port_Numeric'] = label_encoder.fit_transform(top_ports)
        numeric_labels = torch.tensor(top_ports[' Destination Port_Numeric'], dtype=torch.float16)
        label_set.append(numeric_labels)
        
        # remove the label column from the remaining features
        df.drop(columns=[' Label'], inplace=True)
        
        # only use training samples from the ports we selected
        df_filtered = df[df[' Destination Port'].isin(top_ports)]
        print(df_filtered)
        features = torch.tensor(df_filtered.to_numpy(), dtype=torch.float16)
        feature_set.append(features)
        
        # do the same with the remaining features
        features = torch.tensor(df.to_numpy(), dtype=torch.float16)
        true_feature_set.append(features)
        
    return (true_label_set, label_set, true_feature_set, feature_set)


if __name__ == "__main__":
    main()
