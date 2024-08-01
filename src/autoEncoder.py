import numpy as np
import math
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from ansatz import Ansatz
from qiskit_aer import AerSimulator, Aer
from qiskit.compiler import assemble
from qiskit.circuit.library import RealAmplitudes

def AutoEncoder(data, fraud, num_categories, theta_list) -> tuple:
    num_trash = 3
    num_latent = data.num_qubits - num_trash

    print(str(num_latent) + " " + str(num_trash))

    latent_register = QuantumRegister(num_latent)
    trash_register = QuantumRegister(num_trash)
    reference_register = QuantumRegister(num_trash)
    auxiliary_register = QuantumRegister(1)
    classical_register = ClassicalRegister(1)

    qc = QuantumCircuit(latent_register, trash_register, reference_register, auxiliary_register, classical_register)

    encoder_circuit = QuantumCircuit(latent_register, trash_register)
    # encoder_circuit.compose(RealAmplitudes(num_latent + num_trash, reps=1), range(num_latent + num_trash), inplace=True)
    encoder_circuit.compose(Ansatz(num_latent, num_trash, theta_list), range(num_latent + num_trash), inplace=True)

    swap_circuit = QuantumCircuit(latent_register, trash_register, reference_register, auxiliary_register, classical_register)

    swap_circuit.h(auxiliary_register)
    for i in range(num_trash):
        swap_circuit.cswap(auxiliary_register, num_latent + i, num_latent + num_trash + i)
    swap_circuit.h(auxiliary_register)

    qc.compose(data, range(num_latent + num_trash), inplace=True)
    qc.barrier()
    qc.compose(encoder_circuit, inplace=True)
    qc.barrier()
    qc.compose(swap_circuit, inplace=True)
    qc.barrier()
    # qc.measure(auxiliary_register, classical_register)
    qc.save_density_matrix(qubits=[num_latent + num_trash * 2]) # <== here
    qc.measure_all()
    # print(qc.draw())

    simulator = AerSimulator()
    circ = transpile(qc, backend=simulator)
    job = simulator.run(circ)
    state = job.result().data()['density_matrix']
    # sv = state.to_statevector()

    print(float(state[0][0]))

    return(float(state[0][0]), fraud)

    # print(state[0][0])

    # simulator = AerSimulator()
    # compiled_circuit = transpile(qc, simulator)
    # sim_result = simulator.run(compiled_circuit).result()
    # counts = sim_result.get_counts()

    # if('0' not in counts):
    #     counts['0'] = 0

    # print(counts)

    # return (1.0 - counts['0'] / 1024.0, fraud)   # tuple of (probability of 1, fraud)


