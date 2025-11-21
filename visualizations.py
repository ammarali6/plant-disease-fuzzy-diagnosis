"""
Visualization Module for Fuzzy Membership Functions
Creates matplotlib plots for all input and output membership functions.
"""

import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from matplotlib.figure import Figure


# Custom color scheme: ff4b3e, 81c14b, 573d1c, 454545, 000000
COLORS = {
    'red': '#ff4b3e',
    'green': '#81c14b',
    'brown': '#573d1c',
    'gunmetal': '#454545',
    'black': '#000000'
}


def plot_input_membership_functions(input_vars):
    """
    Create comprehensive plots for all 9 input membership functions.
    
    Args:
        input_vars: Dictionary of skfuzzy Antecedent objects
    
    Returns:
        matplotlib.figure.Figure: Figure with all subplots
    """
    fig = plt.figure(figsize=(16, 12))
    fig.suptitle('Input Variable Membership Functions', fontsize=16, fontweight='bold')
    
    var_configs = [
        ('Temp', 'Temperature (°C)', 1),
        ('RH', 'Relative Humidity (%)', 2),
        ('Rain', 'Rainfall (mm)', 3),
        ('LeafWet', 'Leaf Wetness Duration (hours)', 4),
        ('SoilM', 'Soil Moisture (%)', 5),
        ('Drain', 'Soil Drainage (0-10)', 6),
        ('SeedHealth', 'Seed Health (0-10)', 7),
        ('Vector', 'Vector Pressure (0-10)', 8),
        ('Stage', 'Crop Stage (0-3)', 9)
    ]
    
    for var_name, label, pos in var_configs:
        ax = fig.add_subplot(3, 3, pos)
        var = input_vars[var_name]
        
        # Plot each membership function
        colors_list = [COLORS['green'], COLORS['black'], COLORS['red']]
        for idx, term in enumerate(var.terms):
            color = colors_list[idx % len(colors_list)]
            ax.plot(var.universe, var[term].mf, linewidth=2, label=term, color=color)
            ax.fill_between(var.universe, 0, var[term].mf, alpha=0.3, color=color)
        
        ax.set_title(label, fontweight='bold')
        ax.set_xlabel('Value')
        ax.set_ylabel('Membership Degree')
        ax.set_ylim([-0.05, 1.05])
        ax.legend(loc='upper right', fontsize=8)
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_output_membership_functions():
    """
    Create plot for disease risk output membership functions.
    All diseases share the same risk levels: Low, Moderate, High.
    
    Returns:
        matplotlib.figure.Figure: Figure with risk membership functions
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create universe for risk (0-1)
    risk_universe = np.arange(0, 1.01, 0.01)
    
    # Define membership functions
    low = fuzz.trimf(risk_universe, [0, 0, 0.4])
    moderate = fuzz.trimf(risk_universe, [0.25, 0.5, 0.75])
    high = fuzz.trimf(risk_universe, [0.6, 1, 1])
    
    # Plot with custom colors
    ax.plot(risk_universe, low, linewidth=2.5, label='Low Risk', color=COLORS['green'])
    ax.fill_between(risk_universe, 0, low, alpha=0.3, color=COLORS['green'])
    
    ax.plot(risk_universe, moderate, linewidth=2.5, label='Moderate Risk', color=COLORS['black'])
    ax.fill_between(risk_universe, 0, moderate, alpha=0.3, color=COLORS['black'])
    
    ax.plot(risk_universe, high, linewidth=2.5, label='High Risk', color=COLORS['red'])
    ax.fill_between(risk_universe, 0, high, alpha=0.3, color=COLORS['red'])
    
    ax.set_title('Disease Risk Output Membership Functions', fontsize=14, fontweight='bold')
    ax.set_xlabel('Risk Score (0-1)', fontsize=12)
    ax.set_ylabel('Membership Degree', fontsize=12)
    ax.set_ylim([-0.05, 1.05])
    ax.legend(loc='upper center', fontsize=10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_single_input_variable(var_name, var_obj):
    """
    Create detailed plot for a single input variable.
    Useful for focused visualization in the interface.
    
    Args:
        var_name: Name of the variable
        var_obj: skfuzzy Antecedent object
    
    Returns:
        matplotlib.figure.Figure: Figure for single variable
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    
    colors_list = [COLORS['green'], COLORS['brown'], COLORS['red']]
    
    for idx, term in enumerate(var_obj.terms):
        color = colors_list[idx % len(colors_list)]
        ax.plot(var_obj.universe, var_obj[term].mf, linewidth=2.5, label=term, color=color)
        ax.fill_between(var_obj.universe, 0, var_obj[term].mf, alpha=0.3, color=color)
    
    ax.set_title(f'{var_name} Membership Functions', fontsize=14, fontweight='bold')
    ax.set_xlabel('Value', fontsize=12)
    ax.set_ylabel('Membership Degree', fontsize=12)
    ax.set_ylim([-0.05, 1.05])
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_disease_comparison(disease_results):
    """
    Create bar chart comparing risk levels across all diseases.
    
    Args:
        disease_results: Dictionary of disease names to risk scores
    
    Returns:
        matplotlib.figure.Figure: Bar chart figure
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Sort diseases by risk score
    sorted_diseases = sorted(disease_results.items(), key=lambda x: x[1], reverse=True)
    diseases = [d[0] for d in sorted_diseases]
    scores = [d[1] for d in sorted_diseases]
    
    # Color bars based on risk level
    colors = []
    for score in scores:
        if score < 0.4:
            colors.append(COLORS['green'])
        elif score < 0.6:
            colors.append(COLORS['black'])
        else:
            colors.append(COLORS['red'])
    
    bars = ax.barh(diseases, scores, color=colors, edgecolor=COLORS['brown'], linewidth=1.5)
    
    # Add score labels on bars
    for bar, score in zip(bars, scores):
        width = bar.get_width()
        ax.text(width + 0.02, bar.get_y() + bar.get_height()/2, 
                f'{score:.2f}', ha='left', va='center', fontweight='bold')
    
    ax.set_xlabel('Risk Score (0-1)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Disease', fontsize=12, fontweight='bold')
    ax.set_title('Disease Risk Assessment Comparison', fontsize=14, fontweight='bold')
    ax.set_xlim([0, 1.1])
    ax.grid(True, alpha=0.3, axis='x')
    
    # Add risk zone backgrounds
    ax.axvspan(0, 0.4, alpha=0.1, color=COLORS['green'], label='Low Risk Zone')
    ax.axvspan(0.4, 0.6, alpha=0.1, color=COLORS['black'], label='Moderate Risk Zone')
    ax.axvspan(0.6, 1, alpha=0.1, color=COLORS['red'], label='High Risk Zone')
    
    plt.tight_layout()
    return fig


def create_membership_summary_table():
    """
    Create a text summary of all membership function parameters.
    Useful for report documentation.
    
    Returns:
        str: Formatted text with all membership function definitions
    """
    summary = """
