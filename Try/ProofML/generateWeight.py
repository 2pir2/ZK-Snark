import json
import random

def relu(x):
    return max(0, x)

def generate_weights_and_biases(layers, neurons_per_layer):
    weights = []
    biases = []
    for i in range(layers):
        # Generate weights for each neuron in the layer
        layer_weights = [
            [random.uniform(-1, 1) for _ in range(neurons_per_layer)] 
            for _ in range(neurons_per_layer)
        ]
        weights.append(layer_weights)

        # Generate biases for each neuron in the layer
        layer_biases = [random.uniform(-1, 1) for _ in range(neurons_per_layer)]
        biases.append(layer_biases)
    
    return weights, biases

def simulate_neural_network(weights, biases, input_vector):
    current_output = input_vector
    for layer_weights, layer_biases in zip(weights, biases):
        next_output = []
        for neuron_weights, neuron_bias in zip(layer_weights, layer_biases):
            weighted_sum = sum(w * x for w, x in zip(neuron_weights, current_output)) + neuron_bias
            next_output.append(relu(weighted_sum))
        current_output = next_output
    return current_output

def generate_data(layers, neurons_per_layer, filename_weights, filename_expected):
    # Generate weights and biases
    weights, biases = generate_weights_and_biases(layers, neurons_per_layer)
    
    # Generate a random input vector
    input_vector = [random.uniform(0, 1) for _ in range(neurons_per_layer)]
    
    # Simulate the expected output
    expected_output = simulate_neural_network(weights, biases, input_vector)
    
    # Save weights and biases to a file
    with open(filename_weights, "w") as f:
        json.dump({"weights": weights, "biases": biases}, f, indent=4)
    
    # Save expected output to a file
    with open(filename_expected, "w") as f:
        json.dump({"outputs": expected_output}, f, indent=4)

# Generate files for different sizes
sizes = [(2, 5), (10, 10), (20, 50), (100, 100)]  # (layers, neurons per layer)
for size, i in zip(sizes, [10, 100, 1000, 10000]):
    layers, neurons = size
    generate_data(
        layers, neurons, 
        f"weights_{i}.json", 
        f"expected_{i}.json"
    )
