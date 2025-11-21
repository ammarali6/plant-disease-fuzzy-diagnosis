# 📸 SCREENSHOT GUIDE FOR REPORT

This guide provides exact input values for capturing screenshots demonstrating different inferencing scenarios.

---

## 🎯 SCENARIO 1: High Anthracnose Risk

**Description:** Fruiting stage with high rainfall and long leaf wetness

### Input Values:

```
Temperature:              25.0 °C
Relative Humidity:        60 %
Rainfall:                 150 mm
Leaf Wetness Duration:    20 hours
Soil Moisture:            50 %
Soil Drainage:            5
Seed Health:              5
Vector Pressure:          3
Crop Stage:               3.0 (Fruiting)
```

### Expected Result:

- **Anthracnose:** HIGH RISK (🔴)
- Shows high risk due to fruiting stage + environmental conditions favorable for fungal growth

### Screenshots to Capture:

1. Diagnosis tab with input sliders set
2. Results table showing Anthracnose at top
3. Comparison chart highlighting Anthracnose
4. Treatment recommendation panel

---

## 🎯 SCENARIO 2: High Powdery Mildew Risk

**Description:** Moderate temperature with low humidity and short leaf wetness

### Input Values:

```
Temperature:              25.0 °C
Relative Humidity:        30 %
Rainfall:                 20 mm
Leaf Wetness Duration:    4 hours
Soil Moisture:            45 %
Soil Drainage:            5
Seed Health:              7
Vector Pressure:          2
Crop Stage:               2.0 (Flowering)
```

### Expected Result:

- **Powdery Mildew:** HIGH RISK (🔴)
- Classic conditions for powdery mildew: moderate temp, low humidity, short wetness

### Screenshots to Capture:

1. Input settings showing low RH
2. Results with Powdery Mildew highlighted
3. Risk comparison chart
4. Treatment recommendation

---

## 🎯 SCENARIO 3: High Viral Leaf Curl Risk

**Description:** High vector pressure during vegetative stage

### Input Values:

```
Temperature:              35.0 °C
Relative Humidity:        50 %
Rainfall:                 30 mm
Leaf Wetness Duration:    10 hours
Soil Moisture:            40 %
Soil Drainage:            6
Seed Health:              5
Vector Pressure:          9
Crop Stage:               1.0 (Vegetative)
```

### Expected Result:

- **Viral Leaf Curl:** HIGH RISK (🔴)
- High vector pressure (whiteflies) with susceptible plant stage

### Screenshots to Capture:

1. Highlight Vector Pressure slider at 9
2. Results showing Viral Leaf Curl at top
3. Comparison chart
4. Treatment focusing on vector control

---

## 🎯 SCENARIO 4: High Phytophthora Risk

**Description:** Waterlogged conditions with poor drainage

### Input Values:

```
Temperature:              25.0 °C
Relative Humidity:        85 %
Rainfall:                 180 mm
Leaf Wetness Duration:    18 hours
Soil Moisture:            80 %
Soil Drainage:            2
Seed Health:              5
Vector Pressure:          3
Crop Stage:               1.5 (Vegetative/Flowering)
```

### Expected Result:

- **Phytophthora:** HIGH RISK (🔴)
- Excessive water + poor drainage creates perfect conditions for water mold

### Screenshots to Capture:

1. Show wet soil conditions (80%) and poor drainage (2)
2. High rainfall (180mm)
3. Phytophthora at top of results
4. Treatment recommendations for drainage

---

## 🎯 SCENARIO 5: Low Risk - Healthy Conditions

**Description:** Optimal conditions across all parameters

### Input Values:

```
Temperature:              24.0 °C
Relative Humidity:        60 %
Rainfall:                 25 mm
Leaf Wetness Duration:    5 hours
Soil Moisture:            45 %
Soil Drainage:            8
Seed Health:              9
Vector Pressure:          0.5
Crop Stage:               1.0 (Vegetative)
```

### Expected Result:

- **All Diseases:** LOW RISK (🟢)
- Demonstrates system correctly identifies healthy conditions

### Screenshots to Capture:

1. All sliders at optimal values
2. Results table with all green (Low Risk)
3. Comparison chart showing low scores across all diseases
4. Healthy status message

---

## 🎯 SCENARIO 6: Multiple Disease Risks

**Description:** Poor overall conditions triggering multiple diseases

### Input Values:

