import encodeData
import numpy as np
from autoEncoder import AutoEncoder

CATEGORIES = 7

def VQC():
    # path = "../data/test_data.csv"
    (normal_data, fraud_data)  = encodeData.EncodeData(CATEGORIES)
    theta_list = [np.pi / 2] * normal_data.num_qubits    # NOTE: temporary
    (intial_probability, fraud) = AutoEncoder(normal_data, 0, CATEGORIES, theta_list)

VQC()


