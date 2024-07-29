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