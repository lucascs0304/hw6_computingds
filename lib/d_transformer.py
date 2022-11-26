
from abc import ABC, abstractmethod
import numpy as np
import pandas as pd

class transformer(ABC):

    def __init__(self, df, col:list) -> None:
        self.df = df
        self.col = col

    @abstractmethod
    def apply_transform(self):
        return NotImplementedError

class log(transformer):

    def apply_transform(self):
        '''
        Apply logarithms to some of the columns in the dataset.
        
        Parameters:
            df: dataframe to be treated
            col: feature to be transformed

        Returns:
            Transformed dataframe
        '''
        self.df.loc[:,self.col] = self.df.loc[:,self.col].apply(lambda x: np.log10(x))
        return self.df
    
class levels(transformer):

    def apply_transform(self):
        '''
        Apply a transformation to return to original logged values.
        
        Parameters:
            df: dataframe to be treated
            col: feature to be transformed

        Returns:
            Transformed dataframe
        '''
        self.df.loc[:,self.col] = self.df.loc[:,self.col].apply(lambda x: np.exp(x))
        return self.df
