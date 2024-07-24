
from qiskit import QuantumCircuit
from qiskit_aer import Aer
import math
import numpy as np


def encodeQubit(circuit: QuantumCircuit, qubit: int, val:float, max_val:float) -> None:
    #Rotate qubit proportional amount to ratio of val to max_val
    theta = val/max_val * math.pi

    circuit.ry(theta, qubit)

def decodeQubit(qc: QuantumCircuit, qubit: int, max_val) -> float:

    #outer product
    backend = Aer.get_backend('statevector_simulator')
    result = backend.run(qc).result()

    statevector = result.get_statevector()
    
    #shorthand
    n = qc.num_qubits



    #storing amplitudes
    alpha = np.array([])
    beta = np.array([])
    
    
    #binary stuff
    #uses binary pattern, separates amplitudes if qubit is |0> or |1>
    for i in range(2**n):
        if (i//2**qubit)%2 == 1:
            beta = np.append(beta, statevector[i])
        else:
            alpha = np.append(alpha, statevector[i])

    #compute probability of getting |0> or |1> 
    alpha = np.sqrt(np.sum(np.abs(alpha)**2))
    beta = np.sqrt(np.sum(np.abs(beta)**2))

    #since only rotating on real axis, only need real components
    x = alpha.real
    y = beta.real


    #triangle math that find angle
    d2 = math.dist([x,y], [1,0])
    d1 = math.dist([x,y], [0,0])

    res = (d2**2 - d1**2 - 1)/-2/d1

    ang = math.acos(res)
    return ang*max_val*2/math.pi