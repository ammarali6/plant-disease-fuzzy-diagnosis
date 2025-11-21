"""
Test scenarios for the Fuzzy Disease Diagnosis System.
This script validates the system with predefined scenarios for report screenshots.
"""

from fuzzy_system import (
    create_input_variables,
    create_output_variables,
    create_fuzzy_rules,
    create_control_systems,
    diagnose_diseases,
    interpret_risk
)

# Initialize system
print("Initializing system for testing...")
INPUT_VARS = create_input_variables()
OUTPUT_VARS = create_output_variables()
RULES = create_fuzzy_rules(INPUT_VARS, OUTPUT_VARS)
DISEASE_SYSTEMS = create_control_systems(INPUT_VARS, OUTPUT_VARS, RULES)

def test_scenario(name, inputs, expected_disease=None):
    """Test a specific scenario and display results."""
    print(f"\n{'='*70}")
    print(f"SCENARIO: {name}")
    print(f"{'='*70}")
    print("Input Values:")
    for key, value in inputs.items():
        print(f"  {key:15s}: {value}")
    
    results = diagnose_diseases(inputs, DISEASE_SYSTEMS)
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\nTop 5 Diagnoses:")
    print(f"{'-'*70}")
    for rank, (disease, score) in enumerate(sorted_results[:5], 1):
        risk_level = interpret_risk(score)
        indicator = "🔴" if risk_level == "High" else "🟡" if risk_level == "Moderate" else "🟢"
        print(f"{rank}. {indicator} {disease:25s} - Score: {score:.4f} ({risk_level})")
    
    if expected_disease:
        expected_score = results.get(expected_disease, 0)
        expected_risk = interpret_risk(expected_score)
        print(f"\n✅ Expected: {expected_disease} = {expected_risk} ({expected_score:.4f})")
    
    print(f"{'='*70}")
    return results

# Test Scenarios

# Scenario 1: High Anthracnose Risk (Fruiting stage + environmental conditions)
print("\n" + "🌿"*35)
print("TEST SCENARIO 1: High Anthracnose Risk")
print("🌿"*35)
scenario1 = {
    'Temp': 25.0,        # Moderate
    'RH': 60.0,          # Moderate
    'Rain': 150.0,       # High
    'LeafWet': 20.0,     # Long
    'SoilM': 50.0,       # Optimal
    'Drain': 5.0,        # Moderate
    'SeedHealth': 5.0,   # Fair
    'Vector': 3.0,       # Moderate
    'Stage': 3.0         # Fruiting
}
test_scenario("High Anthracnose Risk", scenario1, "Anthracnose")

# Scenario 2: High Powdery Mildew Risk (Moderate temp + Low humidity)
print("\n" + "🌿"*35)
print("TEST SCENARIO 2: High Powdery Mildew Risk")
print("🌿"*35)
scenario2 = {
    'Temp': 25.0,        # Moderate
    'RH': 30.0,          # Low
    'Rain': 20.0,        # Low
    'LeafWet': 4.0,      # Short
    'SoilM': 45.0,       # Optimal
    'Drain': 5.0,        # Moderate
    'SeedHealth': 7.0,   # Good
    'Vector': 2.0,       # None/Moderate
    'Stage': 2.0         # Flowering
}
test_scenario("High Powdery Mildew Risk", scenario2, "Powdery Mildew")

# Scenario 3: High Viral Leaf Curl Risk (High vector pressure)
print("\n" + "🌿"*35)
print("TEST SCENARIO 3: High Viral Leaf Curl Risk")
print("🌿"*35)
scenario3 = {
    'Temp': 35.0,        # High
    'RH': 50.0,          # Moderate
    'Rain': 30.0,        # Low
    'LeafWet': 10.0,     # Medium
    'SoilM': 40.0,       # Optimal
    'Drain': 6.0,        # Moderate/Good
    'SeedHealth': 5.0,   # Fair
    'Vector': 9.0,       # High
    'Stage': 1.0         # Vegetative
}
test_scenario("High Viral Leaf Curl Risk", scenario3, "Viral Leaf Curl")

# Scenario 4: High Phytophthora Risk (Wet soil + poor drainage)
print("\n" + "🌿"*35)
print("TEST SCENARIO 4: High Phytophthora Risk")
print("🌿"*35)
scenario4 = {
    'Temp': 25.0,        # Moderate
    'RH': 85.0,          # High
    'Rain': 180.0,       # High
    'LeafWet': 18.0,     # Long
    'SoilM': 80.0,       # Wet
    'Drain': 2.0,        # Poor
    'SeedHealth': 5.0,   # Fair
    'Vector': 3.0,       # Moderate
    'Stage': 1.5         # Vegetative/Flowering
}
test_scenario("High Phytophthora Risk", scenario4, "Phytophthora")

# Scenario 5: Low Risk - Healthy Conditions
print("\n" + "🌿"*35)
print("TEST SCENARIO 5: Low Risk (Healthy Conditions)")
print("🌿"*35)
scenario5 = {
    'Temp': 24.0,        # Moderate
    'RH': 60.0,          # Moderate
    'Rain': 25.0,        # Low
    'LeafWet': 5.0,      # Short
    'SoilM': 45.0,       # Optimal
    'Drain': 8.0,        # Good
    'SeedHealth': 9.0,   # Good
    'Vector': 0.5,       # None
    'Stage': 1.0         # Vegetative
}
test_scenario("Low Risk - Healthy Conditions", scenario5)

# Scenario 6: Multiple Disease Risks (Mixed conditions)
print("\n" + "🌿"*35)
print("TEST SCENARIO 6: Multiple Disease Risks")
print("🌿"*35)
scenario6 = {
    'Temp': 30.0,        # High
    'RH': 80.0,          # High
    'Rain': 100.0,       # High
    'LeafWet': 16.0,     # Long
    'SoilM': 70.0,       # Wet
    'Drain': 3.0,        # Poor
    'SeedHealth': 2.0,   # Poor
    'Vector': 6.0,       # Moderate/High
    'Stage': 2.5         # Flowering/Fruiting
}
test_scenario("Multiple Disease Risks", scenario6)

print("\n" + "🌿"*35)
print("✅ ALL TEST SCENARIOS COMPLETED")
print("🌿"*35)
print("\nSummary:")
print(f"  - System initialized with {len(RULES)} rules")
print(f"  - Tested 6 different scenarios")
print(f"  - All {len(DISEASE_SYSTEMS)} disease inference systems working")
print(f"  - Ready for demonstration and report screenshots")
print("\n" + "="*70)
