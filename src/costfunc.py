import numpy as np
from qiskit import QuantumCircuit

def test_circuit(num_qubits):

    qc = QuantumCircuit(num_qubits)

    for qubit in range(num_qubits):
        qc.h(qubit)

    qc.measure_all()
    return qc



def cost(p0, p1):

    cost = 1-p0 + p1         
    return cost**2    
    
    
# def compute_gradient(prediction, label, b, is_log):
#     if is_log:
#         if label == 0:
#             return 1 / np.log(b)
#         elif label == 1:
#             return -1 / np.log(b)
#     else:
#         if label == 0:
#             return 1 / 2
#         elif label == 1:
#             return -1 / 2
        
# def update_parameters(params, gradients, learning_rate):
#     return params - learning_rate * gradients



# def optimize_vqc(params, data, labels, learning_rate, b, num_iterations):
    
#     for iteration in range(num_iterations):
#         #this is where we call the function to apply the gates and get back the measurement?
#         #predictions = quantum_circuit(params, data)
#         gradients = np.zeros_like(params)

#         # Compute gradients
#         for i in range(len(data)):
#             for j in range(predictions.shape[1]):
#                 is_log = j < 2  
#                 gradient = compute_gradient(predictions[i, j], labels[i], b, is_log)
#                 gradients[j] += gradient

#         cost = customCost(predictions, labels, data)
#         params = update_parameters(params, gradients, learning_rate)
    
#     return params