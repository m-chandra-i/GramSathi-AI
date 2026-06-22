import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="GramSathi Crop Guide",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)


RAJASTHAN_CROPS = [
        {
        "crop": "Safflower",
        "hindi": "कुसुम",
        "type": "Oilseed",
        "season": "Rabi",
        "zones": ["Hadoti", "Mewar", "Semi-arid Central"],
        "districts": "Kota, Bundi, Baran, Bhilwara, Chittorgarh, Ajmer",
        "soil": "Well-drained loam to clay loam",
        "water_need": "Low",
        "drought_fit": "Good",
        "duration_days": 125,
        "sowing": "October to November",
        "harvest": "February to March",
        "rainfall_mm": "300-500",
        "temperature_c": "15-30",
        "seed_rate_kg_ha": 12.0,
        "spacing": "45 x 20 cm",
        "irrigation": "Usually rainfed; one irrigation at flowering improves yield",
        "common_issues": "Aphid, wilt, alternaria leaf spot",
        "best_practices": "Use treated seed, avoid waterlogging, keep proper spacing, and monitor aphid during flowering.",
        "market_use": "Edible oil, oilcake, bird feed, dryland oilseed crop",
    },
    {
        "crop": "Beetroot",
        "hindi": "चुकंदर",
        "type": "Vegetable",
        "season": "Rabi / Winter",
        "zones": ["Eastern Plains", "Hadoti", "Irrigated Canal"],
        "districts": "Jaipur, Alwar, Bharatpur, Kota, Bundi, Sri Ganganagar",
        "soil": "Loose sandy loam to loam, deep and well-drained soil",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 75,
        "sowing": "October to December",
        "harvest": "60-80 days after sowing",
        "rainfall_mm": "Irrigated winter crop",
        "temperature_c": "15-25",
        "seed_rate_kg_ha": 8.0,
        "spacing": "30 x 10 cm",
        "irrigation": "Light irrigation at regular intervals; avoid moisture stress during root development",
        "common_issues": "Leaf spot, root cracking, damping off",
        "best_practices": "Prepare fine seedbed, thin plants after germination, keep uniform moisture, and harvest tender roots.",
        "market_use": "Fresh vegetable, salad, juice, processing",
    },
    {
        "crop": "Ridge Gourd",
        "hindi": "तोरई",
        "type": "Vegetable",
        "season": "Kharif / Summer",
        "zones": ["Eastern Plains", "Semi-arid Central", "Mewar", "Hadoti"],
        "districts": "Jaipur, Alwar, Tonk, Ajmer, Udaipur, Kota",
        "soil": "Sandy loam to loam, rich in organic matter",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 70,
        "sowing": "February to March or June to July",
        "harvest": "50-70 days after sowing",
        "rainfall_mm": "400-700 or irrigation supported",
        "temperature_c": "24-32",
        "seed_rate_kg_ha": 5.0,
        "spacing": "2.0 x 1.0 m",
        "irrigation": "Regular light irrigation; drip irrigation is useful",
        "common_issues": "Fruit fly, red pumpkin beetle, powdery mildew, downy mildew",
        "best_practices": "Use raised beds, provide support or trellis, pick tender fruits regularly, and remove diseased vines.",
        "market_use": "Fresh vegetable, local market",
    },
    {
        "crop": "Bitter Gourd",
        "hindi": "करेला",
        "type": "Vegetable",
        "season": "Kharif / Summer",
        "zones": ["Eastern Plains", "Semi-arid Central", "Mewar", "Hadoti"],
        "districts": "Jaipur, Alwar, Ajmer, Tonk, Udaipur, Kota, Bundi",
        "soil": "Well-drained sandy loam with good organic matter",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 85,
        "sowing": "February to March for summer; June to July for kharif",
        "harvest": "55-85 days after sowing",
        "rainfall_mm": "400-700 or irrigation supported",
        "temperature_c": "24-32",
        "seed_rate_kg_ha": 5.0,
        "spacing": "2.0 x 1.0 m",
        "irrigation": "Frequent light irrigation; avoid waterlogging around root zone",
        "common_issues": "Fruit fly, powdery mildew, downy mildew, mosaic virus",
        "best_practices": "Use trellis support, collect and destroy infested fruits, maintain drainage, and harvest fruits at tender stage.",
        "market_use": "Fresh vegetable, medicinal value, local market",
    },
    {
        "crop": "Amaranthus",
        "hindi": "चौलाई",
        "type": "Leafy Vegetable",
        "season": "Kharif / Summer",
        "zones": ["Eastern Plains", "Semi-arid Central", "Mewar", "Hadoti"],
        "districts": "Jaipur, Alwar, Ajmer, Tonk, Udaipur, Kota, Bhilwara",
        "soil": "Fertile loam to sandy loam with good drainage",
        "water_need": "Low",
        "drought_fit": "Good",
        "duration_days": 35,
        "sowing": "March to September depending on local temperature",
        "harvest": "25-35 days after sowing; multiple cuttings possible",
        "rainfall_mm": "300-600 or light irrigation",
        "temperature_c": "25-35",
        "seed_rate_kg_ha": 2.5,
        "spacing": "20-25 cm rows",
        "irrigation": "Light irrigation after sowing and after each cutting",
        "common_issues": "Leaf spot, aphid, flea beetle",
        "best_practices": "Use clean seed, harvest tender leaves, avoid dirty irrigation water, and apply light nitrogen after cutting.",
        "market_use": "Leafy vegetable, household nutrition, local market",
    },
    {
        "crop": "Bajra",
        "hindi": "बाजरा",
        "type": "Cereal",
        "season": "Kharif",
        "zones": ["Arid West", "Shekhawati", "Semi-arid Central"],
        "districts": "Barmer, Jodhpur, Nagaur, Churu, Jhunjhunu, Sikar, Jaisalmer",
        "soil": "Sandy loam, light soil",
        "water_need": "Low",
        "drought_fit": "Excellent",
        "duration_days": 85,
        "sowing": "June to July, after first good monsoon rain",
        "harvest": "September to October",
        "rainfall_mm": "250-500",
        "temperature_c": "25-35",
        "seed_rate_kg_ha": 4.0,
        "spacing": "45 cm row spacing",
        "irrigation": "Mostly rainfed; one life-saving irrigation helps in dry spell",
        "common_issues": "Shoot fly, downy mildew, moisture stress",
        "best_practices": "Use timely sowing, seed treatment, wider spacing, and conserve soil moisture with interculture.",
        "market_use": "Grain, flour, fodder, poultry feed",
    },
        {
        "crop": "Bottle Gourd",
        "hindi": "लौकी",
        "type": "Vegetable",
        "season": "Kharif / Summer",
        "zones": ["Eastern Plains", "Semi-arid Central", "Mewar", "Hadoti"],
        "districts": "Jaipur, Alwar, Tonk, Ajmer, Udaipur, Kota, Bundi",
        "soil": "Well-drained sandy loam to loam with organic matter",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 75,
        "sowing": "February to March for summer; June to July for kharif",
        "harvest": "50-75 days after sowing",
        "rainfall_mm": "400-700 or irrigation supported",
        "temperature_c": "24-32",
        "seed_rate_kg_ha": 4.0,
        "spacing": "2.0 x 1.0 m",
        "irrigation": "Regular light irrigation; avoid waterlogging near roots",
        "common_issues": "Fruit fly, powdery mildew, downy mildew, red pumpkin beetle",
        "best_practices": "Use raised beds, provide support if possible, harvest tender fruits regularly, and keep vines disease-free.",
        "market_use": "Fresh vegetable, local market, household use",
    },
    {
        "crop": "Cucumber",
        "hindi": "खीरा",
        "type": "Vegetable",
        "season": "Summer / Kharif",
        "zones": ["Eastern Plains", "Irrigated Canal", "Semi-arid Central", "Hadoti"],
        "districts": "Jaipur, Alwar, Bharatpur, Sri Ganganagar, Hanumangarh, Kota",
        "soil": "Sandy loam, fertile and well-drained soil",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 60,
        "sowing": "February to March or June to July",
        "harvest": "40-60 days after sowing",
        "rainfall_mm": "Irrigated crop or 400-600 rainfall",
        "temperature_c": "22-32",
        "seed_rate_kg_ha": 3.0,
        "spacing": "1.5 x 0.6 m",
        "irrigation": "Frequent light irrigation; drip irrigation is useful",
        "common_issues": "Fruit fly, downy mildew, powdery mildew, mosaic virus",
        "best_practices": "Use healthy seed, mulch the field, avoid overhead irrigation, and pick fruits at tender stage.",
        "market_use": "Fresh salad, local vegetable market",
    },
    {
        "crop": "Radish",
        "hindi": "मूली",
        "type": "Vegetable",
        "season": "Rabi",
        "zones": ["Eastern Plains", "Semi-arid Central", "Irrigated Canal", "Hadoti"],
        "districts": "Jaipur, Alwar, Bharatpur, Sikar, Sri Ganganagar, Kota",
        "soil": "Loose sandy loam, deep and stone-free soil",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 45,
        "sowing": "September to December",
        "harvest": "30-50 days after sowing",
        "rainfall_mm": "Irrigated winter crop",
        "temperature_c": "10-25",
        "seed_rate_kg_ha": 10.0,
        "spacing": "30 x 8 cm",
        "irrigation": "Light irrigation at short intervals for tender roots",
        "common_issues": "Root splitting, aphid, leaf spot, root maggot",
        "best_practices": "Prepare fine seedbed, keep moisture uniform, thin plants on time, and harvest before roots become hard.",
        "market_use": "Fresh root, leaves, salad, local market",
    },
    {
        "crop": "Spinach",
        "hindi": "पालक",
        "type": "Leafy Vegetable",
        "season": "Rabi / Winter",
        "zones": ["Eastern Plains", "Hadoti", "Mewar", "Irrigated Canal"],
        "districts": "Jaipur, Alwar, Kota, Bundi, Udaipur, Sri Ganganagar",
        "soil": "Fertile loam with good moisture holding capacity",
        "water_need": "Medium",
        "drought_fit": "Low",
        "duration_days": 40,
        "sowing": "September to February",
        "harvest": "25-40 days after sowing; multiple cuttings possible",
        "rainfall_mm": "Irrigated leafy vegetable crop",
        "temperature_c": "15-25",
        "seed_rate_kg_ha": 25.0,
        "spacing": "20-25 cm rows",
        "irrigation": "Frequent light irrigation after each cutting",
        "common_issues": "Leaf spot, downy mildew, aphid",
        "best_practices": "Use clean seed, avoid dirty irrigation water, harvest tender leaves, and maintain nitrogen carefully.",
        "market_use": "Fresh leafy vegetable, local market, household nutrition",
    },
    {
        "crop": "Cowpea",
        "hindi": "लोबिया",
        "type": "Pulse / Vegetable / Fodder",
        "season": "Kharif / Summer",
        "zones": ["Arid West", "Semi-arid Central", "Eastern Plains", "Mewar"],
        "districts": "Jodhpur, Nagaur, Jaipur, Ajmer, Alwar, Udaipur, Pali",
        "soil": "Sandy loam to loam, well-drained soil",
        "water_need": "Low",
        "drought_fit": "Good",
        "duration_days": 70,
        "sowing": "March to April for summer; June to July for kharif",
        "harvest": "Green pods in 45-60 days; grain in 70-90 days",
        "rainfall_mm": "300-600",
        "temperature_c": "25-35",
        "seed_rate_kg_ha": 20.0,
        "spacing": "45 x 15 cm",
        "irrigation": "Light irrigation if dry spell occurs; avoid waterlogging",
        "common_issues": "Aphid, pod borer, yellow mosaic virus, leaf spot",
        "best_practices": "Use treated seed, support vegetable types if needed, pick pods regularly, and rotate with cereals.",
        "market_use": "Green pods, dry pulse, fodder, soil fertility improvement",
    },
        {
        "crop": "Sunflower",
        "hindi": "सूरजमुखी",
        "type": "Oilseed",
        "season": "Rabi / Spring",
        "zones": ["Irrigated Canal", "Eastern Plains", "Hadoti", "Semi-arid Central"],
        "districts": "Sri Ganganagar, Hanumangarh, Jaipur, Alwar, Kota, Bundi, Tonk",
        "soil": "Well-drained loam to sandy loam",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 95,
        "sowing": "January to February for spring crop; June to July for kharif crop",
        "harvest": "April to May for spring crop; September to October for kharif crop",
        "rainfall_mm": "500-700 or irrigation supported",
        "temperature_c": "20-30",
        "seed_rate_kg_ha": 8.0,
        "spacing": "60 x 30 cm",
        "irrigation": "Irrigate at bud formation, flowering, and seed filling stages; avoid waterlogging",
        "common_issues": "Capitulum borer, leaf spot, downy mildew, bird damage",
        "best_practices": "Use treated seed, maintain proper spacing, support pollination, protect mature heads from birds, and harvest when back of head turns yellow-brown.",
        "market_use": "Edible oil, bird feed, oilcake, ornamental value",
    },
    {
        "crop": "Wheat",
        "hindi": "गेहूं",
        "type": "Cereal",
        "season": "Rabi",
        "zones": ["Irrigated Canal", "Eastern Plains", "Hadoti"],
        "districts": "Sri Ganganagar, Hanumangarh, Kota, Bundi, Bharatpur, Alwar, Jaipur",
        "soil": "Loam, clay loam, fertile alluvial soil",
        "water_need": "High",
        "drought_fit": "Low",
        "duration_days": 125,
        "sowing": "November to early December",
        "harvest": "March to April",
        "rainfall_mm": "350-650 with irrigation",
        "temperature_c": "15-25",
        "seed_rate_kg_ha": 100.0,
        "spacing": "20-22 cm row spacing",
        "irrigation": "4-6 irrigations; crown root stage is critical",
        "common_issues": "Rust, termite, aphid, lodging",
        "best_practices": "Sow on time, keep first irrigation at crown root stage, avoid excess nitrogen, monitor rust.",
        "market_use": "Flour, household grain, straw",
    },
    {
        "crop": "Mustard",
        "hindi": "सरसों",
        "type": "Oilseed",
        "season": "Rabi",
        "zones": ["Shekhawati", "Semi-arid Central", "Eastern Plains", "Hadoti", "Irrigated Canal"],
        "districts": "Churu, Jhunjhunu, Sikar, Jaipur, Ajmer, Nagaur, Kota, Bundi, Sri Ganganagar",
        "soil": "Well-drained loam to clay loam",
        "water_need": "Low",
        "drought_fit": "Excellent",
        "duration_days": 110,
        "sowing": "October to November",
        "harvest": "February to March",
        "rainfall_mm": "300-500",
        "temperature_c": "15-25",
        "seed_rate_kg_ha": 5.0,
        "spacing": "45 x 20 cm",
        "irrigation": "Usually rainfed; one irrigation at siliqua formation improves yield",
        "common_issues": "Sawfly, aphid, alternaria leaf spot",
        "best_practices": "Use quality seed, timely sowing, avoid waterlogging, and monitor pests during pod formation.",
        "market_use": "Oil, oilcake, dal quality, poultry feed, dryland oilseed crop",
    },
    {
        "crop": "Gram",
        "hindi": "चना",
        "type": "Pulse",
        "season": "Rabi",
        "zones": ["Shekhawati", "Semi-arid Central", "Eastern Plains", "Hadoti"],
        "districts": "Churu, Jhunjhunu, Sikar, Jaipur, Ajmer, Nagaur, Kota, Bhilwara",
        "soil": "Well-drained loam to clay loam",
        "water_need": "Low",
        "drought_fit": "Good",
        "duration_days": 120,
        "sowing": "October to November",
        "harvest": "February to March",
        "rainfall_mm": "250-500",
        "temperature_c": "10-30",
        "seed_rate_kg_ha": 80.0,
        "spacing": "45 x 20 cm",
        "irrigation": "Usually rainfed; one irrigation helps in dry spell",
        "common_issues": "Pod borer, wilt, rust",
        "best_practices": "Use treated seed, timely sowing, avoid excess nitrogen, and pick mature pods on time.",
        "market_use": "Split dal, whole pulse, household grain, protein source",
    },
    {
        "crop": "Arhar (Pigeon Pea)",
        "hindi": "अरहर",
        "type": "Pulse",
        "season": "Kharif",
        "zones": ["Eastern Plains", "Mewar", "Hadoti", "Tribal South"],
        "districts": "Jaipur, Ajmer, Udaipur, Kota, Bundi, Banswara, Dungarpur",
        "soil": "Well-drained loam to clay loam soil",
        "water_need": "Medium",
        "drought_fit": "Good",
        "duration_days": 210,
        "sowing": "June to July with monsoon",
        "harvest": "December to January or January to February",
        "rainfall_mm": "600-900",
        "temperature_c": "20-35",
        "seed_rate_kg_ha": 15.0,
        "spacing": "60 x 30 cm",
        "irrigation": "Supplementary irrigation during dry spell",
        "common_issues": "Fusarium wilt, Phytophthora blight, pod borer, thrips",
        "best_practices": "Use disease-free seed, wider spacing, avoid waterlogging, and remove infested plants early.",
        "market_use": "Split dal, whole pulse, fodder for livestock",
    },
    {
        "crop": "Lentil",
        "hindi": "मसूर",
        "type": "Pulse",
        "season": "Rabi",
        "zones": ["Eastern Plains", "Semi-arid Central", "Irrigated Canal"],
        "districts": "Alwar, Bharatpur, Jaipur, Sri Ganganagar, Hanumangarh",
        "soil": "Well-drained sandy loam to loam",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 100,
        "sowing": "November to December",
        "harvest": "February to March",
        "rainfall_mm": "Irrigated crop or 300-500 mm",
        "temperature_c": "15-25",
        "seed_rate_kg_ha": 40.0,
        "spacing": "30 x 10 cm",
        "irrigation": "2-3 light irrigations; avoid excess water",
        "common_issues": "Anthracnose, fusarium wilt, rust",
        "best_practices": "Use healthy seed, avoid waterlogging, thin plants early, and harvest on time.",
        "market_use": "Whole lentil, split dal, processed pulses, export market",
    },
    {
        "crop": "Maize",
        "hindi": "मक्का",
        "type": "Cereal",
        "season": "Kharif / Summer",
        "zones": ["Eastern Plains", "Semi-arid Central", "Mewar", "Hadoti"],
        "districts": "Jaipur, Alwar, Tonk, Ajmer, Udaipur, Kota, Bhilwara",
        "soil": "Fertile loam to clay loam, good drainage",
        "water_need": "High",
        "drought_fit": "Low",
        "duration_days": 100,
        "sowing": "March to April for summer; June to July for kharif",
        "harvest": "July to August for summer; September to October for kharif",
        "rainfall_mm": "500-1000",
        "temperature_c": "20-30",
        "seed_rate_kg_ha": 20.0,
        "spacing": "60 x 20 cm",
        "irrigation": "5-6 irrigations; critical at silking and milk stage",
        "common_issues": "Shoot fly, stem borer, leaf spot, cob rot",
        "best_practices": "Use quality hybrid seed, proper spacing, timely irrigation, and remove affected cobs.",
        "market_use": "Grain, fodder, corn meal, processed foods, animal feed",
    },
    {
        "crop": "Coriander",
        "hindi": "धनिया",
        "type": "Spice",
        "season": "Rabi",
        "zones": ["Hadoti", "Semi-arid Central", "Eastern Plains"],
        "districts": "Kota, Bundi, Bhilwara, Jaipur, Ajmer",
        "soil": "Well-drained loam to sandy loam",
        "water_need": "Low",
        "drought_fit": "Good",
        "duration_days": 120,
        "sowing": "October to November",
        "harvest": "February to March when plants turn brown",
        "rainfall_mm": "300-500",
        "temperature_c": "15-25",
        "seed_rate_kg_ha": 12.0,
        "spacing": "45 x 20 cm",
        "irrigation": "2-3 light irrigations; avoid excess moisture",
        "common_issues": "Aphid, powdery mildew, stem gall, leaf spot",
        "best_practices": "Use quality seed, timely sowing, thin plants early, and thresh at right maturity.",
        "market_use": "Whole seeds, ground powder, spice market, condiment",
    },
    {
        "crop": "Garlic",
        "hindi": "लहसुन",
        "type": "Vegetable",
        "season": "Rabi",
        "zones": ["Hadoti", "Eastern Plains", "Semi-arid Central"],
        "districts": "Kota, Bundi, Jaipur, Alwar, Bharatpur",
        "soil": "Well-drained loam to clay loam rich in organic matter",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 150,
        "sowing": "October to November; plant cloves directly",
        "harvest": "May to June when tops dry",
        "rainfall_mm": "Irrigated winter crop",
        "temperature_c": "15-25",
        "seed_rate_kg_ha": 2000.0,
        "spacing": "30 x 10 cm",
        "irrigation": "5-6 light irrigations throughout season",
        "common_issues": "Basal rot, leaf spot, mites, nematode",
        "best_practices": "Use healthy cloves, treat seed, maintain drainage, and harvest at full maturity.",
        "market_use": "Fresh bulbs, dried garlic, powder, processed foods, health market",
    },
    {
        "crop": "Soybean",
        "hindi": "सोयाबीन",
        "type": "Pulse / Oilseed",
        "season": "Kharif",
        "zones": ["Semi-arid Central", "Hadoti", "Mewar", "Eastern Plains"],
        "districts": "Jaipur, Ajmer, Tonk, Kota, Bundi, Bhilwara, Udaipur",
        "soil": "Well-drained loam to clay loam",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 100,
        "sowing": "June to July with first monsoon rain",
        "harvest": "September to October",
        "rainfall_mm": "600-800",
        "temperature_c": "20-35",
        "seed_rate_kg_ha": 75.0,
        "spacing": "45 x 20 cm",
        "irrigation": "Supplementary irrigation if dry spell occurs",
        "common_issues": "Stem fly, leaf folder, powdery mildew, rot diseases",
        "best_practices": "Use treated quality seed, wider spacing, avoid waterlogging, and rotate crops.",
        "market_use": "Grains, oil, processed foods, animal feed, protein source",
    },
    {
        "crop": "Barley",
        "hindi": "जौ",
        "type": "Cereal",
        "season": "Rabi",
        "zones": ["Shekhawati", "Semi-arid Central", "Eastern Plains"],
        "districts": "Churu, Jhunjhunu, Sikar, Jaipur, Ajmer, Nagaur",
        "soil": "Loam to clay loam, well-drained soil",
        "water_need": "Low",
        "drought_fit": "Excellent",
        "duration_days": 110,
        "sowing": "November to December",
        "harvest": "March to April",
        "rainfall_mm": "250-500",
        "temperature_c": "15-25",
        "seed_rate_kg_ha": 100.0,
        "spacing": "20-22 cm rows",
        "irrigation": "1-2 irrigations; avoid waterlogging",
        "common_issues": "Rust, smut, aphid",
        "best_practices": "Use quality seed, timely sowing, avoid excess nitrogen, and monitor for pest.",
        "market_use": "Grain, flour, animal feed, malting barley, beer industry",
    },
    {
        "crop": "Rapeseed",
        "hindi": "तोरिया",
        "type": "Oilseed",
        "season": "Rabi",
        "zones": ["Eastern Plains", "Irrigated Canal"],
        "districts": "Jaipur, Alwar, Bharatpur, Sri Ganganagar, Hanumangarh",
        "soil": "Well-drained loam to clay loam",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 100,
        "sowing": "October to November",
        "harvest": "February to March",
        "rainfall_mm": "300-600",
        "temperature_c": "15-25",
        "seed_rate_kg_ha": 7.0,
        "spacing": "45 x 20 cm",
        "irrigation": "2-3 irrigations; critical at flowering",
        "common_issues": "Sawfly, aphid, alternaria leaf spot",
        "best_practices": "Use quality seed, timely sowing, manage pests, and harvest at maturity.",
        "market_use": "Oil, oilcake, meal, condiment",
    },
    {
        "crop": "Guar",
        "hindi": "ग्वार",
        "type": "Pulse / Vegetable",
        "season": "Summer",
        "zones": ["Arid West", "Shekhawati", "Semi-arid Central"],
        "districts": "Barmer, Jodhpur, Nagaur, Churu, Jhunjhunu, Sikar",
        "soil": "Sandy loam, well-drained light soil",
        "water_need": "Low",
        "drought_fit": "Excellent",
        "duration_days": 90,
        "sowing": "February to March",
        "harvest": "May to June for vegetables; June to July for pods",
        "rainfall_mm": "250-500",
        "temperature_c": "25-40",
        "seed_rate_kg_ha": 20.0,
        "spacing": "45 x 15 cm",
        "irrigation": "Light irrigation if needed; mostly rainfed",
        "common_issues": "Aphid, jassid, powdery mildew",
        "best_practices": "Use quality seed, proper spacing, monitor pests, and harvest on time.",
        "market_use": "Guar gum, vegetable pods, animal fodder, industrial gum",
    },
    {
        "crop": "Cumin",
        "hindi": "जीरा",
        "type": "Spice",
        "season": "Rabi",
        "zones": ["Arid West", "Shekhawati", "Semi-arid Central"],
        "districts": "Barmer, Jodhpur, Nagaur, Churu, Jhunjhunu",
        "soil": "Well-drained light loam, sandy loam",
        "water_need": "Low",
        "drought_fit": "Excellent",
        "duration_days": 120,
        "sowing": "October to November",
        "harvest": "February to March when umbels turn brown",
        "rainfall_mm": "300-500",
        "temperature_c": "20-30",
        "seed_rate_kg_ha": 5.0,
        "spacing": "45 x 20 cm",
        "irrigation": "2-3 light irrigations",
        "common_issues": "Aphid, powdery mildew, wilt",
        "best_practices": "Use quality seed, thin plants early, manage diseases, and thresh at maturity.",
        "market_use": "Seeds, spice powder, condiment, export market",
    },
    {
        "crop": "Isabgol",
        "hindi": "इसबगोल",
        "type": "Medicinal",
        "season": "Rabi",
        "zones": ["Arid West", "Shekhawati"],
        "districts": "Barmer, Jodhpur, Jaisalmer, Churu, Jhunjhunu",
        "soil": "Well-drained light loam, sandy soil",
        "water_need": "Low",
        "drought_fit": "Excellent",
        "duration_days": 130,
        "sowing": "October to November",
        "harvest": "February to March; collect seeds when pods dry",
        "rainfall_mm": "250-400",
        "temperature_c": "20-30",
        "seed_rate_kg_ha": 5.0,
        "spacing": "30 x 15 cm",
        "irrigation": "1-2 light irrigations if needed",
        "common_issues": "Aphid, powdery mildew, disease-free",
        "best_practices": "Use quality seed, timely sowing, thin plants, and harvest when dry.",
        "market_use": "Seeds, husk, medicinal value, pharmaceutical use, export market",
    },
    {
        "crop": "Taramira",
        "hindi": "तारामीरा",
        "type": "Oilseed",
        "season": "Rabi",
        "zones": ["Arid West", "Shekhawati", "Semi-arid Central"],
        "districts": "Barmer, Jodhpur, Jaisalmer, Churu, Jhunjhunu, Nagaur",
        "soil": "Sandy loam, well-drained light soil",
        "water_need": "Low",
        "drought_fit": "Excellent",
        "duration_days": 120,
        "sowing": "October to November",
        "harvest": "February to March",
        "rainfall_mm": "300-500",
        "temperature_c": "15-25",
        "seed_rate_kg_ha": 5.0,
        "spacing": "45 x 20 cm",
        "irrigation": "Usually rainfed; one irrigation helps",
        "common_issues": "Aphid, powdery mildew, stem gall",
        "best_practices": "Use quality seed, timely sowing, manage pests, and harvest at maturity.",
        "market_use": "Oil, oilcake, feed, dryland crop",
    },
    {
        "crop": "Moth",
        "hindi": "मोठ",
        "type": "Pulse",
        "season": "Kharif / Summer",
        "zones": ["Arid West", "Shekhawati", "Semi-arid Central"],
        "districts": "Barmer, Jodhpur, Nagaur, Churu, Jhunjhunu, Sikar",
        "soil": "Sandy loam, light well-drained soil",
        "water_need": "Low",
        "drought_fit": "Excellent",
        "duration_days": 90,
        "sowing": "March to April for summer; June to July for kharif",
        "harvest": "June to July for summer; September to October for kharif",
        "rainfall_mm": "250-500",
        "temperature_c": "25-35",
        "seed_rate_kg_ha": 15.0,
        "spacing": "30 x 10 cm",
        "irrigation": "Light irrigation if dry spell; mostly rainfed",
        "common_issues": "Pod borer, aphid, yellow mosaic virus",
        "best_practices": "Use quality seed, manage pests, wider spacing, and harvest on time.",
        "market_use": "Split dal, whole pulse, animal feed, sprouts, dryland pulse",
    },
    {
        "crop": "Sesame",
        "hindi": "तिल",
        "type": "Oilseed",
        "season": "Kharif",
        "zones": ["Eastern Plains", "Semi-arid Central", "Hadoti"],
        "districts": "Jaipur, Ajmer, Alwar, Kota, Bhilwara",
        "soil": "Well-drained loam to sandy loam",
        "water_need": "Medium",
        "drought_fit": "Good",
        "duration_days": 100,
        "sowing": "June to July with monsoon",
        "harvest": "September to October",
        "rainfall_mm": "600-800",
        "temperature_c": "25-35",
        "seed_rate_kg_ha": 5.0,
        "spacing": "45 x 20 cm",
        "irrigation": "Supplementary irrigation during dry spell",
        "common_issues": "Aphid, leaf spot, wilt, phyllody",
        "best_practices": "Use quality seed, manage pests, timely thinning, and harvest at maturity.",
        "market_use": "Oil, seeds, oilcake, tahini, traditional sweet, export market",
    },
    {
        "crop": "Cotton",
        "hindi": "कपास",
        "type": "Cash Crop / Fiber",
        "season": "Kharif",
        "zones": ["Irrigated Canal", "Eastern Plains", "Semi-arid Central"],
        "districts": "Sri Ganganagar, Hanumangarh, Jaipur, Alwar, Bhilwara",
        "soil": "Well-drained loam to clay loam soil",
        "water_need": "High",
        "drought_fit": "Low",
        "duration_days": 180,
        "sowing": "April to May before monsoon",
        "harvest": "September to December",
        "rainfall_mm": "600-1000 or assured irrigation",
        "temperature_c": "20-35",
        "seed_rate_kg_ha": 20.0,
        "spacing": "90 x 60 cm",
        "irrigation": "8-10 irrigations; critical at flowering and boll development",
        "common_issues": "Boll worm, leaf hopper, spider mite, Fusarium wilt",
        "best_practices": "Use quality hybrid seed, proper spacing, IPM for pests, and harvest at maturity.",
        "market_use": "Raw cotton, textile fiber, oil, oilcake, lint market",
    },
    {
        "crop": "Sugarcane",
        "hindi": "गन्ना",
        "type": "Cash Crop",
        "season": "Kharif / Perennial",
        "zones": ["Irrigated Canal", "Eastern Plains"],
        "districts": "Sri Ganganagar, Hanumangarh, Bharatpur, Alwar",
        "soil": "Deep fertile loam to alluvial soil",
        "water_need": "High",
        "drought_fit": "Low",
        "duration_days": 365,
        "sowing": "September to November for autumn crop; February to March for spring",
        "harvest": "10-12 months after planting",
        "rainfall_mm": "1000-1500 or assured irrigation",
        "temperature_c": "20-30",
        "seed_rate_kg_ha": 25000.0,
        "spacing": "90 cm rows",
        "irrigation": "8-10 heavy irrigations; avoid waterlogging",
        "common_issues": "Shoot borer, red rot, wilt disease, smut",
        "best_practices": "Use disease-free seed cane, proper spacing, manage water, and intercrop.",
        "market_use": "Sugar, gur, juice, alcohol, animal feed, organic sugar",
    },
    {
        "crop": "Mango",
        "hindi": "आम",
        "type": "Fruit",
        "season": "Perennial",
        "zones": ["Tribal South", "Mewar", "Hadoti"],
        "districts": "Banswara, Dungarpur, Udaipur, Kota, Bundi, Jhalawar",
        "soil": "Deep well-drained loam to alluvial soil",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 1460,
        "sowing": "Planting July to September",
        "harvest": "May to July after bearing starts",
        "rainfall_mm": "750-1200 or irrigation supported",
        "temperature_c": "20-38",
        "seed_rate_kg_ha": 0.0,
        "spacing": "10 x 10 m",
        "irrigation": "Protective irrigation in young orchards; avoid irrigation before flowering",
        "common_issues": "Mango hopper, powdery mildew, fruit fly, anthracnose",
        "best_practices": "Use grafted plants, train young trees, keep orchard sanitation, and protect flowering from pests.",
        "market_use": "Fresh fruit, pickle, pulp, processing",
    },
    {
        "crop": "Date Palm",
        "hindi": "खजूर",
        "type": "Fruit",
        "season": "Perennial",
        "zones": ["Arid West", "Irrigated Canal"],
        "districts": "Jaisalmer, Bikaner, Barmer, Jodhpur, Sri Ganganagar",
        "soil": "Sandy loam, deep well-drained arid soil",
        "water_need": "Medium",
        "drought_fit": "Excellent",
        "duration_days": 1460,
        "sowing": "Plant tissue-culture plants or offshoots during February-March or July-August",
        "harvest": "June to July after bearing starts",
        "rainfall_mm": "Arid crop with assured irrigation",
        "temperature_c": "25-45",
        "seed_rate_kg_ha": 0.0,
        "spacing": "8 x 8 m",
        "irrigation": "Regular irrigation is needed in arid climate; drip is preferred",
        "common_issues": "Red palm weevil, fruit rot, bird damage",
        "best_practices": "Use quality plants, maintain male plants for pollination, use drip irrigation, and protect fruit bunches.",
        "market_use": "Fresh dates, dry dates, premium arid fruit market",
    },
    {
        "crop": "Sweet Orange",
        "hindi": "मौसंबी",
        "type": "Fruit",
        "season": "Perennial",
        "zones": ["Hadoti", "Eastern Plains"],
        "districts": "Jhalawar, Kota, Baran, Bundi, Alwar, Bharatpur",
        "soil": "Well-drained loam to sandy loam",
        "water_need": "High",
        "drought_fit": "Low",
        "duration_days": 1460,
        "sowing": "Planting July to September",
        "harvest": "October to January after bearing starts",
        "rainfall_mm": "Irrigation supported orchard crop",
        "temperature_c": "15-35",
        "seed_rate_kg_ha": 0.0,
        "spacing": "6 x 6 m",
        "irrigation": "Regular irrigation required; drip improves water use",
        "common_issues": "Citrus canker, gummosis, citrus psylla, fruit drop",
        "best_practices": "Use disease-free budded plants, maintain drainage, prune dry branches, and monitor citrus pests.",
        "market_use": "Fresh fruit, juice, citrus market",
    },
    {
        "crop": "Turmeric",
        "hindi": "हल्दी",
        "type": "Spice",
        "season": "Kharif",
        "zones": ["Tribal South", "Mewar", "Hadoti"],
        "districts": "Banswara, Dungarpur, Udaipur, Pratapgarh, Jhalawar",
        "soil": "Well-drained loam to clay loam rich in organic matter",
        "water_need": "High",
        "drought_fit": "Low",
        "duration_days": 240,
        "sowing": "April to June before or with monsoon",
        "harvest": "January to March when leaves dry",
        "rainfall_mm": "800-1200 or irrigation supported",
        "temperature_c": "20-35",
        "seed_rate_kg_ha": 2000.0,
        "spacing": "45 x 20 cm",
        "irrigation": "Regular irrigation and mulching; avoid waterlogging",
        "common_issues": "Rhizome rot, leaf spot, shoot borer",
        "best_practices": "Use healthy rhizomes, treat seed material, mulch after planting, and harvest after full maturity.",
        "market_use": "Spice, powder, medicine, processing",
    },
    {
        "crop": "Ginger",
        "hindi": "अदरक",
        "type": "Spice",
        "season": "Kharif",
        "zones": ["Tribal South", "Mewar"],
        "districts": "Udaipur, Banswara, Dungarpur, Pratapgarh, Sirohi",
        "soil": "Loose loam rich in organic matter, well-drained soil",
        "water_need": "High",
        "drought_fit": "Low",
        "duration_days": 240,
        "sowing": "April to May before monsoon",
        "harvest": "December to February",
        "rainfall_mm": "900-1500 or irrigation supported",
        "temperature_c": "20-30",
        "seed_rate_kg_ha": 1500.0,
        "spacing": "30 x 20 cm",
        "irrigation": "Frequent light irrigation and mulch; avoid stagnant water",
        "common_issues": "Rhizome rot, bacterial wilt, shoot borer",
        "best_practices": "Use disease-free rhizomes, plant on raised beds, mulch well, and remove infected plants quickly.",
        "market_use": "Fresh ginger, dry ginger, spice, medicine",
    },
    {
        "crop": "Marigold",
        "hindi": "गेंदा",
        "type": "Flower",
        "season": "Rabi / Kharif",
        "zones": ["Eastern Plains", "Semi-arid Central", "Hadoti", "Mewar"],
        "districts": "Jaipur, Ajmer, Alwar, Kota, Udaipur, Bhilwara",
        "soil": "Well-drained loam to sandy loam",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 100,
        "sowing": "Nursery June-July or September-October; transplant after 25-30 days",
        "harvest": "Flower picking starts 55-70 days after transplanting",
        "rainfall_mm": "Irrigated flower crop",
        "temperature_c": "18-30",
        "seed_rate_kg_ha": 1.0,
        "spacing": "45 x 30 cm",
        "irrigation": "Regular irrigation; avoid wet flowers during picking",
        "common_issues": "Aphid, thrips, leaf spot, flower blight",
        "best_practices": "Use healthy seedlings, pinch plants for branching, pick flowers regularly, and keep beds weed-free.",
        "market_use": "Garlands, decoration, religious use, flower market",
    },
    {
        "crop": "Rose",
        "hindi": "गुलाब",
        "type": "Flower",
        "season": "Perennial",
        "zones": ["Eastern Plains", "Semi-arid Central", "Mewar"],
        "districts": "Jaipur, Ajmer, Alwar, Udaipur, Pushkar belt, Sikar",
        "soil": "Well-drained loam rich in organic matter",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 365,
        "sowing": "Plant rooted cuttings or budded plants during July-August or January-February",
        "harvest": "Flower harvest starts 4-6 months after planting",
        "rainfall_mm": "Irrigated flower crop",
        "temperature_c": "15-30",
        "seed_rate_kg_ha": 0.0,
        "spacing": "75 x 75 cm",
        "irrigation": "Regular irrigation; drip is useful for quality flowers",
        "common_issues": "Aphid, thrips, powdery mildew, black spot",
        "best_practices": "Use healthy planting material, prune regularly, remove diseased leaves, and pick flowers early morning.",
        "market_use": "Loose flowers, garlands, rose water, perfume, decoration",
    },    
]


