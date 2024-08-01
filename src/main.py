import encodeData as ED
from ansatz import Ansatz
import autoEncoder as AE
import costfunc as CF

from autoEncoder import AutoEncoder
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator, Aer
import numpy as np

CATEGORIES = 7

def main():
    path = "../data/test_data.csv"
    (normal_data, fraud_data)  = ED.EncodeData(CATEGORIES, path)
    theta_list = (np.random.rand(normal_data.num_qubits) * np.pi).tolist()
    # print(theta_list)
    (intial_probability, fraud) = AutoEncoder(normal_data, 0, CATEGORIES, theta_list)
    # Ansatz()

if __name__ == "__main__":
    main()

