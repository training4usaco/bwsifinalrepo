import numpy as np
from qiskit import QuantumCircuit

def test_circuit(num_qubits):

    qc = QuantumCircuit(num_qubits)

    for qubit in range(num_qubits):
        qc.h(qubit)

    qc.measure_all()
    return qc



def customCost(predictions, labels, data):
    
    distance_from_home = data[:, 0]
    distance_from_last_transaction = data[:, 1]
    ratio_to_median_purchase_price = data[:, 2]
    repeat_retailer = data[:, 3]
    used_chip = data[:, 4]
    used_pin_number = data[:, 5]
    online_order = data[:, 6]

    log_loss_1 = np.log(np.abs(np.subtract(labels, predictions[:,0]))/2)
    log_loss_2 = np.log(np.abs(np.subtract(labels, predictions[:,1]))/2)

    linear_repeat_retailer =  np.abs(np.subtract(labels, predictions[:,2]))/2
    linear_used_chip = np.abs(np.subtract(labels, predictions[:,3]))/2
    linear_used_pin_number = np.abs(np.subtract(labels, predictions[:,4]))/2
    linear_online_order = np.abs(np.subtract(labels, predictions[:,5]))/2

    cost = np.sum(log_loss_1, log_loss_2, 
                  linear_repeat_retailer, linear_used_chip, linear_used_pin_number, 
                  linear_online_order)
    
    return cost

def compute_gradient(prediction, label, b, is_log):
    if is_log:
        if label == 0:
            return 1 / np.log(b)
        elif label == 1:
            return -1 / np.log(b)
    else:
        if label == 0:
            return 1 / 2
        elif label == 1:
            return -1 / 2
        
def update_parameters(params, gradients, learning_rate):
    return params - learning_rate * gradients



def optimize_vqc(params, data, labels, learning_rate, b, num_iterations):
    
    for iteration in range(num_iterations):
        #this is where we call the function to apply the gates and get back the measurement?
        #predictions = quantum_circuit(params, data)
        gradients = np.zeros_like(params)

        # Compute gradients
        for i in range(len(data)):
            for j in range(predictions.shape[1]):
                is_log = j < 2  
                gradient = compute_gradient(predictions[i, j], labels[i], b, is_log)
                gradients[j] += gradient

        cost = customCost(predictions, labels, data)
        params = update_parameters(params, gradients, learning_rate)
    
    return params