ZONE_NOTES = {
    "Arid West": "Low rainfall, sandy soils, strong fit for bajra, moth, guar, cumin, isabgol, taramira.",
    "Shekhawati": "Semi-arid dryland farming with pulses, mustard, barley, bajra and fodder crops.",
    "Semi-arid Central": "Mixed dryland and irrigated fields around Jaipur, Ajmer, Nagaur, Tonk and nearby belts.",
    "Eastern Plains": "Better irrigation access in many villages; mustard, wheat, vegetables and fodder can work well.",
    "Hadoti": "Black soil belt; soybean, coriander, garlic, wheat, lentil and vegetables are common choices.",
    "Mewar": "Mixed terrain; maize, pulses, oilseeds, spices and vegetables suit many rural fields.",
    "Tribal South": "Higher rainfall pockets; maize, paddy, arhar and mixed farming are useful.",
    "Irrigated Canal": "Assured irrigation belt; wheat, cotton, rice, mustard and fodder crops are possible.",
}


def build_dataframe() -> pd.DataFrame:
    """✅ FIXED: Removed redundant zone_text column"""
    df = pd.DataFrame(RAJASTHAN_CROPS)
    # Create search_blob for filtering
    df["search_blob"] = (
        df["crop"]
        + " "
        + df["hindi"]
        + " "
        + df["type"]
        + " "
        + df["season"]
        + " "
        + df["districts"]
        + " "
        + df["soil"]
        + " "
        + df["zones"].apply(lambda items: ", ".join(items))
    ).str.lower()
    return df


