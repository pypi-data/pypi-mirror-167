
__module_name__ = "_WebMatrix.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# import packages -------------------------------------------------------------
import scipy
import os


# import local dependencies ---------------------------------------------------
from ._WebFile import WebFile

# supporting functions: -------------------------------------------------------
def _convert_mtx_filepath(mtx_path, user_ext=None):
    if mtx_path.endswith("mtx.gz"):
        return mtx_path.replace("mtx.gz", "npz")
    elif mtx_path.endswith("mtx"):
        return mtx_path.replace("mtx.gz", "npz")
    else:
        if user_ext:
            return mtx_path.replace(user_ext, "npz")
        else:
            print("Supply user_ext")
            

# main module class: ----------------------------------------------------------
class WebMatrix(WebFile):
    def __init__(self, http_address, local_path=None, user_ext=None):
        super().__init__(http_address, local_path)

        self.npz_path = _convert_mtx_filepath(self.local_path, user_ext=None)    
    
    def to_npz(self):
        self.mat = scipy.io.mmread(self.local_path)
        scipy.sparse.save_npz(self.npz_path, self.mat)
        return self.mat
    
    def read(self):
        
        if os.path.exists(self.npz_path):
            return scipy.sparse.load_npz(self.npz_path)
        
        elif os.path.exists(self.local_path):
            return self.to_npz()
        else:
            self.download()
            return self.to_npz()