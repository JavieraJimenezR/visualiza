from pathlib import Path
import pandas as pd

def load_parquet_files(directory: Path | str) -> pd.DataFrame:
    directory_path = Path(directory)
    parquet_files = list(directory_path.glob("*.parquet"))
    
    df_list = [pd.read_parquet(file) for file in parquet_files]
    combined_df = pd.concat(df_list, ignore_index=True)
    
    return combined_df