
import pandas
import numpy

class nan_filler:
    
        def __init__(self, df, col):
            self.df = df
            self.col = col
            self.fill_means(self.col)
        
        def fill_means(self, col):
            
            '''
            Fill NaN with the mean value of the column in the given columns.
            
            Parameters: 
                df (dataframe): dataframe to fill NaNs for
                col (list): target columns to fill NaNs for
                
            Returns:
                df: dataframe with filled NaN in target columns
            '''
            
            self.df.loc[:,col].fillna(self.df.mean().iloc[0], inplace=True)
