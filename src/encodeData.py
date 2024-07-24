import csv
import sys
from math import ceil, log2
from pathlib import Path
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile

def EncodeDataUtility(data_set) -> QuantumCircuit:
    # TODO: encode each dataset with entanglement
    pass

def EncodeData(relative_path = "../data/card_transdata.csv"):
    # reads in the data

    distance_from_home = []
    distance_from_last_purchace = []
    ratio_to_median = []
    repeat_retailer = []
    used_chip = []
    used_pin_number = []
    online_order = []
    fraud = []

    absolute_path = Path(__file__).parent / relative_path
    with open(absolute_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:  # pls help idk how to pythong
            distance_from_home.append(row[0])
            distance_from_last_purchace.append(row[1])
            ratio_to_median.append(row[2])
            repeat_retailer.append(row[3])
            used_chip.append(row[4])
            used_pin_number.append(row[5])
            online_order.append(row[6])
            fraud.append(row[7])
    


    