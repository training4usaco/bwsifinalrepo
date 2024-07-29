from qiskit import QuantumCircuit
from qiskit import ClassicalRegister, QuantumRegister
from qiskit_aer import Aer
import math
import numpy as np

'''
Functionality of autoencoder from paper:
- data compression: reduces input to less qubits (only latent qubits left after)
- unitary, but no decoder needed?
- "parameterized quantum circuit" 
- minimize reconstruction error
- need classical register + auxiliary qubit + reference space
'''

# nt = number of trash qubits
# n = total number of qubits
# i think it goes like (ry gates on all qubits -> cz gates on some pairs) 
# -> ry gates on trash qubits 
def ansatz(nt, n): 
    qc = QuantumCircuit(n)
    
    

    theta = #idk

    # ry gates on all qubits
    for i in range(n):
        qc.ry(i)



    




# function should be applied after classical data is converted to quantum qubits 
def autoEncode(trash, latent):
    reg = QuantumRegister()

