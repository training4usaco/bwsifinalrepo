from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import QFT
from qiskit.circuit import ControlledGate
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator, Aer
import math
import encoding as enc



testCirc = QuantumCircuit(3)
enc.encodeQubit(testCirc, 0, 2343, 7000)

print(enc.decodeQubit(testCirc, 0, 7000))
