from qiskit import QuantumCircuit, Aer, transpile


def run(**kwargs):
    circ = QuantumCircuit(2)
    circ.h(0)
    circ.cx(0, 1)
    circ.measure_all()

    # Transpile for simulator
    simulator = Aer.get_backend('aer_simulator')
    circ = transpile(circ, simulator)

    # Run and get counts
    result = simulator.run(circ).result()
    counts = result.get_counts(circ)

    return counts
