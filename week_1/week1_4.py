from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import random

simulator = AerSimulator()

def quantum_random_bit():
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    compiled = transpile(qc, simulator)
    job = simulator.run(compiled, shots=1)
    result = job.result()
    counts = result.get_counts()

    return int(list(counts.keys())[0])

quantum_bits = []

for _ in range(100):
    quantum_bits.append(quantum_random_bit())

print("Quantum Bits:")
print(quantum_bits)

python_bits = []

for _ in range(100):
    python_bits.append(random.randint(0, 1))

print("Python Bits:")
print(python_bits)

print("\nQuantum")
print("Zeros:", quantum_bits.count(0))
print("Ones :", quantum_bits.count(1))

print("\nPython")
print("Zeros:", python_bits.count(0))
print("Ones :", python_bits.count(1))

