import numpy as np

def calculate(list):
    if len(list) !=9: # Checking for right size.
        raise ValueError("List must contain nine numbers.")

    array = np.asarray(list) # Converting list to numpy array.

    mat = np.reshape(array, (3,3)) # Reshaping array to (3,3).

    # Calculating values an converting results in lists.
    meanax1 = np.mean(mat, axis=0).tolist()
    meanax2 = np.mean(mat, axis=1).tolist()
    meanfl = np.mean(mat).tolist()

    varax1 = np.var(mat, axis=0).tolist()
    varax2 = np.var(mat, axis=1).tolist()
    varfl = np.var(mat).tolist()
    
    stdax1 = np.std(mat, axis=0).tolist()
    stdax2 = np.std(mat, axis=1).tolist()
    stdfl = np.std(mat).tolist()
    
    maxax1 = np.max(mat, axis=0).tolist()
    maxax2 = np.max(mat, axis=1).tolist()
    maxfl = np.max(mat).tolist()
    
    minax1 = np.min(mat, axis=0).tolist()
    minax2 = np.min(mat, axis=1).tolist()
    minfl = np.min(mat).tolist()
    
    sumax1 = np.sum(mat, axis=0).tolist()
    sumax2 = np.sum(mat, axis=1).tolist()
    sumfl = np.sum(mat).tolist()

    calculations = {
      'mean': [meanax1, meanax2, meanfl],
      'variance': [varax1, varax2, varfl],
      'standard deviation': [stdax1, stdax2, stdfl],
      'max': [maxax1, maxax2, maxfl],
      'min': [minax1, minax2, minfl],
      'sum': [sumax1, sumax2, sumfl]
    }
    
    return calculations