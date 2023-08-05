
__module_name__ = "_WebFrame.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# import packages -------------------------------------------------------------
import pandas as pd


# import local dependencies ---------------------------------------------------
from ._WebFile import WebFile


# main module class: ----------------------------------------------------------
class WebFrame(WebFile):
    """A subclass of WebFile made for file types readable as pandas dataframes."""
    
    def __init__(self, http_address, local_path=None):
        super().__init__(http_address, local_path)
    
    def read(self, read_func=pd.read_csv, **kwargs):
        self.download()
        return read_func(self.local_path, **kwargs)