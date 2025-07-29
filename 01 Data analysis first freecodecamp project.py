import numpy as np
import sys
def calculate (l):
    if(len (l) != 9):
        raise ValueError("List must contain nine numbers")
    else :  
        A = np.array(l).reshape(3,3)
        mean_r = np.mean(A,axis = 0).tolist()
        mean_c = np.mean(A,axis = 1).tolist()
        mean_t = np.mean(A).tolist()
            
        var_r = np.var(A,axis = 0).tolist()
        var_c = np.var(A,axis = 1).tolist()
        var_t = np.var(A).tolist()
            
            
        std_r = np.std(A,axis = 0).tolist()
        std_c = np.std(A,axis = 1).tolist()
        std_t = np.std(A).tolist()
            
            
        max_r = np.max(A,axis = 0).tolist()
        max_c = np.max(A,axis  = 1).tolist()
        max_t = np.max(A).tolist()
            
        min_r = np.min(A,axis = 0).tolist()
        min_c = np.min(A,axis  = 1).tolist()
        min_t = np.min(A).tolist()
            
        sum_r = np.sum(A,axis = 0).tolist()
        sum_c = np.sum(A,axis = 1).tolist()
        sum_t = np.sum(A).tolist()
            
        
        return {
  'mean': [mean_r, mean_c, mean_t],
  'variance': [var_r, var_c, var_t],
  'standard deviation': [std_r, std_c, std_t],
  'max': [max_r, max_c, max_t],
  'min': [min_r, min_c, max_t],
  'sum': [sum_r, sum_c, sum_t]
}