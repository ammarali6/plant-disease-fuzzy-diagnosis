"""
Disease Knowledge Base
Contains fuzzy rules and treatment recommendations for 10 plant diseases.
Based on research paper on chilli crop diseases.
"""

# Disease information and treatments
DISEASES = {
    'Anthracnose': {
        'type': 'Fungal',
        'pathogen': 'Colletotrichum spp.',
        'treatment': 'Apply Mancozeb or Carbendazim fungicide. Remove infected fruits. Improve air circulation.',
    },
    'Powdery Mildew': {
        'type': 'Fungal',
        'pathogen': 'Leveillula taurica',
        'treatment': 'Apply sulfur-based fungicides. Reduce humidity. Ensure proper spacing between plants.',
    },
    'Fusarium Wilt': {
        'type': 'Fungal',
        'pathogen': 'Fusarium oxysporum',
        'treatment': 'Use resistant varieties. Improve soil drainage. Apply Trichoderma-based biocontrol agents.',
    },
    'Phytophthora': {
        'type': 'Oomycete',
        'pathogen': 'Phytophthora capsici',
        'treatment': 'Apply Metalaxyl or Dimethomorph. Improve drainage. Avoid waterlogging. Use raised beds.',
    },
    'Cercospora': {
        'type': 'Fungal',
        'pathogen': 'Cercospora capsici',
        'treatment': 'Spray Mancozeb or Carbendazim. Remove infected leaves. Maintain proper plant nutrition.',
    },
    'Bacterial Leaf Spot': {
        'type': 'Bacterial',
        'pathogen': 'Xanthomonas campestris',
        'treatment': 'Apply copper-based bactericides. Use disease-free seeds. Remove infected plants immediately.',
    },
    'Bacterial Wilt': {
        'type': 'Bacterial',
        'pathogen': 'Ralstonia solanacearum',
        'treatment': 'No cure available. Remove infected plants. Use resistant varieties. Improve drainage.',
    },
    'Viral Leaf Curl': {
        'type': 'Viral',
        'pathogen': 'Begomovirus',
        'treatment': 'Control whitefly vectors with insecticides. Remove infected plants. Use virus-free seedlings.',
    },
    'Mosaic Viruses': {
        'type': 'Viral',
        'pathogen': 'CMV, TMV, PepMoV',
        'treatment': 'Control aphid vectors. Remove infected plants. Use certified virus-free seeds.',
    },
    'Nematodes': {
        'type': 'Parasitic',
        'pathogen': 'Root-knot nematodes',
        'treatment': 'Apply nematicides. Use soil solarization. Rotate with non-host crops. Add organic matter.',
    }
}

