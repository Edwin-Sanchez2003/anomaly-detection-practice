"""
    Edwin Sanchez
    
    Dataset Loader
    
    This module has functions to load the dataset.
"""

import os
from tqdm import tqdm
import pandas as pd
import numpy as np

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
def load_dataset( dataset_dir : str, num_high_traffic_ports : int = 5 ):
    # load dataset into pandas dataframes
    file_paths, dfs = load_dataset_pd ( dataset_dir = dataset_dir )
    
    # for each df, load
    
    for df in dfs:
        pass
        
    # return selected ports, train, test datasets...
        
    

if __name__ == "__main__":
    main()
