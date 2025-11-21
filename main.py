"""
Plant Disease Fuzzy Diagnosis System
Main application with Gradio interface for user interaction.
Implements Mamdani fuzzy inference for 10 plant diseases.

Author: Knowledge Representation and Reasoning Project
Based on: Research paper on chilli crop diseases
"""

import gradio as gr
import numpy as np
import matplotlib.pyplot as plt
from knowledge.fuzzy_system import (
    create_input_variables,
    create_output_variables,
    create_fuzzy_rules,
    create_control_systems,
    diagnose_diseases,
    interpret_risk,
    get_risk_color,
    explain_diagnosis
)
from knowledge.disease_knowledge import get_disease_info, FUZZY_RULES, get_all_diseases
from ui.visualizations import (
    plot_input_membership_functions,
    plot_output_membership_functions,
    plot_disease_comparison,
    create_membership_summary_table,
    COLORS
)

# Initialize fuzzy system components
print("Initializing Fuzzy Inference System...")
INPUT_VARS = create_input_variables()
OUTPUT_VARS = create_output_variables()
RULES = create_fuzzy_rules(INPUT_VARS, OUTPUT_VARS)
DISEASE_SYSTEMS = create_control_systems(INPUT_VARS, OUTPUT_VARS, RULES)
print(f"System initialized with {len(RULES)} rules for {len(OUTPUT_VARS)} diseases.")


