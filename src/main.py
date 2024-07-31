import encodeData as ED
from ansatz import Ansatz
import autoEncoder as AE
import costfunc as CF

from autoEncoder import AutoEncoder


import numpy as np

CATEGORIES = 7

def main():
    (normal_data, fraud_data)  = ED.EncodeData(CATEGORIES, "../data/test_data.csv")
    theta_list = [np.random(0, np.pi)] * CATEGORIES
    Ansatz()
       # NOTE: temporary
    # AutoEncoder(normal_data, CATEGORIES, theta_list)

if __name__ == "__main__":
    main()