```
Temperature:              30.0 °C
Relative Humidity:        80 %
Rainfall:                 100 mm
Leaf Wetness Duration:    16 hours
Soil Moisture:            70 %
Soil Drainage:            3
Seed Health:              2
Vector Pressure:          6
Crop Stage:               2.5 (Flowering/Fruiting)
```

### Expected Result:

- **Multiple Diseases:** MODERATE to HIGH RISK
- Shows system can identify complex scenarios with multiple risk factors

### Screenshots to Capture:

1. Mixed input conditions
2. Results showing 3-4 diseases at moderate/high risk
3. Comparison chart with multiple elevated bars
4. Demonstrates fuzzy logic handling complex interactions

---

## 📊 ADDITIONAL SCREENSHOTS FOR REPORT

### Membership Function Visualizations

1. **Input Membership Functions:**

   - Click "Show Input Variables" button
   - Capture the 3x3 grid showing all 9 input variables
   - Clear visualization of triangular membership functions

2. **Output Membership Functions:**
   - Click "Show Output Variables" button
   - Capture the risk level plot (Low, Moderate, High)
   - Show overlapping regions between risk levels

### Rule Base Documentation

1. Navigate to "Rule Base" tab
2. Capture scrollable view showing rules organized by disease
3. Show color-coded risk levels
4. Highlight a few example rules with descriptions

### Membership Parameters

1. In "Membership Functions" tab
2. Scroll to parameters section
3. Capture mathematical notation (trimf values)
4. Shows all 9 inputs + output parameters

### About/Documentation

1. Navigate to "About" tab
2. Capture system overview
3. Show methodology section
4. Highlight disease list and technology stack

---

## 🎨 Screenshot Best Practices

### Quality Guidelines:

- Use full browser window (not just tab)
- Ensure all text is readable
- Capture complete sections (don't cut off)
- Use consistent browser zoom level (100%)
- Include browser chrome for context (optional)

### Organization:

1. Create folder: `screenshots/`
2. Name files descriptively:
   - `scenario1_anthracnose_inputs.png`
   - `scenario1_anthracnose_results.png`
   - `scenario1_anthracnose_chart.png`
   - `scenario1_anthracnose_treatment.png`

### For Each Scenario Capture:

1. ✅ Input settings (sliders)
2. ✅ Results table
3. ✅ Comparison chart
4. ✅ Treatment recommendation

---

## 🔄 Quick Reset Between Scenarios

To quickly reset and test another scenario:

1. Simply adjust the sliders to new values
2. Click "Diagnose Diseases" button
3. No need to refresh page
4. System recalculates instantly

---

## ✨ Pro Tips

### Highlight Important Elements:

- Use your OS screenshot tool's annotation features
- Add arrows pointing to key values
- Circle the top diagnosis
- Highlight relevant treatment recommendations

### Capture Sequence:

1. Start with Scenario 5 (healthy) to show baseline
2. Then show disease-specific scenarios (1-4)
3. End with Scenario 6 (multiple risks) to show complexity
4. Follow with technical visualizations

### Report Integration:

- Pair each screenshot with explanatory text
- Reference specific rule numbers that triggered
- Explain fuzzy logic reasoning
- Show how membership values lead to conclusions

---

## 📱 Browser Recommendations

**Best for screenshots:**

- Chrome/Chromium (clean UI)
- Firefox (good rendering)

**Screenshot Tools:**

- Linux: `gnome-screenshot`, `flameshot`
- Built-in: Screenshot tool in browser DevTools
- External: `Shutter`, `Spectacle`

---

## 🎯 Checklist for Report

- [ ] Scenario 1: Anthracnose (4 screenshots)
- [ ] Scenario 2: Powdery Mildew (4 screenshots)
- [ ] Scenario 3: Viral Leaf Curl (4 screenshots)
- [ ] Scenario 4: Phytophthora (4 screenshots)
- [ ] Scenario 5: Healthy Conditions (4 screenshots)
- [ ] Scenario 6: Multiple Risks (4 screenshots)
- [ ] Input Membership Functions (1 screenshot)
- [ ] Output Membership Functions (1 screenshot)
- [ ] Rule Base View (2-3 screenshots)
- [ ] Membership Parameters (1 screenshot)

**Total: ~30 screenshots minimum**

---

**✅ Ready to capture screenshots! Open http://127.0.0.1:7860 and follow the scenarios above.**
