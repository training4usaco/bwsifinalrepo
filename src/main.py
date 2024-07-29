import encodeData
from autoEncoder import AutoEncoder

CATEGORIES = 7

def main():
    data = encodeData.EncodeData(CATEGORIES, "../data/test_data.csv")
    theta_list = [0] * data.num_qubits    # NOTE: temporary
    AutoEncoder(data, CATEGORIES, theta_list)

if __name__ == "__main__":
    main()

