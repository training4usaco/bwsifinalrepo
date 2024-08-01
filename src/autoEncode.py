# from qiskit import QuantumCircuit
# from qiskit import ClassicalRegister, QuantumRegister, Parameter
# from qiskit_aer import Aer
# import math
# import numpy as np

# '''
# Functionality of autoencoder from paper:
# - data compression: reduces input to less qubits (only latent qubits left after)
# - unitary, but no decoder needed?
# - "parameterized quantum circuit" 
# - minimize reconstruction error
# - need classical register + auxiliary qubit + reference space
# '''

# # n = total number of qubits
# # nt = number of trash qubits
# # accordign to diagram in paper:
# # i think it goes like (ry gates on all qubits -> cz gates on some pairs) x nt 
# # -> ry gates on trash qubits at the end 

# def ansatz(n, nt): 
#     qc = QuantumCircuit(n)
#     theta = [Parameter(f'θ{i}') for i in range(n)]

#     for i in range(nt):          
#         # ry gates on all qubits
#         for i in range(n):
#             qc.ry(theta[i], i)
    

#     # cz gates on trash and latent qubits
    


#     # ry gates on trash qubits
#     for i in range(nt):
#         qc.ry(theta[i], i)
    
    

# # function should be applied after classical data is converted to quantum qubits 
# def autoEncode(trash, latent):
#     reg = QuantumRegister()

