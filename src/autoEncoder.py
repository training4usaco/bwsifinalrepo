import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from ansatz import Ansatz

def AutoEncoder(data, num_categories, theta_list) -> QuantumCircuit:
    num_latent = data.num_qubits - num_categories
    num_trash = num_categories
    latent_register = QuantumRegister(num_latent)
    trash_register = QuantumRegister(num_trash)
    reference_register = QuantumRegister(num_trash)
    auxiliary_register = QuantumRegister(1)
    classical_register = ClassicalRegister(num_trash)

    qc = QuantumCircuit(latent_register, trash_register, reference_register, auxiliary_register, classical_register)

    encoder_circuit = QuantumCircuit(latent_register, trash_register, reference_register, auxiliary_register, classical_register)
    encoder_circuit.compose(Ansatz(num_latent, num_trash, theta_list), range(num_latent + num_trash), inplace=True)

    swap_circuit = QuantumCircuit(latent_register, trash_register, reference_register, auxiliary_register, classical_register)

    swap_circuit.h(auxiliary_register)
    for i in range(num_trash):
        swap_circuit.cswap(auxiliary_register, num_latent + i, num_latent + num_trash + i)

    qc.compose(encoder_circuit, inplace=True)
    qc.compose(swap_circuit, inplace=True)
    qc.compose(encoder_circuit.inverse(), inplace=True)

    # measure everything and put in classical register?? 
    qc.measure(latent_register, classical_register[:num_latent]) # latent qubits 
    qc.measure(trash_register, classical_register[num_latent:num_latent + num_trash]) # trash qubits
    qc.measure(reference_register, classical_register[num_latent + num_trash:num_latent + 2 * num_trash]) # reference qubits
    qc.measure(auxiliary_register, classical_register[num_latent + 2 * num_trash:num_latent + 2 * num_trash + 1]) # auxiliary qubits 

