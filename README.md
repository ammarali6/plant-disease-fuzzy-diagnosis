# 🌿 Plant Disease Fuzzy Diagnosis System

An intelligent plant disease diagnosis system using **Mamdani Fuzzy Logic Inference** to identify 10 different diseases in chilli crops based on environmental conditions and plant health indicators.

## 📋 Overview

This system implements a comprehensive fuzzy expert system with:

- **9 Input Variables** (environmental and plant factors)
- **10 Disease Outputs** (fungal, bacterial, viral, and parasitic)
- **30 Fuzzy Rules** (derived from scientific research)
- **Triangular Membership Functions** (trimf)
- **Interactive Web Interface** (Gradio)

## 🦠 Diseases Diagnosed

| Disease             | Type      | Pathogen                 |
| ------------------- | --------- | ------------------------ |
| Anthracnose         | Fungal    | _Colletotrichum spp._    |
| Powdery Mildew      | Fungal    | _Leveillula taurica_     |
| Fusarium Wilt       | Fungal    | _Fusarium oxysporum_     |
| Phytophthora        | Oomycete  | _Phytophthora capsici_   |
| Cercospora          | Fungal    | _Cercospora capsici_     |
| Bacterial Leaf Spot | Bacterial | _Xanthomonas campestris_ |
| Bacterial Wilt      | Bacterial | _Ralstonia solanacearum_ |
| Viral Leaf Curl     | Viral     | _Begomovirus_            |
| Mosaic Viruses      | Viral     | _CMV, TMV, PepMoV_       |
| Nematodes           | Parasitic | Root-knot nematodes      |

## 📊 Input Variables

1. **Temperature (Temp)**: 10-40°C
2. **Relative Humidity (RH)**: 10-100%
3. **Rainfall (Rain)**: 0-200mm
4. **Leaf Wetness Duration (LeafWet)**: 0-24 hours
5. **Soil Moisture (SoilM)**: 0-100%
6. **Soil Drainage (Drain)**: 0-10 scale
7. **Seed Health (SeedHealth)**: 0-10 scale
8. **Vector Pressure (Vector)**: 0-10 scale
9. **Crop Stage (Stage)**: 0-3 (Seedling → Vegetative → Flowering → Fruiting)

## 🛠️ Technology Stack

- **Python 3.9+**
- **scikit-fuzzy**: Fuzzy logic inference engine
- **Gradio**: Interactive web interface
- **Matplotlib**: Visualization of membership functions
- **NumPy**: Numerical computations
- **uv**: Fast Python package manager

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- uv package manager

### Install uv (if not already installed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Setup Project

```bash
# Clone or navigate to project directory
cd /path/to/project

# Install dependencies using uv
uv pip install -r requirements.txt
```

## 🎮 Usage

### Run the Application

```bash
python main.py
```

The application will launch a web interface at `http://127.0.0.1:7860`

### Using the Interface

1. **Diagnosis Tab**:

   - Adjust sliders for all 9 input variables
   - Click "🔍 Diagnose Diseases" button
   - View results table with risk scores for all 10 diseases
   - See visual comparison chart
   - Get treatment recommendations for top diagnosis

2. **Membership Functions Tab**:

   - View all input variable membership functions
   - View output risk membership functions
   - See mathematical parameters for all fuzzy sets

3. **Rule Base Tab**:

   - Browse all 30 fuzzy rules
   - Organized by disease type
   - See rule conditions and consequences

4. **About Tab**:
   - System documentation
   - Methodology details
   - References and disclaimers

## 📸 Screenshot Scenarios

### Scenario 1: High Anthracnose Risk

```
Stage = 3.0 (Fruiting)
Temp = 25°C
Rain = 150mm
LeafWet = 20h
Expected: Anthracnose = High Risk
```

### Scenario 2: High Powdery Mildew Risk

```
Temp = 25°C
RH = 30%
LeafWet = 4h
Expected: Powdery Mildew = High Risk
```

### Scenario 3: High Viral Leaf Curl Risk

```
Vector = 9
Stage = 1.0 (Vegetative)
Temp = 35°C
Expected: Viral Leaf Curl = High Risk
```

### Scenario 4: Low Risk (Healthy Conditions)

```
All optimal values
Expected: All diseases = Low Risk
```

## 📁 Project Structure

```
project/
├── main.py                      # Gradio interface and main application
├── fuzzy_system.py              # Fuzzy logic inference implementation
├── disease_knowledge.py         # Disease information and rule base
├── visualizations.py            # Matplotlib visualization functions
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── input-variables.md           # Input variable definitions
├── fuzzy-sets.md                # Membership function parameters
├── rule-base.md                 # Fuzzy rules documentation
├── disease-outputs.md           # Output variable definitions
└── assignment-requirements.md   # Project requirements
```

## 🧮 Fuzzy Logic Implementation

### Membership Functions

All variables use **triangular membership functions (trimf)** for:

- Simplicity and computational efficiency
- Clear interpretation
- Suitability for agricultural data
- Domain expert knowledge alignment

### Inference Method

- **Type**: Mamdani Fuzzy Inference System
- **Aggregation**: Maximum
- **Implication**: Minimum
- **Defuzzification**: Centroid method

### Risk Levels

- **Low Risk**: 0.0 - 0.4 (🟢 Green)
- **Moderate Risk**: 0.4 - 0.6 (⚪ White)
- **High Risk**: 0.6 - 1.0 (🔴 Red)

## 🎨 Color Scheme

The interface uses a custom color palette:

- `#ff4b3e` - Red (High Risk)
- `#81c14b` - Green (Low Risk)
- `#573d1c` - Brown (UI Accents)
- `#454545` - Gunmetal (Dark Gray)
- `#000000` - Black (Moderate Risk)

## 📚 References

Based on scientific research:

- "Major Diseases of Chilli Crop and Their Management"
- International Journal of Biology and Biotechnology (2011)
- Federal Urdu University for Arts, Science & Technology, Pakistan

## 🤝 Contributing

This is an academic project for Knowledge Representation and Reasoning course.

## ⚠️ Disclaimer

This system is designed for **educational and research purposes**. For professional agricultural disease management, always consult qualified agricultural experts and extension services.

## 📝 License

Academic Project - Knowledge Representation and Reasoning Course

## 👨‍💻 Author

Developed as part of KRR Course Project, 5th Semester

---

**🌿 Empowering Agriculture with Fuzzy Logic & AI 🌿**
