"""
Quick test to verify fuzzy inference is working
"""

from fuzzy_system import (
    create_input_variables,
    create_output_variables,
    create_fuzzy_rules,
    create_control_systems,
    diagnose_diseases
)

# Initialize system
print("Initializing system...")
input_vars = create_input_variables()
output_vars = create_output_variables()
rules = create_fuzzy_rules(input_vars, output_vars)
system = create_control_systems(input_vars, output_vars, rules)

print(f"Created unified system with {len(rules)} rules for {len(output_vars)} diseases")

# Test with favorable conditions for Anthracnose
# (High temp, high humidity, high rain, long leaf wetness)
test_inputs = {
    'Temp': 30.0,      # High
    'RH': 85.0,        # High
    'Rain': 150.0,     # High
    'LeafWet': 18.0,   # Long
    'SoilM': 70.0,     # High
    'Drain': 3.0,      # Poor
    'SeedHealth': 5.0, # Moderate
    'Vector': 5.0,     # Moderate
    'Stage': 2.0       # Flowering
}

print("\n" + "="*60)
print("Testing with inputs favorable for Anthracnose:")
print("="*60)
for key, val in test_inputs.items():
    print(f"  {key}: {val}")

print("\nRunning diagnosis...")
results = diagnose_diseases(test_inputs, system)

print("\n" + "="*60)
print("RESULTS:")
print("="*60)
for disease, score in sorted(results.items(), key=lambda x: x[1], reverse=True):
    print(f"{disease:25s}: {score:.4f}")
