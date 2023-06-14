import numpy as np
import matplotlib.pyplot as plt

class QuantumArtGenerator:
    def __init__(self, canvas_size):
        self.canvas_size = canvas_size
        self.canvas = np.zeros((canvas_size, canvas_size))

    def generate_art(self):
        print("Generating quantum art...")
        for i in range(self.canvas_size):
            for j in range(self.canvas_size):
                intensity = np.random.uniform(0.0, 1.0)
                self.canvas[i, j] = intensity
        print("Quantum art generated.")

    def display_art(self):
        plt.imshow(self.canvas, cmap='gray')
        plt.axis('off')
        plt.show()

def main():
    art_generator = QuantumArtGenerator(200)

    # Generate quantum art
    art_generator.generate_art()

    # Display the generated art
    art_generator.display_art()

if __name__ == "__main__":
    main()
