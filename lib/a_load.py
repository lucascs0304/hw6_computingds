import pandas as pd
from sklearn.model_selection import train_test_split

class loader():
    
    def __init__(self, file):
        self.file = file
        self.load()
        self.split()
        
    def load(self):
        
        '''
        Read database.
        
        Parameters: 
            path: path to data
            
        Returns:
            df: database in pandas format
        '''
        
        self.df = pd.read_csv(self.file, index_col=0)
      

    def split(self):

        
        '''
        Split data between train and test using sklearn.model_selection.train_test_split.
        
        Parameters: 
            df: dataframe to split data for
            
        Returns:
            X_train: splitted X axis for training models
            y_train: splitted y axis for training models
            X_test: splitted X axis for testing models
            y_test: splitted y axis for testing models
            
        '''
        
        seed = 2
        self.train, self.test = train_test_split(self.df, test_size=0.3, random_state=seed)

        return self.train, self.test