MEMBERSHIP FUNCTION PARAMETERS (Triangular - trimf)
====================================================

INPUT VARIABLES:
----------------

1. Temperature (Temp): Universe = [10, 40] °C
   - Low:      trimf([10, 10, 20])
   - Moderate: trimf([18, 24, 30])
   - High:     trimf([28, 40, 40])

2. Relative Humidity (RH): Universe = [10, 100] %
   - Low:      trimf([10, 10, 45])
   - Moderate: trimf([40, 60, 80])
   - High:     trimf([75, 100, 100])

3. Rainfall (Rain): Universe = [0, 200] mm
   - None: trimf([0, 0, 10])
   - Low:  trimf([5, 25, 50])
   - High: trimf([40, 100, 200])

4. Leaf Wetness Duration (LeafWet): Universe = [0, 24] hours
   - Short:  trimf([0, 0, 6])
   - Medium: trimf([4, 10, 16])
   - Long:   trimf([12, 24, 24])

5. Soil Moisture (SoilM): Universe = [0, 100] %
   - Dry: trimf([0, 0, 30])
   - Opt: trimf([20, 45, 65])
   - Wet: trimf([55, 100, 100])

6. Soil Drainage (Drain): Universe = [0, 10]
   - Poor:     trimf([0, 0, 3])
   - Moderate: trimf([2.5, 5, 7.5])
   - Good:     trimf([7, 10, 10])

7. Seed Health (SeedHealth): Universe = [0, 10]
   - Poor: trimf([0, 0, 3])
   - Fair: trimf([2.5, 5, 7.5])
   - Good: trimf([7, 10, 10])

8. Vector Pressure (Vector): Universe = [0, 10]
   - None:     trimf([0, 0, 2])
   - Moderate: trimf([1.5, 5, 8.5])
   - High:     trimf([7.5, 10, 10])

9. Crop Stage (Stage): Universe = [0, 3]
   - Seedling:   trimf([0, 0, 0.5])
   - Vegetative: trimf([0.5, 1, 1.5])
   - Flowering:  trimf([1.5, 2, 2.5])
   - Fruiting:   trimf([2.5, 3, 3])

OUTPUT VARIABLE:
----------------

Disease Risk: Universe = [0, 1]
   - Low:      trimf([0, 0, 0.4])
   - Moderate: trimf([0.25, 0.5, 0.75])
   - High:     trimf([0.6, 1, 1])

JUSTIFICATION:
--------------
Triangular membership functions (trimf) were chosen because:
1. Simple and computationally efficient
2. Easy to interpret and explain to users
3. Suitable for agricultural data with clear boundaries
4. Widely used in fuzzy expert systems
5. Supported by domain expert knowledge from research
"""
    return summary
