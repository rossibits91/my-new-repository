from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.quantum_info import random_statevector, Statevector

class QuantumTeleportation:
    """Simple Quantum Teleportation Protocol Implementation"""

    def create_bell_pair(self) -> QuantumCircuit:
        """Create a maximally entangled Bell pair"""
        qr = QuantumRegister(2, 'bell')
        qc = QuantumCircuit(qr)
        qc.h(0)
        qc.cx(0, 1)
        return qc

    def build_teleportation_circuit(self):
        """Build the complete teleportation circuit"""
        # Qubits: 0 = state to teleport, 1 = Alice's entangled qubit, 2 = Bob's qubit
        qr = QuantumRegister(3, 'q')
        cr_z = ClassicalRegister(1, 'cz')  # Measurement for Z correction
        cr_x = ClassicalRegister(1, 'cx')  # Measurement for X correction
        qc = QuantumCircuit(qr, cr_z, cr_x)

        # Step 1: Prepare random state to teleport on qubit 0
        original_state = random_statevector(2)
        qc.initialize(original_state, 0)

        # Step 2: Create entangled pair between Alice (1) and Bob (2)
        qc.h(1)
        qc.cx(1, 2)

        qc.barrier()

        # Step 3: Alice performs Bell measurement on qubits 0 and 1
        qc.cx(0, 1)
        qc.h(0)
        qc.measure(0, cr_z[0])
        qc.measure(1, cr_x[0])

        qc.barrier()

        # Step 4: Bob applies corrections based on classical bits
        qc.x(2).c_if(cr_x, 1)   # Apply X if needed
        qc.z(2).c_if(cr_z, 1)   # Apply Z if needed

        return qc, original_state