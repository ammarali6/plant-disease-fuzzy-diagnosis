"""
Fuzzy Inference System for Plant Disease Diagnosis
Implements Mamdani fuzzy inference with triangular membership functions.
Based on research paper fuzzy model with 9 input variables and 10 disease outputs.
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from disease_knowledge import FUZZY_RULES, get_all_diseases


def create_input_variables():
    """
    Create all 9 fuzzy input variables with their membership functions.
    All membership functions use triangular (trimf) as per research paper.
    
    Explanation:
    temp = ctrl.Antecedent creates the input variable
    np.arange creates UoD with 10-40.1 being range and 0.1 is resolution
    
    next 3 lines define fuzzy sets
    temp.universe correspond to params [a,b,c] of triangle:
    triangle starts at a
    peak (100% membership) is at b
    triangle ends at c

    Returns:
        dict: Dictionary of skfuzzy Antecedent objects
    """
    
    # 1. Temperature (10-40°C)
    temp = ctrl.Antecedent(np.arange(10, 40.1, 0.1), 'Temp')
    temp['Low'] = fuzz.trimf(temp.universe, [10, 10, 20]) # Left Shoulder
    temp['Moderate'] = fuzz.trimf(temp.universe, [18, 24, 30]) # Standard Triangle
    temp['High'] = fuzz.trimf(temp.universe, [28, 40, 40]) # Right Shoulder
    
    # 2. Relative Humidity (10-100%)
    rh = ctrl.Antecedent(np.arange(10, 100.1, 0.1), 'RH')
    rh['Low'] = fuzz.trimf(rh.universe, [10, 10, 45])
    rh['Moderate'] = fuzz.trimf(rh.universe, [40, 60, 80])
    rh['High'] = fuzz.trimf(rh.universe, [75, 100, 100])
    
    # 3. Rainfall (0-200 mm)
    rain = ctrl.Antecedent(np.arange(0, 200.1, 0.1), 'Rain')
    rain['None'] = fuzz.trimf(rain.universe, [0, 0, 10])
    rain['Low'] = fuzz.trimf(rain.universe, [5, 25, 50])
    rain['High'] = fuzz.trimf(rain.universe, [40, 100, 200])
    
    # 4. Leaf Wetness Duration (0-24 hours/day)
    leafwet = ctrl.Antecedent(np.arange(0, 24.1, 0.1), 'LeafWet')
    leafwet['Short'] = fuzz.trimf(leafwet.universe, [0, 0, 6])
    leafwet['Medium'] = fuzz.trimf(leafwet.universe, [4, 10, 16])
    leafwet['Long'] = fuzz.trimf(leafwet.universe, [12, 24, 24])
    
    # 5. Soil Moisture (0-100%)
    soilm = ctrl.Antecedent(np.arange(0, 100.1, 0.1), 'SoilM')
    soilm['Dry'] = fuzz.trimf(soilm.universe, [0, 0, 30])
    soilm['Opt'] = fuzz.trimf(soilm.universe, [20, 45, 65])
    soilm['Wet'] = fuzz.trimf(soilm.universe, [55, 100, 100])
    
    # 6. Soil Drainage (0-10 scale)
    drain = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'Drain')
    drain['Poor'] = fuzz.trimf(drain.universe, [0, 0, 3])
    drain['Moderate'] = fuzz.trimf(drain.universe, [2.5, 5, 7.5])
    drain['Good'] = fuzz.trimf(drain.universe, [7, 10, 10])
    
    # 7. Seed Health (0-10 scale)
    seedhealth = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'SeedHealth')
    seedhealth['Poor'] = fuzz.trimf(seedhealth.universe, [0, 0, 3])
    seedhealth['Fair'] = fuzz.trimf(seedhealth.universe, [2.5, 5, 7.5])
    seedhealth['Good'] = fuzz.trimf(seedhealth.universe, [7, 10, 10])
    
    # 8. Vector Pressure (0-10 scale)
    vector = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'Vector')
    vector['None'] = fuzz.trimf(vector.universe, [0, 0, 2])
    vector['Moderate'] = fuzz.trimf(vector.universe, [1.5, 5, 8.5])
    vector['High'] = fuzz.trimf(vector.universe, [7.5, 10, 10])
    
    # 9. Crop Stage (0-3: Seedling=0, Vegetative=1, Flowering=2, Fruiting=3)
    stage = ctrl.Antecedent(np.arange(0, 3.1, 0.1), 'Stage')
    stage['Seedling'] = fuzz.trimf(stage.universe, [0, 0, 0.5])
    stage['Vegetative'] = fuzz.trimf(stage.universe, [0.5, 1, 1.5])
    stage['Flowering'] = fuzz.trimf(stage.universe, [1.5, 2, 2.5])
    stage['Fruiting'] = fuzz.trimf(stage.universe, [2.5, 3, 3])
    
    return {
        'Temp': temp,
        'RH': rh,
        'Rain': rain,
        'LeafWet': leafwet,
        'SoilM': soilm,
        'Drain': drain,
        'SeedHealth': seedhealth,
        'Vector': vector,
        'Stage': stage
    }


def create_output_variables():
    """
    Create output variables for all 10 diseases.
    Each disease has Risk levels: Low, Moderate, High
    
    Returns:
        dict: Dictionary of skfuzzy Consequent objects for each disease
    """
    diseases = get_all_diseases()
    output_vars = {}
    
    for disease in diseases:
        # Create risk output variable (0-1 scale)

        # Consequent takes params universe,label
        risk = ctrl.Consequent(np.arange(0, 1.01, 0.01), disease)
        
        # Define risk membership functions (same for all diseases)
        risk['Low'] = fuzz.trimf(risk.universe, [0, 0, 0.4])
        risk['Moderate'] = fuzz.trimf(risk.universe, [0.25, 0.5, 0.75])
        risk['High'] = fuzz.trimf(risk.universe, [0.6, 1, 1])
        
        output_vars[disease] = risk
    
    return output_vars


def create_fuzzy_rules(input_vars, output_vars):
    """
    Create all 30 fuzzy rules from the research paper.
    Each rule maps input conditions to disease risk levels.
    
    Args:
        input_vars: Dictionary of input Antecedent objects
        output_vars: Dictionary of output Consequent objects
    
    Returns:
        list: List of skfuzzy Rule objects
    """
    rules = []
    
    for rule_def in FUZZY_RULES:
        disease = rule_def['disease']
        conditions = rule_def['conditions']
        risk_level = rule_def['risk']
        
        # Build antecedent (IF part) by combining all conditions
        antecedent_parts = []
        for var_name, fuzzy_term in conditions.items():
            antecedent_parts.append(input_vars[var_name][fuzzy_term])
        
        # Combine conditions with AND operator
        if len(antecedent_parts) == 1:
            antecedent = antecedent_parts[0]
        else:
            antecedent = antecedent_parts[0]
            for part in antecedent_parts[1:]:
                antecedent = antecedent & part
        
        # Build consequent (THEN part)
        consequent = output_vars[disease][risk_level]
        
        # Create rule
        rule = ctrl.Rule(antecedent, consequent, label=f"Rule {rule_def['id']}")
        rules.append(rule)
    
    return rules


def create_control_systems(input_vars, output_vars, rules):
    """
    Create a single unified control system with all rules.
    All diseases are computed together with all inputs available.
    
    Args:
        input_vars: Dictionary of input variables
        output_vars: Dictionary of output variables  
        rules: List of all fuzzy rules
    
    Returns:
        ControlSystemSimulation: Single simulation object for all diseases
    """
    # Create one unified control system with ALL rules
    ctrl_system = ctrl.ControlSystem(rules)
    simulation = ctrl.ControlSystemSimulation(ctrl_system)
    
    print(f"🔍 Created unified control system with {len(rules)} rules for {len(output_vars)} diseases")
    
    return simulation


def diagnose_diseases(input_values, disease_system):
    """
    Perform fuzzy inference to diagnose all diseases using unified system.
    
    Args:
        input_values: Dictionary of input variable values
        disease_system: Unified ControlSystemSimulation object
    
    Returns:
        dict: Dictionary of disease names to risk scores (0-1)
    """
    results = {}
    
    # Debug: Print input values
    print("\n🔍 DEBUG - Input values received:")
    for var, val in input_values.items():
        print(f"  {var}: {val}")
    
    try:
        # Set ALL input values on the unified system
        for var_name, value in input_values.items():
            disease_system.input[var_name] = value
        
        # Compute fuzzy inference once for all diseases
        disease_system.compute()
        
        # Extract outputs for each disease
        for disease in get_all_diseases():
            try:
                risk_score = disease_system.output[disease]
                results[disease] = risk_score
                print(f"✅ {disease}: {risk_score:.4f}")
            except KeyError:
                # Disease output not available (no rules fired strongly enough)
                results[disease] = 0.0
                print(f"⚠️  {disease}: 0.0000 (no rules fired)")
        
    except Exception as e:
        # If computation fails entirely, assign low risk to all
        print(f"❌ Error during computation: {e}")
        import traceback
        traceback.print_exc()
        for disease in get_all_diseases():
            results[disease] = 0.0
    
    return results


def interpret_risk(risk_score):
    """
    Convert risk score to linguistic term.
    
    Args:
        risk_score: Float between 0 and 1
    
    Returns:
        str: Risk level (Low, Moderate, or High)
    """
    if risk_score < 0.4:
        return 'Low'
    elif risk_score < 0.6:
        return 'Moderate'
    else:
        return 'High'


def get_risk_color(risk_level):
    """
    Get color code for risk level using custom color scheme.
    Color scheme: ff4b3e (red), 81c14b (green), 573d1c (brown), 454545 (gunmetal), 000000 (black)
    
    Args:
        risk_level: String (Low, Moderate, or High)
    
    Returns:
        str: Hex color code
    """
    colors = {
        'Low': '#81c14b',      # Green
        'Moderate': '#000000',  # Black (neutral)
        'High': '#ff4b3e'       # Red
    }
    return colors.get(risk_level, '#000000')


def explain_diagnosis(input_values, disease_system):
    """
    Extract which rules fired and their activation strengths for explainability.
    Uses scikit-fuzzy's aggregate_firing attribute to get actual rule activations.
    
    This provides transparency by showing:
    - Which rules contributed to each disease diagnosis
    - How strongly each rule activated (firing strength)
    - The conditions and consequences of fired rules
    
    Args:
        input_values: Dictionary of input variable values
        disease_system: Unified ControlSystemSimulation object
    
    Returns:
        dict: Dictionary mapping disease names to list of fired rules with details
              Format: {
                  'Disease': [
                      {
                          'rule_id': int,
                          'strength': float,
                          'conditions': dict,
                          'risk': str,
                          'description': str
                      }, ...
                  ]
              }
    """
    fired_rules_by_disease = {}
    
    try:
        # Set ALL input values (should already be set from diagnose_diseases)
        for var_name, value in input_values.items():
            disease_system.input[var_name] = value
        
        # Compute inference (should already be computed, but ensure it's done)
        disease_system.compute()
        
        # Group fired rules by disease
        for rule in disease_system.ctrl.rules:
            # Access the aggregate_firing using the simulation object as index
            # StatePerSimulation requires bracket notation
            try:
                activation_strength = rule.aggregate_firing[disease_system]
            except (KeyError, TypeError):
                activation_strength = 0.0
            
            # Only include rules that actually fired (strength > 0.01 threshold)
            if activation_strength > 0.01:
                # Find the corresponding rule definition from FUZZY_RULES
                rule_label = str(rule.label)  # e.g., "Rule 1"
                rule_id = int(rule_label.split()[-1]) if 'Rule' in rule_label else 0
                
                # Get rule details from FUZZY_RULES
                rule_def = next((r for r in FUZZY_RULES if r['id'] == rule_id), None)
                
                if rule_def:
                    disease = rule_def['disease']
                    
                    if disease not in fired_rules_by_disease:
                        fired_rules_by_disease[disease] = []
                    
                    fired_rules_by_disease[disease].append({
                        'rule_id': rule_id,
                        'strength': activation_strength,
                        'conditions': rule_def['conditions'],
                        'risk': rule_def['risk'],
                        'description': rule_def['description']
                    })
        
        # Sort rules by strength for each disease
        for disease in fired_rules_by_disease:
            fired_rules_by_disease[disease].sort(key=lambda x: x['strength'], reverse=True)
                
    except Exception as e:
        # If extraction fails, print error
        print(f"❌ Error in explain_diagnosis: {e}")
        import traceback
        traceback.print_exc()
    
    return fired_rules_by_disease
