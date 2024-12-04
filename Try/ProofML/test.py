import numpy as np
import json

weights_path = '/Users/hanxu/Desktop/ZK-Snark/Try/ProofML/weights.json'
inputs_path = '/Users/hanxu/Desktop/ZK-Snark/Try/ProofML/inputs.json'
outputs_path = '/Users/hanxu/Desktop/ZK-Snark/Try/ProofML/outputs.json'

# Load weights, biases, and inputs from JSON files
with open(weights_path, 'r') as f:
    weights_data = json.load(f)
with open(inputs_path, 'r') as f:
    inputs_data = json.load(f)
with open(outputs_path, 'r') as f:
    expected_outputs = json.load(f)

# Helper function to apply ReLU to a list of numbers
def relu(x):
    return np.maximum(0, x)

# Function to round and scale down
def round_and_scale_down(value):
    rounded_value = round(value * 1e3) / 1e3
    return rounded_value

# Forward pass through the neural network
def neural_network_output(weights, biases, input_data):
    # Initial layer output is the input data
    layer_output = input_data

    # Iterate over each layer's weights and biases
    for layer_idx, (layer_weights, layer_biases) in enumerate(zip(weights, biases)):
        next_layer_output = []
        for neuron_idx, (neuron_weights, bias) in enumerate(zip(layer_weights, layer_biases)):
            # Weighted sum with bias
            weighted_sum = sum(w * i for w, i in zip(neuron_weights, layer_output)) + bias
            # Apply rounding and scaling down
            weighted_sum = round_and_scale_down(weighted_sum)
            # Apply ReLU
            neuron_output = relu(weighted_sum)
            next_layer_output.append(neuron_output)
        # Update layer output to next layer's output
        layer_output = next_layer_output

    # Print the final layer's output
    print("Final layer output:", layer_output)
    # Find and return the index of the maximum value in the final output (argmax)
    return np.argmax(layer_output)

# Load weights, biases, and inputs
weights = weights_data["weights"]
biases = weights_data["biases"]
inputs = inputs_data["inputs"]

# Run the neural network on each input and print the computed output and argmax
for i, input_data in enumerate(inputs):
    computed_argmax = neural_network_output(weights, biases, input_data)
    print(f"Input {i+1}: Computed argmax = {computed_argmax}")
