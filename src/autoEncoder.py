import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from ansatz import Ansatz
from qiskit_aer import AerSimulator
from qiskit.compiler import assemble

def AutoEncoder(data, fraud, num_categories, theta_list) -> tuple:
    num_latent = data.num_qubits - num_categories
    num_trash = num_categories

    print(str(num_latent) + " " + str(num_trash))

    latent_register = QuantumRegister(num_latent)
    trash_register = QuantumRegister(num_trash)
    reference_register = QuantumRegister(num_trash)
    auxiliary_register = QuantumRegister(1)
    classical_register = ClassicalRegister(1)

    qc = QuantumCircuit(latent_register, trash_register, reference_register, auxiliary_register, classical_register)

    encoder_circuit = QuantumCircuit(latent_register, trash_register)
    encoder_circuit.compose(Ansatz(num_latent, num_trash, theta_list), range(num_latent + num_trash), inplace=True)

    swap_circuit = QuantumCircuit(latent_register, trash_register, reference_register, auxiliary_register, classical_register)

    swap_circuit.h(auxiliary_register)
    for i in range(num_trash):
        swap_circuit.cswap(auxiliary_register, num_latent + i, num_latent + num_trash + i)
    swap_circuit.h(auxiliary_register)

    qc.compose(encoder_circuit, inplace=True)
    qc.barrier()
    qc.compose(swap_circuit, inplace=True)
    qc.barrier()
    qc.measure(auxiliary_register, classical_register)

    # print(qc.draw())

    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    sim_result = simulator.run(compiled_circuit).result()
    counts = sim_result.get_counts()

    if('0' not in counts):
        counts['0'] = 0

    print(counts)

    return (1.0 - counts['0'] / 1024.0, fraud)   # tuple of (probability of 1, fraud)


