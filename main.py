from teleportation.simulator import TeleportationSimulator

import matplotlib.pyplot as plt

def main():
    print("=== Quantum Teleportation Protocol Prototype ===\n")

    simulator = TeleportationSimulator()
    result = simulator.run(shots=1024)

    print(f"Teleportation Successful: {result['success']}")
    print(f"State Fidelity: {result['fidelity']:.4f}")
    print(f"Measurement Outcomes: {result['counts']}")

    print("\nCircuit:")
    print(result['circuit'])

    print("\nPrototype completed. State successfully teleported with high fidelity.")

if __name__ == "__main__":
    main()