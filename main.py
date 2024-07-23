from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble
from qiskit.visualization import plot_histogram
from collections import Counter

qc = QuantumCircuit()