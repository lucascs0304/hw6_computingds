
import pandas

class nan_dropper():
    
    def __init__(self, df, col):
        self.df = df
        self.col = col
        self.drop_nan(self.col)
        
    def drop_nan(self, col):
        
        '''
        Remove those rows that contain NaN values in the given columns.
        
        Parameters: 
            df (dataframe): dataframe to remove rows for
            col (list): target columns to remove rows for
            
        Returns:
                cleaned_df: dataframe with removed rows in target columns
        '''
        
        self.cleaned_df = self.df.dropna(axis=0, subset=col, how='any')
