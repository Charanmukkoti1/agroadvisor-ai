import streamlit as st

# ================= AI INFERENCE ENGINE =================
def agro_advisor_engine(facts):
    output = []

    soil = facts["soil"]
    rainfall = facts["rainfall"]
    temperature = facts["temperature"]
    humidity = facts["humidity"]
    soil_pH = facts["soil_pH"]
    soil_moisture = facts["soil_moisture"]
    crop = facts["crop"]
    season = facts["season"]

    # --------- 1. CROP PLANNING AI ----------
    if soil == "Loamy" and rainfall >= 150 and 20 <= temperature <= 30:
        output.append("🌾 Crop Planning: Rice is suitable")
    if soil == "Black" and rainfall >= 100:
        output.append("🌿 Crop Planning: Cotton is suitable")
    if soil == "Sandy" and rainfall < 75:
        output.append("🌾 Crop Planning: Millet is suitable")
    if rainfall < 50:
        output.append("🌵 Crop Planning: Use drought-resistant crops")

    # --------- 2. WEATHER / CLIMATE AWARENESS ----------
    if rainfall < 50:
        output.append("⚠️ Climate Alert: Drought risk – irrigation required")
    if rainfall > 200:
        output.append("⚠️ Climate Alert: Flood risk – ensure drainage")
    if temperature > 38:
        output.append("🔥 Climate Alert: Heat stress – avoid midday farming")
    if humidity > 80:
        output.append("🐛 Climate Alert: High pest & disease risk")

    # --------- 3. MARKET PRICE TREND (RULE-BASED) ----------
    if crop == "Rice" and season == "Harvest":
        output.append("📈 Market Insight: Rice prices usually drop at harvest – consider storage")
    if crop == "Onion" and rainfall < 60:
        output.append("📈 Market Insight: Onion prices may increase – delay selling")
    if crop == "Cotton" and season == "Off-season":
        output.append("📈 Market Insight: Cotton prices tend to rise – good selling time")

    # --------- 4. RESOURCE OPTIMIZATION ----------
    if crop in ["Rice", "Sugarcane"]:
        output.append("💧 Resource Advice: High water requirement")
    if crop in ["Millet", "Groundnut"]:
        output.append("💧 Resource Advice: Low water requirement")

    if soil_moisture == "Low":
        output.append("🚰 Resource Action: Start irrigation immediately")
    if rainfall > 150:
        output.append("🚰 Resource Action: Reduce irrigation")

    if soil_pH < 5.5:
        output.append("🧪 Soil Advice: Apply lime to reduce acidity")
    if soil_pH > 8:
        output.append("🧪 Soil Advice: Apply gypsum to reduce alkalinity")

    return output


# =========