# Fuzzy Rule Base (30 Rules)
# Each rule is a tuple: (disease_name, conditions, risk_level)
FUZZY_RULES = [
    # Anthracnose Rules (1-4)
    {
        'id': 1,
        'disease': 'Anthracnose',
        'conditions': {
            'Stage': 'Fruiting',
            'Temp': 'Moderate',
            'Rain': 'High',
            'LeafWet': 'Long'
        },
        'risk': 'High',
        'description': 'High risk during fruiting with moderate temp, high rain, and long leaf wetness'
    },
    {
        'id': 2,
        'disease': 'Anthracnose',
        'conditions': {
            'Stage': 'Fruiting',
            'Temp': 'High',
            'LeafWet': 'Medium'
        },
        'risk': 'Moderate',
        'description': 'Moderate risk during fruiting with high temp and medium leaf wetness'
    },
    {
        'id': 3,
        'disease': 'Anthracnose',
        'conditions': {
            'SeedHealth': 'Poor',
            'Rain': 'High'
        },
        'risk': 'High',
        'description': 'High risk with poor seed health and high rainfall'
    },
    {
        'id': 4,
        'disease': 'Anthracnose',
        'conditions': {
            'Rain': 'Low',
            'LeafWet': 'Short'
        },
        'risk': 'Low',
        'description': 'Low risk with low rain or short leaf wetness'
    },
    
    # Powdery Mildew Rules (5-7)
    {
        'id': 5,
        'disease': 'Powdery Mildew',
        'conditions': {
            'Temp': 'Moderate',
            'RH': 'Low',
            'LeafWet': 'Short'
        },
        'risk': 'High',
        'description': 'High risk with moderate temp, low humidity, and short leaf wetness'
    },
    {
        'id': 6,
        'disease': 'Powdery Mildew',
        'conditions': {
            'Temp': 'High',
            'RH': 'Moderate'
        },
        'risk': 'Moderate',
        'description': 'Moderate risk with high temp and moderate humidity'
    },
    {
        'id': 7,
        'disease': 'Powdery Mildew',
        'conditions': {
            'RH': 'High',
            'LeafWet': 'Long'
        },
        'risk': 'Low',
        'description': 'Low risk with high humidity and long leaf wetness'
    },
    
    # Fusarium Wilt Rules (8-10)
    {
        'id': 8,
        'disease': 'Fusarium Wilt',
        'conditions': {
            'SoilM': 'Wet',
            'Temp': 'High',
            'Drain': 'Poor'
        },
        'risk': 'High',
        'description': 'High risk with wet soil, high temp, and poor drainage'
    },
    {
        'id': 9,
        'disease': 'Fusarium Wilt',
        'conditions': {
            'SoilM': 'Opt',
            'Drain': 'Moderate'
        },
        'risk': 'Moderate',
        'description': 'Moderate risk with optimal soil moisture and moderate drainage'
    },
    {
        'id': 10,
        'disease': 'Fusarium Wilt',
        'conditions': {
            'SeedHealth': 'Good',
            'Drain': 'Good'
        },
        'risk': 'Low',
        'description': 'Low risk with good seed health and good drainage'
    },
    
    # Phytophthora Rules (11-13)
    {
        'id': 11,
        'disease': 'Phytophthora',
        'conditions': {
            'SoilM': 'Wet',
            'Rain': 'High',
            'Drain': 'Poor'
        },
        'risk': 'High',
        'description': 'High risk with wet soil, high rain, and poor drainage'
    },
    {
        'id': 12,
        'disease': 'Phytophthora',
        'conditions': {
            'LeafWet': 'Long',
            'Temp': 'Moderate'
        },
        'risk': 'Moderate',
        'description': 'Moderate risk with long leaf wetness and moderate temp'
    },
    {
        'id': 13,
        'disease': 'Phytophthora',
        'conditions': {
            'Rain': 'None',
            'SoilM': 'Dry'
        },
        'risk': 'Low',
        'description': 'Low risk with no rain and dry soil'
    },
    
    # Cercospora Rules (14-16)
    {
        'id': 14,
        'disease': 'Cercospora',
        'conditions': {
            'RH': 'High',
            'LeafWet': 'Long',
            'SeedHealth': 'Poor'
        },
        'risk': 'High',
        'description': 'High risk with high humidity, long leaf wetness, and poor seed health'
    },
    {
        'id': 15,
        'disease': 'Cercospora',
        'conditions': {
            'Rain': 'High',
            'LeafWet': 'Medium'
        },
        'risk': 'Moderate',
        'description': 'Moderate risk with high rain and medium leaf wetness'
    },
    {
        'id': 16,
        'disease': 'Cercospora',
        'conditions': {
            'SeedHealth': 'Good',
            'LeafWet': 'Short'
        },
        'risk': 'Low',
        'description': 'Low risk with good seed health and short leaf wetness'
    },
    
    # Bacterial Leaf Spot Rules (17-19)
    {
        'id': 17,
        'disease': 'Bacterial Leaf Spot',
        'conditions': {
            'SeedHealth': 'Poor',
            'LeafWet': 'Long',
            'Rain': 'High'
        },
        'risk': 'High',
        'description': 'High risk with poor seed health, long leaf wetness, and high rain'
    },
    {
        'id': 18,
        'disease': 'Bacterial Leaf Spot',
        'conditions': {
            'Temp': 'Moderate',
            'RH': 'High'
        },
        'risk': 'Moderate',
        'description': 'Moderate risk with moderate temp and high humidity'
    },
    {
        'id': 19,
        'disease': 'Bacterial Leaf Spot',
        'conditions': {
            'SeedHealth': 'Good',
            'Rain': 'None'
        },
        'risk': 'Low',
        'description': 'Low risk with good seed health and no rain'
    },
    
    # Bacterial Wilt Rules (20-22)
    {
        'id': 20,
        'disease': 'Bacterial Wilt',
        'conditions': {
            'SoilM': 'Wet',
            'Temp': 'High',
            'Drain': 'Poor'
        },
        'risk': 'High',
        'description': 'High risk with wet soil, high temp, and poor drainage'
    },
    {
        'id': 21,
        'disease': 'Bacterial Wilt',
        'conditions': {
            'SoilM': 'Opt',
            'Drain': 'Moderate'
        },
        'risk': 'Moderate',
        'description': 'Moderate risk with optimal soil moisture and moderate drainage'
    },
    {
        'id': 22,
        'disease': 'Bacterial Wilt',
        'conditions': {
            'SoilM': 'Dry'
        },
        'risk': 'Low',
        'description': 'Low risk with dry soil'
    },
    
    # Viral Leaf Curl Rules (23-25)
    {
        'id': 23,
        'disease': 'Viral Leaf Curl',
        'conditions': {
            'Vector': 'High',
            'Stage': 'Vegetative',
            'Temp': 'High'
        },
        'risk': 'High',
        'description': 'High risk with high vector pressure during vegetative/flowering stage and high temp'
    },
    {
        'id': 24,
        'disease': 'Viral Leaf Curl',
        'conditions': {
            'Vector': 'Moderate',
            'SeedHealth': 'Poor'
        },
        'risk': 'Moderate',
        'description': 'Moderate risk with moderate vector pressure and poor seed health'
    },
    {
        'id': 25,
        'disease': 'Viral Leaf Curl',
        'conditions': {
            'Vector': 'None'
        },
        'risk': 'Low',
        'description': 'Low risk with no vector pressure'
    },
    
    # Mosaic Viruses Rules (26-27)
    {
        'id': 26,
        'disease': 'Mosaic Viruses',
        'conditions': {
            'Vector': 'High',
            'SeedHealth': 'Poor'
        },
        'risk': 'High',
        'description': 'High risk with high vector pressure and poor seed health'
    },
    {
        'id': 27,
        'disease': 'Mosaic Viruses',
        'conditions': {
            'SeedHealth': 'Good',
            'Vector': 'None'
        },
        'risk': 'Low',
        'description': 'Low risk with good seed health and no vectors'
    },
    
    # Nematodes Rules (28-30)
    {
        'id': 28,
        'disease': 'Nematodes',
        'conditions': {
            'Temp': 'High',
            'SoilM': 'Opt',
            'Drain': 'Poor'
        },
        'risk': 'High',
        'description': 'High risk with high temp, optimal soil moisture, and poor drainage'
    },
    {
        'id': 29,
        'disease': 'Nematodes',
        'conditions': {
            'Drain': 'Good',
            'SeedHealth': 'Good'
        },
        'risk': 'Low',
        'description': 'Low risk with good drainage and good seed health'
    },
    {
        'id': 30,
        'disease': 'Nematodes',
        'conditions': {
            'SeedHealth': 'Poor',
            'SoilM': 'Opt'
        },
        'risk': 'Moderate',
        'description': 'Moderate risk with poor seed health and optimal soil moisture'
    }
]


def get_disease_info(disease_name):
    """Get detailed information about a specific disease."""
    return DISEASES.get(disease_name, {})


def get_rules_for_disease(disease_name):
    """Get all fuzzy rules for a specific disease."""
    return [rule for rule in FUZZY_RULES if rule['disease'] == disease_name]


def get_all_diseases():
    """Get list of all disease names."""
    return list(DISEASES.keys())