def perform_diagnosis(temp, rh, rain, leafwet, soilm, drain, seedhealth, vector, stage):
    """
    Main diagnosis function that takes input values and returns results.
    
    Args:
        All 9 input variables as individual parameters
    
    Returns:
        tuple: (diagnosis_html, comparison_plot, top_disease_info)
    """
    # Prepare input dictionary
    input_values = {
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
    
    # Perform fuzzy inference
    results = diagnose_diseases(input_values, DISEASE_SYSTEMS)
    
    # Sort by risk score
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    
    # Create HTML table for results
    html = f"""
    <div style="font-family: Arial, sans-serif; padding: 20px; background-color: {COLORS['black']}; border-radius: 10px;">
        <h2 style="color: {COLORS['brown']}; text-align: center; margin-bottom: 20px;">
            🌿 Disease Diagnosis Results 🌿
        </h2>
        <table style="width: 100%; border-collapse: collapse; background-color: white; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <thead>
                <tr style="background-color: {COLORS['brown']}; color: white;">
                    <th style="padding: 12px; text-align: left; border: 1px solid #333;">Rank</th>
                    <th style="padding: 12px; text-align: left; border: 1px solid #333;">Disease</th>
                    <th style="padding: 12px; text-align: left; border: 1px solid #333;">Type</th>
                    <th style="padding: 12px; text-align: center; border: 1px solid #333;">Risk Score</th>
                    <th style="padding: 12px; text-align: center; border: 1px solid #333;">Risk Level</th>
                    <th style="padding: 12px; text-align: center; border: 1px solid #333;">Status</th>
                </tr>
            </thead>
            <tbody>
    """
    
    for rank, (disease, score) in enumerate(sorted_results, 1):
        risk_level = interpret_risk(score)
        color = get_risk_color(risk_level)
        disease_info = get_disease_info(disease)
        disease_type = disease_info.get('type', 'Unknown')
        
        # Status indicator
        if risk_level == 'High':
            status = '🔴 ALERT'
        elif risk_level == 'Moderate':
            status = '🟡 CAUTION'
        else:
            status = '🟢 SAFE'
        
        html += f"""
            <tr style="background-color: {'#f9f9f9' if rank % 2 == 0 else 'white'}; color: #000;">
                <td style="padding: 10px; border: 1px solid #333; font-weight: bold; color: #000;">{rank}</td>
                <td style="padding: 10px; border: 1px solid #333; font-weight: bold; color: #000;">{disease}</td>
                <td style="padding: 10px; border: 1px solid #333; color: #000;"><i>{disease_type}</i></td>
                <td style="padding: 10px; border: 1px solid #333; text-align: center; font-weight: bold; color: #000;">{score:.3f}</td>
                <td style="padding: 10px; border: 1px solid #333; text-align: center;">
                    <span style="background-color: {color}; color: {'white' if risk_level != 'Moderate' else COLORS['brown']}; 
                                 padding: 5px 15px; border-radius: 15px; font-weight: bold;">
                        {risk_level}
                    </span>
                </td>
                <td style="padding: 10px; border: 1px solid #333; text-align: center; font-size: 18px; color: #000;">{status}</td>
            </tr>
        """
    
    html += """
            </tbody>
        </table>
    </div>
    """
    
    # Get explainability - which rules fired
    fired_rules = explain_diagnosis(input_values, DISEASE_SYSTEMS)
    
    # Create explanation section
    explanation_html = f"""
    <div style="font-family: Arial, sans-serif; padding: 20px; background-color: {COLORS['black']}; 
                border-radius: 10px; margin-top: 20px; border: 2px solid {COLORS['brown']};">
        <h2 style="color: {COLORS['brown']}; text-align: center; margin-bottom: 20px; border-bottom: 3px solid {COLORS['brown']}; padding-bottom: 10px;">
            📋 EXPLAINABILITY: Rules That Fired
        </h2>
        <p style="text-align: center; color: #666; margin-bottom: 20px;">
            <i>Understanding how the diagnosis was reached through activated fuzzy rules</i>
        </p>
    """
    
    if fired_rules:
        # Show rules for top 5 diseases with highest risk
        top_diseases = sorted_results[:5]
        
        for disease, score in top_diseases:
            if disease in fired_rules and score > 0.01:  # Only show if has fired rules and non-zero risk
                risk_level = interpret_risk(score)
                color = get_risk_color(risk_level)
                disease_info = get_disease_info(disease)
                
                explanation_html += f"""
                <div style="margin: 15px 0; padding: 15px; background-color: white; 
                            border-left: 5px solid {color}; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    <h3 style="color: {COLORS['brown']}; margin-top: 0;">
                        🦠 {disease} 
                        <span style="background-color: {color}; color: {'white' if risk_level != 'Moderate' else COLORS['brown']}; 
                                     padding: 3px 10px; border-radius: 10px; font-size: 14px; margin-left: 10px;">
                            Risk: {score:.3f} ({risk_level})
                        </span>
                    </h3>
                    <p style="color: #666; font-style: italic; margin: 5px 0;">
                        <strong>Type:</strong> {disease_info.get('type', 'Unknown')} | 
                        <strong>Pathogen:</strong> {disease_info.get('pathogen', 'Unknown')}
                    </p>
                """
                
                # Display fired rules for this disease
                for rule_info in fired_rules[disease]:
                    strength = rule_info['strength']
                    strength_percent = strength * 100
                    
                    # Create visual strength bar
                    filled_blocks = int(strength * 10)
                    bar = '█' * filled_blocks + '░' * (10 - filled_blocks)
                    
                    # Color code by risk level
                    rule_risk = rule_info['risk']
                    rule_color = get_risk_color(rule_risk)
                    
                    # Format conditions
                    conditions_str = " <strong>AND</strong> ".join(
                        [f"{var}=<em>{term}</em>" for var, term in rule_info['conditions'].items()]
                    )
                    
                    explanation_html += f"""
                    <div style="margin: 10px 0; padding: 12px; background-color: #f9f9f9; 
                                border-radius: 5px; border-left: 3px solid {rule_color};">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                            <strong style="color: {COLORS['brown']};">✓ Rule {rule_info['rule_id']}</strong>
                            <span style="font-family: monospace; color: {COLORS['brown']}; font-size: 14px;">
                                Strength: {strength:.3f} ({strength_percent:.1f}%) {bar}
                            </span>
                        </div>
                        <div style="color: #000; font-size: 14px; line-height: 1.6;">
                            <strong style="color: {COLORS['brown']};">IF</strong> {conditions_str}<br>
                            <strong style="color: {COLORS['brown']};">THEN</strong> Risk = 
                            <span style="background-color: {rule_color}; color: {'white' if rule_risk != 'Moderate' else COLORS['brown']}; 
                                         padding: 2px 8px; border-radius: 5px; font-weight: bold;">
                                {rule_risk}
                            </span>
                        </div>
                        <p style="color: #666; font-size: 12px; margin: 8px 0 0 0; font-style: italic;">
                            {rule_info['description']}
                        </p>
                    </div>
                    """
                
                explanation_html += "</div>"
        
        explanation_html += """
        <div style="margin-top: 20px; padding: 15px; background-color: #fff3cd; border-radius: 5px; border-left: 4px solid #856404;">
            <strong style="color: #856404;">💡 How to interpret:</strong>
            <ul style="margin: 10px 0; color: #856404; line-height: 1.8;">
                <li><strong>Strength:</strong> Shows how strongly each rule condition was satisfied (0.0 = not satisfied, 1.0 = fully satisfied)</li>
                <li><strong>Multiple Rules:</strong> Multiple rules can fire simultaneously; the system aggregates them using fuzzy logic</li>
                <li><strong>Fuzzy AND:</strong> Rule strength = minimum membership of all conditions</li>
            </ul>
        </div>
        """
    else:
        explanation_html += """
        <p style="text-align: center; color: #666; padding: 20px;">
            No rules fired significantly. All conditions resulted in very low risk assessments.
        </p>
        """
    
    explanation_html += "</div>"
    
    # Create comparison plot
    fig = plot_disease_comparison(results)
    
    # Get top disease information
    top_disease, top_score = sorted_results[0]
    top_risk = interpret_risk(top_score)
    top_info = get_disease_info(top_disease)
    
    info_html = f"""
    <div style="font-family: Arial, sans-serif; padding: 20px; background-color: {get_risk_color(top_risk)}; 
                color: {'white' if top_risk != 'Moderate' else COLORS['brown']}; border-radius: 10px; margin-top: 20px;">
        <h2 style="margin-top: 0;">🎯 Primary Diagnosis: {top_disease}</h2>
        <p style="font-size: 16px;"><strong>Disease Type:</strong> {top_info.get('type', 'Unknown')}</p>
        <p style="font-size: 16px;"><strong>Pathogen:</strong> <i>{top_info.get('pathogen', 'Unknown')}</i></p>
        <p style="font-size: 16px;"><strong>Risk Level:</strong> {top_risk} ({top_score:.1%} confidence)</p>
        <hr style="border-color: rgba(255,255,255,0.3);">
        <h3>💊 Recommended Treatment:</h3>
        <p style="font-size: 15px; line-height: 1.6;">{top_info.get('treatment', 'Consult agricultural expert.')}</p>
    </div>
    """
    
    return html, fig, info_html, explanation_html


def show_input_plots():
    """Generate and return input membership function plots."""
    fig = plot_input_membership_functions(INPUT_VARS)
    return fig


def show_output_plots():
    """Generate and return output membership function plots."""
    fig = plot_output_membership_functions()
    return fig


def show_rule_base():
    """Generate HTML display of all fuzzy rules."""
    html = f"""
    <div style="font-family: Arial, sans-serif; padding: 20px; background-color: {COLORS['black']}; 
                border-radius: 10px; max-height: 600px; overflow-y: auto;">
        <h2 style="color: {COLORS['brown']}; text-align: center;">📋 Fuzzy Rule Base (30 Rules)</h2>
    """
    
    current_disease = None
    for rule in FUZZY_RULES:
        if rule['disease'] != current_disease:
            if current_disease is not None:
                html += "</div>"
            current_disease = rule['disease']
            disease_info = get_disease_info(current_disease)
            html += f"""
            <div style="margin: 20px 0; padding: 15px; background-color: white; border-left: 5px solid {COLORS['brown']}; border-radius: 5px;">
                <h3 style="color: {COLORS['brown']}; margin-top: 0;">{current_disease} ({disease_info.get('type', '')})</h3>
            """
        
        # Build condition string
        conditions_str = " AND ".join([f"{k}={v}" for k, v in rule['conditions'].items()])
        
        risk_color = get_risk_color(rule['risk'])
        
        html += f"""
        <div style="margin: 10px 0; padding: 10px; background-color: #f9f9f9; border-radius: 5px;">
            <strong>Rule {rule['id']}:</strong><br>
            <span style="color: {COLORS['brown']};">IF</span> {conditions_str} 
            <span style="color: {COLORS['brown']};">THEN</span> 
            <span style="background-color: {risk_color}; color: {'white' if rule['risk'] != 'Moderate' else COLORS['brown']}; 
                         padding: 3px 10px; border-radius: 10px; font-weight: bold;">
                Risk = {rule['risk']}
            </span>
            <br><small style="color: #666;"><i>{rule['description']}</i></small>
        </div>
        """
    
    html += "</div></div>"
    return html


def show_membership_params():
    """Show membership function parameters as text."""
    return f"""
    <div style="font-family: monospace; background-color: {COLORS['brown']}; color: {COLORS['gunmetal']}; 
                padding: 20px; border-radius: 10px; white-space: pre-wrap; max-height: 600px; overflow-y: auto;">
{create_membership_summary_table()}
    </div>
    """


# Create Gradio Interface
with gr.Blocks(
    title="🌿 Plant Disease Fuzzy Diagnosis System",
    theme=gr.themes.Base(
        primary_hue="green",
        secondary_hue="orange"
    ),
    css=f"""
        .gradio-container {{
            font-family: Arial, sans-serif;
        }}
        h1 {{
            color: {COLORS['brown']};
            text-align: center;
        }}
    """
) as app:
    
    gr.Markdown(
        f"""
        # 🌿 Plant Disease Fuzzy Diagnosis System
        ### Intelligent Disease Detection Using Fuzzy Logic Inference
        
        This system uses **Mamdani Fuzzy Inference** with **30 rules** to diagnose **10 different plant diseases** 
        based on environmental conditions and plant health indicators.
        
        **Diseases Covered:** Anthracnose, Powdery Mildew, Fusarium Wilt, Phytophthora, Cercospora, 
        Bacterial Leaf Spot, Bacterial Wilt, Viral Leaf Curl, Mosaic Viruses, Nematodes
        """
    )
    
    with gr.Tabs():
        # Tab 1: Diagnosis
        with gr.Tab("🔬 Diagnosis"):
            gr.Markdown("### Enter Environmental and Plant Conditions")
            
            with gr.Row():
                with gr.Column():
                    gr.Markdown("#### 🌡️ Environmental Factors")
                    temp_slider = gr.Slider(10, 40, value=25, step=0.5, label="Temperature (°C)")
                    rh_slider = gr.Slider(10, 100, value=60, step=1, label="Relative Humidity (%)")
                    rain_slider = gr.Slider(0, 200, value=50, step=5, label="Rainfall (mm)")
                    leafwet_slider = gr.Slider(0, 24, value=8, step=0.5, label="Leaf Wetness Duration (hours)")
                
                with gr.Column():
                    gr.Markdown("#### 🌱 Soil & Plant Factors")
                    soilm_slider = gr.Slider(0, 100, value=45, step=1, label="Soil Moisture (%)")
                    drain_slider = gr.Slider(0, 10, value=5, step=0.5, label="Soil Drainage (0-10)")
                    seedhealth_slider = gr.Slider(0, 10, value=7, step=0.5, label="Seed Health (0-10)")
                    vector_slider = gr.Slider(0, 10, value=3, step=0.5, label="Vector Pressure (0-10)")
                    stage_slider = gr.Slider(0, 3, value=1.5, step=0.1, 
                                            label="Crop Stage (0=Seedling, 1=Vegetative, 2=Flowering, 3=Fruiting)")
            
            diagnose_btn = gr.Button("🔍 Diagnose Diseases", variant="primary", size="lg")
            
            gr.Markdown("### 📊 Diagnosis Results")
            diagnosis_output = gr.HTML()
            
            with gr.Row():
                comparison_plot = gr.Plot(label="Disease Risk Comparison")
            
            top_disease_info = gr.HTML()
            
            gr.Markdown("### 🔍 Rule Explanation")
            explanation_output = gr.HTML()
            
            # Connect diagnosis button
            diagnose_btn.click(
                fn=perform_diagnosis,
                inputs=[temp_slider, rh_slider, rain_slider, leafwet_slider, soilm_slider,
                       drain_slider, seedhealth_slider, vector_slider, stage_slider],
                outputs=[diagnosis_output, comparison_plot, top_disease_info, explanation_output]
            )
            diagnose_btn.click(
                fn=perform_diagnosis,
                inputs=[temp_slider, rh_slider, rain_slider, leafwet_slider, soilm_slider,
                       drain_slider, seedhealth_slider, vector_slider, stage_slider],
                outputs=[diagnosis_output, comparison_plot, top_disease_info, explanation_output]
            )
        
        # Tab 2: Membership Functions
        with gr.Tab("📈 Membership Functions"):
            gr.Markdown("### Fuzzy Membership Function Visualizations")
            
            with gr.Row():
                show_input_btn = gr.Button("Show Input Variables", variant="secondary")
                show_output_btn = gr.Button("Show Output Variables", variant="secondary")
            
            membership_plot = gr.Plot(label="Membership Functions")
            
            show_input_btn.click(fn=show_input_plots, outputs=membership_plot)
            show_output_btn.click(fn=show_output_plots, outputs=membership_plot)
            
            gr.Markdown("### 📝 Membership Function Parameters")
            membership_params = gr.HTML(value=show_membership_params())
        
        # Tab 3: Rule Base
        with gr.Tab("📋 Rule Base"):
            gr.Markdown("### Complete Fuzzy Rule Base")
            rules_display = gr.HTML(value=show_rule_base())
    
    gr.Markdown(
        """
        ---
        <div style="text-align: center; color: #573d1c;">
            <p>💚 Plant Disease Fuzzy Diagnosis System | Powered by Fuzzy Logic & AI</p>
        </div>
        """
    )


if __name__ == "__main__":
    print("\n" + "="*60)
    print("🌿 PLANT DISEASE FUZZY DIAGNOSIS SYSTEM 🌿")
    print("="*60)
    print(f"✅ Loaded {len(INPUT_VARS)} input variables")
    print(f"✅ Loaded {len(OUTPUT_VARS)} disease outputs")
    print(f"✅ Loaded {len(RULES)} fuzzy rules")
    print(f"✅ Created unified inference system")
    print("="*60)
    print("🚀 Launching Gradio interface...\n")
    
    app.launch(
        share=False,
        server_name="127.0.0.1",
        server_port=7860,
        show_error=True
    )