def inject_css() -> None:
    st.markdown(
        """
        <style>
        :root {
            --green: #1f6b45;
            --green-soft: #e8f3ec;
            --mustard: #c78a18;
            --terracotta: #a84f32;
            --ink: #243126;
            --muted: #687568;
            --line: #dfe7dd;
            --paper: #fbfaf5;
        }

        .stApp {
            background:
                linear-gradient(180deg, rgba(255, 252, 244, 0.92) 0%, rgba(245, 250, 241, 0.96) 58%, #ffffff 100%),
                repeating-linear-gradient(112deg, rgba(31, 107, 69, 0.07) 0 2px, transparent 2px 32px),
                linear-gradient(180deg, #f5ead6 0%, #e9f4e8 48%, #ffffff 100%);
            background-attachment: fixed;
            color: var(--ink);
        }

        [data-testid="stAppViewContainer"] > .main {
            background: transparent;
        }

        section[data-testid="stSidebar"] {
            background: #f4f0e6;
            border-right: 1px solid var(--line);
        }

        h1, h2, h3 {
            color: var(--ink);
            letter-spacing: 0;
        }

        .hero {
            border: 1px solid #c8ddc3;
            background:
                linear-gradient(135deg, rgba(27, 94, 60, 0.96), rgba(54, 117, 70, 0.88) 58%, rgba(143, 95, 34, 0.82)),
                repeating-linear-gradient(118deg, rgba(255,255,255,0.18) 0 2px, transparent 2px 26px),
                linear-gradient(180deg, #315f3e, #7d6a2d);
            color: white;
            padding: 28px 30px;
            border-radius: 8px;
            margin-bottom: 18px;
            box-shadow: 0 16px 36px rgba(44, 83, 47, 0.16);
        }

        .hero h1 {
            color: white;
            font-size: 2.2rem;
            line-height: 1.15;
            margin: 0 0 8px 0;
        }

        .hero p {
            max-width: 900px;
            margin: 0;
            color: #eef8ef;
            font-size: 1.02rem;
        }

        .mini-note {
            color: var(--muted);
            font-size: 0.9rem;
            margin-top: -4px;
        }

        .crop-card {
            background: rgba(255,255,255,0.96);
            border: 1px solid var(--line);
            border-left: 5px solid var(--green);
            border-radius: 8px;
            padding: 16px 17px;
            min-height: 270px;
            box-shadow: 0 10px 24px rgba(61, 81, 55, 0.06);
            margin-bottom: 14px;
        }

        .crop-card h3 {
            margin: 0 0 4px 0;
            font-size: 1.22rem;
        }

        .tag-row {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin: 10px 0 12px 0;
        }

        .tag {
            border-radius: 999px;
            padding: 4px 9px;
            font-size: 0.78rem;
            font-weight: 700;
            background: #eef5e8;
            color: #315b36;
            border: 1px solid #d8e6d2;
        }

        .tag.water-low {
            background: #e8f3ec;
            color: #1f6b45;
        }

        .tag.water-medium {
            background: #fff3d8;
            color: #8a5a00;
        }

        .tag.water-high {
            background: #e7f0fa;
            color: #24577a;
        }

        .field-label {
            color: var(--muted);
            font-weight: 700;
            font-size: 0.78rem;
            text-transform: uppercase;
        }

        .card-line {
            margin: 6px 0;
            color: #2f3b31;
            font-size: 0.94rem;
        }

        div[data-testid="stMetric"] {
            background: white;
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 12px 14px;
            box-shadow: 0 8px 22px rgba(61, 81, 55, 0.05);
        }

        .advisory-box {
            background: #fffaf0;
            border: 1px solid #ead8a8;
            border-left: 5px solid var(--mustard);
            border-radius: 8px;
            padding: 14px 16px;
            margin-top: 10px;
        }

        .source-box {
            background: #f2f7f8;
            border: 1px solid #d4e3e7;
            border-radius: 8px;
            padding: 12px 14px;
            color: #375056;
            font-size: 0.9rem;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 6px;
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 8px 8px 0 0;
            padding: 10px 14px;
            background: #eef4ea;
        }

        .stTabs [aria-selected="true"] {
            background: white;
            color: var(--green);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def water_class(value: str) -> str:
    return {
        "Low": "water-low",
        "Medium": "water-medium",
        "High": "water-high",
    }.get(value, "water-medium")


def crop_card(row: pd.Series) -> None:
    st.markdown(
        f"""
        <div class="crop-card">
            <h3>{row['crop']} <span style="color:#687568;font-weight:600;">({row['hindi']})</span></h3>
            <div class="tag-row">
                <span class="tag">{row['season']}</span>
                <span class="tag">{row['type']}</span>
                <span class="tag {water_class(row['water_need'])}">{row['water_need']} water</span>
                <span class="tag">Drought: {row['drought_fit']}</span>
            </div>
            <div class="card-line"><span class="field-label">Rural belts</span><br>{row['districts']}</div>
            <div class="card-line"><span class="field-label">Soil</span><br>{row['soil']}</div>
            <div class="card-line"><span class="field-label">Sowing</span><br>{row['sowing']}</div>
            <div class="card-line"><span class="field-label">Irrigation</span><br>{row['irrigation']}</div>
            <div class="card-line"><span class="field-label">Main care</span><br>{row['best_practices']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    all_seasons = sorted(df["season"].unique())
    all_types = sorted(df["type"].unique())
    all_waters = ["Low", "Medium", "High"]
    all_zones = sorted({zone for zones in df["zones"] for zone in zones})

    with st.sidebar:
        st.header("Find Suitable Crops")
        query = st.text_input("Search crop, district, soil", placeholder="Example: Nagaur, sandy, bajra")
        seasons = st.multiselect("Season", all_seasons, default=all_seasons)
        crop_types = st.multiselect("Crop type", all_types, default=all_types)
        water = st.multiselect("Water need", all_waters, default=all_waters)
        zones = st.multiselect("Rural zone", all_zones, default=all_zones)
        drought_only = st.checkbox("Show drought-strong crops only")

    filtered = df[
        df["season"].isin(seasons)
        & df["type"].isin(crop_types)
        & df["water_need"].isin(water)
        & df["zones"].apply(lambda items: any(zone in items for zone in zones))
    ].copy()

    if query.strip():
        filtered = filtered[filtered["search_blob"].str.contains(query.strip().lower(), na=False)]

    if drought_only:
        filtered = filtered[filtered["drought_fit"].isin(["Good", "Excellent"])]

    return filtered


def area_to_hectare(area: float, unit: str) -> float:
    if unit == "Hectare":
        return area
    if unit == "Acre":
        return area * 0.404686
    return area * 0.253


def show_overview_metrics(df: pd.DataFrame, filtered: pd.DataFrame) -> None:
    low_water = int((filtered["water_need"] == "Low").sum())
    drought_count = int(filtered["drought_fit"].isin(["Good", "Excellent"]).sum())
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Crops in Database", len(df))
    c2.metric("Matching Crops", len(filtered))
    c3.metric("Low Water Matches", low_water)
    c4.metric("Drought Strong Matches", drought_count)


def show_crop_finder(filtered: pd.DataFrame) -> None:
    if filtered.empty:
        st.warning("No crop matched your filters. Try removing one filter or searching a wider district/soil term.")
        return

    st.caption("Cards are arranged for quick village-level decision making. Confirm final crop choice with local agriculture officers or KVK.")
    left, right = st.columns(2)
    for index, (_, row) in enumerate(filtered.sort_values(["season", "crop"]).iterrows()):
        with left if index % 2 == 0 else right:
            crop_card(row)


def show_compare(df: pd.DataFrame) -> None:
    default_crops = ["Bajra", "Mustard", "Gram", "Guar"]
    selected = st.multiselect(
        "Choose crops to compare",
        sorted(df["crop"].tolist()),
        default=[crop for crop in default_crops if crop in df["crop"].tolist()],
        max_selections=6,
    )

    if not selected:
        st.info("Select two or more crops to compare.")
        return

    compare_columns = [
        "crop",
        "hindi",
        "season",
        "type",
        "water_need",
        "drought_fit",
        "duration_days",
        "soil",
        "sowing",
        "harvest",
        "seed_rate_kg_ha",
        "common_issues",
        "market_use",
    ]
    compare_df = df[df["crop"].isin(selected)][compare_columns].rename(
        columns={
            "crop": "Crop",
            "hindi": "Hindi",
            "season": "Season",
            "type": "Type",
            "water_need": "Water",
            "drought_fit": "Drought Fit",
            "duration_days": "Duration Days",
            "soil": "Soil",
            "sowing": "Sowing Window",
            "harvest": "Harvest Window",
            "seed_rate_kg_ha": "Seed kg/ha",
            "common_issues": "Main Risks",
            "market_use": "Market Use",
        }
    )
    st.dataframe(compare_df, use_container_width=True, hide_index=True)


def show_calendar(df: pd.DataFrame) -> None:
    st.subheader("Crop Calendar")
    st.write("Use this as a planning view for sowing, harvest, irrigation and input purchase timing.")

    calendar_df = df[
        [
            "crop",
            "hindi",
            "season",
            "zones",
            "sowing",
            "harvest",
            "duration_days",
            "water_need",
            "seed_rate_kg_ha",
        ]
    ].copy()
    calendar_df["zones"] = calendar_df["zones"].apply(", ".join)
    calendar_df = calendar_df.rename(
        columns={
            "crop": "Crop",
            "hindi": "Hindi",
            "season": "Season",
            "zones": "Best Rural Zones",
            "sowing": "Sowing",
            "harvest": "Harvest",
            "duration_days": "Duration Days",
            "water_need": "Water",
            "seed_rate_kg_ha": "Seed kg/ha",
        }
    )
    st.dataframe(calendar_df.sort_values(["Season", "Crop"]), use_container_width=True, hide_index=True)

    chart_data = df.groupby(["season", "water_need"]).size().reset_index(name="count")
    pivot = chart_data.pivot(index="season", columns="water_need", values="count").fillna(0)
    st.bar_chart(pivot)


def show_planner(df: pd.DataFrame) -> None:
    st.subheader("Village Crop Planner")
    st.write("Select your rural zone, season and water situation. The app will shortlist practical crops from the local database.")

    c1, c2, c3 = st.columns(3)
    zone = c1.selectbox("Rural zone", sorted(ZONE_NOTES.keys()))
    season = c2.selectbox("Season", ["Kharif", "Rabi", "Kharif / Summer", "Kharif / Rabi", "Rabi / Kharif", "Rabi / Perennial"])
    water = c3.selectbox("Water availability", ["Low", "Medium", "High"])

    water_rank = {"Low": 1, "Medium": 2, "High": 3}
    recommendation = df[
        df["zones"].apply(lambda zones: zone in zones)
        & df["season"].str.contains(season.split(" / ")[0], case=False, regex=False)
        & df["water_need"].map(water_rank).le(water_rank[water])
    ].copy()

    st.markdown(f"<div class='advisory-box'><b>{zone}</b>: {ZONE_NOTES[zone]}</div>", unsafe_allow_html=True)

    if recommendation.empty:
        st.info("No exact match found. Increase water availability or choose a nearby rural zone.")
    else:
        st.markdown("#### Recommended shortlist")
        st.dataframe(
            recommendation[
                [
                    "crop",
                    "hindi",
                    "type",
                    "water_need",
                    "drought_fit",
                    "sowing",
                    "harvest",
                    "districts",
                    "best_practices",
                ]
            ].rename(
                columns={
                    "crop": "Crop",
                    "hindi": "Hindi",
                    "type": "Type",
                    "water_need": "Water",
                    "drought_fit": "Drought Fit",
                    "sowing": "Sowing",
                    "harvest": "Harvest",
                    "districts": "District Belts",
                    "best_practices": "Best Practice",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )

    st.markdown("#### Seed Requirement Estimate")
    c4, c5, c6 = st.columns(3)
    selected_crop = c4.selectbox("Crop", sorted(df["crop"].tolist()))
    area = c5.number_input("Farm area", min_value=0.1, value=1.0, step=0.1)
    unit = c6.selectbox("Unit", ["Hectare", "Acre", "Bigha"])

    # ✅ FIXED: Added error handling for missing crops
    crop_data = df[df["crop"] == selected_crop]
    if crop_data.empty:
        st.error("Crop not found in database!")
    else:
        crop_row = crop_data.iloc[0]
        hectare = area_to_hectare(area, unit)
        seed_required = hectare * float(crop_row["seed_rate_kg_ha"])

        st.success(
            f"For {area:g} {unit} of {selected_crop}, approximate seed need is {seed_required:.1f} kg. "
            f"Use local recommended variety and seed rate before purchase."
        )


def show_data_table(df: pd.DataFrame) -> None:
    st.subheader("Full Crop Data")
    
    # ✅ FIXED: Proper column selection and zones conversion
    export_df = df[
        [col for col in df.columns if col not in ["search_blob", "zones"]]
    ].copy()
    
    # Add formatted zones column
    export_df["zones"] = df["zones"].apply(", ".join)
    
    st.dataframe(export_df, use_container_width=True, hide_index=True)

export_df = filtered_df.drop(
    columns=["search_blob"],
    errors="ignore"
)

csv = export_df.to_csv(index=False)

st.download_button(
    "Download CSV",
    csv,
    "gramsathi_crops.csv",
    "text/csv"
)

    st.markdown(
        """
        <div class="source-box">
            <b>Use note:</b> This is a practical planning dataset for Rajasthan rural crop selection.
            Weather, soil test, seed variety and mandi conditions change by village and year, so final
            decisions should be checked with the local Agriculture Department, Krishi Vigyan Kendra,
            or experienced local agronomist.
        </div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    inject_css()
    df = build_dataframe()
    filtered = filter_dataframe(df)

    st.markdown(
        """
        <div class="hero">
            <h1>GramSathi Crop Guide</h1>
            <p>Rajasthan rural crop database with season-wise filters, water planning, crop comparison,
            sowing calendar and seed requirement estimate for village-level decisions.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    show_overview_metrics(df, filtered)
    st.markdown("<p class='mini-note'>Built as a clean crop advisory dashboard, not a chatbot-style AI screen.</p>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Crop Finder", "Compare", "Calendar", "Village Planner", "Data Table"]
    )

    with tab1:
        show_crop_finder(filtered)

    with tab2:
        show_compare(df)

    with tab3:
        show_calendar(df)

    with tab4:
        show_planner(df)

    with tab5:
        show_data_table(df)


if __name__ == "__main__":
    main()
