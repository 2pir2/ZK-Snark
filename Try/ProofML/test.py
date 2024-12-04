import json

def relu(x):
    """ReLU activation function."""
    return max(0, x)

def simulate_neural_network(weights, biases, input_vector):
    """Simulates the forward pass of a neural network."""
    current_output = input_vector
    for layer_index, (layer_weights, layer_biases) in enumerate(zip(weights, biases)):
        next_output = []
        for neuron_weights, neuron_bias in zip(layer_weights, layer_biases):
            # Weighted sum
            weighted_sum = sum(w * x for w, x in zip(neuron_weights, current_output)) + neuron_bias
            # Apply ReLU activation
            next_output.append(relu(weighted_sum))
        current_output = next_output  # Move to the next layer
        print(f"Outputs of layer {layer_index + 1}: {current_output}")  # Debug: Outputs of each layer
    return current_output

# Load the weights.json file
with open("weights.json", "r") as file:
    data = json.load(file)

weights = data["weights"]
biases = data["biases"]

# Generate a random input vector matching the first layer's input size
input_size = len(weights[0][0])  # Input size is the number of weights for the first neuron in the first layer
input_vector = [0.5] * input_size  # Example: Using a fixed value for each input

# Simulate the network and print final layer outputs
final_outputs = simulate_neural_network(weights, biases, input_vector)

print("\nFinal outputs (last layer):")
for neuron_index, output in enumerate(final_outputs):
    print(f"Neuron {neuron_index}: {output}")
