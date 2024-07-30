import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.quantum_info import Statevector
from ansatz import Ansatz

def AutoEncoder(data, num_categories, theta_list) -> float:
    num_latent = data.num_qubits - num_categories
    num_trash = num_categories
    latent_register = QuantumRegister(num_latent)
    trash_register = QuantumRegister(num_trash)

    # NOTE: Swap stuff not needed for this
    # reference_register = QuantumRegister(num_trash)
    # auxiliary_register = QuantumRegister(1)
    # classical_register = ClassicalRegister(num_trash)

    qc = QuantumCircuit(latent_register, trash_register)

    encoder_circuit = QuantumCircuit(latent_register, trash_register)
    encoder_circuit.compose(Ansatz(num_latent, num_trash, theta_list), range(num_latent + num_trash), inplace=True)

    swap_circuit = QuantumCircuit(latent_register, trash_register)

    # swap_circuit.h(auxiliary_register)
    # for i in range(num_trash):
    #     swap_circuit.cswap(auxiliary_register, num_latent + i, num_latent + num_trash + i)


    qc.compose(encoder_circuit, inplace=True)
    qc.barrier()
    # qc.compose(swap_circuit, inplace=True)
    qc.barrier()

    for i in range(num_latent, num_latent + num_trash):
        qc.reset(i)

    qc.barrier()

    qc.compose(encoder_circuit.inverse(), inplace=True)

    input_data = Statevector(data).data
    output_state = Statevector(qc).data

    fidelity = np.sqrt(np.dot(input_data.conj(), output_state) ** 2)

    return 1.0 - fidelity

