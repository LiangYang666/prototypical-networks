#%%
import pandas as pd
import os


ROOT_PATH = '../../data/Mini-imagenet'
#%%
if __name__ == "__main__":
    #%%
    train_data = pd.read_csv(os.path.join(ROOT_PATH, 'train.csv'))
    test_data = pd.read_csv(os.path.join(ROOT_PATH, 'test.csv'))
    val_data = pd.read_csv(os.path.join(ROOT_PATH, 'val.csv'))
    all_data = pd.concat([train_data, test_data, val_data])

