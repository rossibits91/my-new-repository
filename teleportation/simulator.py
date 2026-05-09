from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit.quantum_info import state_fidelity, Statevector
from .circuit import QuantumTeleportation

class TeleportationSimulator:
    def __init__(self):
        self.backend = AerSimulator()
        self.tp = QuantumTeleportation()

    def run(self, shots: int = 1000):
        """Run the teleportation protocol and return results"""
        qc, original_state = self.tp.build_teleportation_circuit()

        # Transpile and run
        tqc = transpile(qc, self.backend)
        result = self.backend.run(tqc, shots=shots).result()
        counts = result.get_counts()

        # Get final statevector
        statevector = result.get_statevector()

        # Bob's qubit is the third qubit (index 2, basis states 4-7 in 3-qubit space)
        final_bob = Statevector(statevector)[4:8]
        fidelity = state_fidelity(original_state, final_bob)

        return {
            'circuit': qc,
            'counts': counts,
            'original_state': original_state,
            'final_statevector': statevector,
            'fidelity': fidelity,
            'success': fidelity > 0.95
        }