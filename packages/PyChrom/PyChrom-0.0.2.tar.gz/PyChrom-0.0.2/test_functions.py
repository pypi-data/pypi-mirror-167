import pychrom as chrom
import numpy as np

test = np.asarray([1, 1, 2, 4, 5, 4, 2, 1, 1])
chrom.baseline_arPLS(test)
chrom.normalize(test)
chrom.peak_search(test)