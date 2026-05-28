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
        "zones": ["Eastern Plains", "Shekhawati", "Irrigated Canal", "Semi-arid Central"],
        "districts": "Alwar, Bharatpur, Jaipur, Tonk, Sikar, Jhunjhunu, Hanumangarh, Sri Ganganagar",
        "soil": "Loam to sandy loam",
        "water_need": "Medium",
        "drought_fit": "Good",
        "duration_days": 120,
        "sowing": "October to November",
        "harvest": "February to March",
        "rainfall_mm": "300-500",
        "temperature_c": "18-28",
        "seed_rate_kg_ha": 5.0,
        "spacing": "30-45 cm row spacing",
        "irrigation": "1-3 irrigations; flowering and pod filling are important",
        "common_issues": "Aphid, white rust, alternaria blight",
        "best_practices": "Use clean seed, keep balanced sulphur nutrition, avoid late sowing, inspect aphid early.",
        "market_use": "Edible oil, oilcake, spices",
    },
    {
        "crop": "Gram",
        "hindi": "चना",
        "type": "Pulse",
        "season": "Rabi",
        "zones": ["Arid West", "Semi-arid Central", "Eastern Plains"],
        "districts": "Bikaner, Churu, Nagaur, Jaipur, Ajmer, Jaisalmer, Tonk",
        "soil": "Well-drained loam, sandy loam",
        "water_need": "Low",
        "drought_fit": "Good",
        "duration_days": 115,
        "sowing": "October to November",
        "harvest": "February to March",
        "rainfall_mm": "300-450",
        "temperature_c": "20-28",
        "seed_rate_kg_ha": 75.0,
        "spacing": "30 cm row spacing",
        "irrigation": "Often rainfed; avoid waterlogging",
        "common_issues": "Wilt, pod borer, collar rot",
        "best_practices": "Treat seed with rhizobium and fungicide, use wilt-tolerant seed, avoid excess irrigation.",
        "market_use": "Dal, besan, roasted grain, fodder",
    },
    {
        "crop": "Barley",
        "hindi": "जौ",
        "type": "Cereal",
        "season": "Rabi",
        "zones": ["Shekhawati", "Eastern Plains", "Semi-arid Central"],
        "districts": "Jaipur, Sikar, Alwar, Ajmer, Bharatpur, Nagaur",
        "soil": "Loam, sandy loam, alkaline-tolerant soil",
        "water_need": "Medium",
        "drought_fit": "Good",
        "duration_days": 115,
        "sowing": "November",
        "harvest": "March to April",
        "rainfall_mm": "300-500",
        "temperature_c": "12-25",
        "seed_rate_kg_ha": 85.0,
        "spacing": "22 cm row spacing",
        "irrigation": "2-3 irrigations if available",
        "common_issues": "Rust, smut, aphid",
        "best_practices": "Use treated seed, avoid very late sowing, manage weeds in first 35 days.",
        "market_use": "Malt, animal feed, grain",
    },
    {
        "crop": "Maize",
        "hindi": "मक्का",
        "type": "Cereal",
        "season": "Kharif",
        "zones": ["Tribal South", "Mewar", "Hadoti"],
        "districts": "Udaipur, Banswara, Dungarpur, Pratapgarh, Chittorgarh, Bhilwara",
        "soil": "Well-drained loam, medium black soil",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 95,
        "sowing": "June to July",
        "harvest": "September to October",
        "rainfall_mm": "500-800",
        "temperature_c": "24-32",
        "seed_rate_kg_ha": 20.0,
        "spacing": "60 x 20 cm",
        "irrigation": "Needs moisture at knee-high, tasseling, and grain filling",
        "common_issues": "Fall armyworm, stem borer, leaf blight",
        "best_practices": "Use line sowing, maintain plant population, watch whorl damage, apply balanced nutrition.",
        "market_use": "Grain, green cob, poultry feed, fodder",
    },
    {
        "crop": "Moong",
        "hindi": "मूंग",
        "type": "Pulse",
        "season": "Kharif / Summer",
        "zones": ["Arid West", "Semi-arid Central", "Shekhawati"],
        "districts": "Nagaur, Jodhpur, Pali, Ajmer, Barmer, Jaipur, Tonk",
        "soil": "Light loam, sandy loam",
        "water_need": "Low",
        "drought_fit": "Good",
        "duration_days": 65,
        "sowing": "June to July for kharif; March for summer with irrigation",
        "harvest": "August to September; May for summer",
        "rainfall_mm": "300-500",
        "temperature_c": "25-35",
        "seed_rate_kg_ha": 15.0,
        "spacing": "30 x 10 cm",
        "irrigation": "Rainfed in kharif; light irrigation in summer",
        "common_issues": "Yellow mosaic virus, whitefly, pod borer",
        "best_practices": "Use disease-free seed, seed treatment, avoid waterlogging, pick pods in multiple rounds.",
        "market_use": "Dal, sprouts, green manure",
    },
    {
        "crop": "Moth Bean",
        "hindi": "मोठ",
        "type": "Pulse",
        "season": "Kharif",
        "zones": ["Arid West", "Shekhawati"],
        "districts": "Jaisalmer, Barmer, Bikaner, Jodhpur, Nagaur, Churu",
        "soil": "Sandy, light soil",
        "water_need": "Low",
        "drought_fit": "Excellent",
        "duration_days": 75,
        "sowing": "July after rain",
        "harvest": "September to October",
        "rainfall_mm": "200-400",
        "temperature_c": "25-36",
        "seed_rate_kg_ha": 12.0,
        "spacing": "30-45 cm rows",
        "irrigation": "Mostly rainfed",
        "common_issues": "Yellow mosaic, pod borer, dry spell",
        "best_practices": "Best for low-rainfall fields; keep weed-free early and avoid dense sowing.",
        "market_use": "Dal, sprouts, fodder",
    },
    {
        "crop": "Guar",
        "hindi": "ग्वार",
        "type": "Pulse / Industrial",
        "season": "Kharif",
        "zones": ["Arid West", "Shekhawati", "Irrigated Canal"],
        "districts": "Bikaner, Churu, Jodhpur, Barmer, Nagaur, Hanumangarh, Sri Ganganagar",
        "soil": "Sandy loam, well-drained soil",
        "water_need": "Low",
        "drought_fit": "Excellent",
        "duration_days": 95,
        "sowing": "June to July",
        "harvest": "October to November",
        "rainfall_mm": "250-450",
        "temperature_c": "25-35",
        "seed_rate_kg_ha": 18.0,
        "spacing": "45 x 15 cm",
        "irrigation": "Rainfed; excess water reduces performance",
        "common_issues": "Bacterial blight, powdery mildew, aphid",
        "best_practices": "Use treated seed, do not over-irrigate, choose grain or vegetable type as per market.",
        "market_use": "Guar gum, vegetable pods, fodder",
    },
    {
        "crop": "Groundnut",
        "hindi": "मूंगफली",
        "type": "Oilseed",
        "season": "Kharif",
        "zones": ["Semi-arid Central", "Eastern Plains", "Arid West"],
        "districts": "Bikaner, Jaipur, Jodhpur, Nagaur, Sikar, Dausa",
        "soil": "Sandy loam, well-drained light soil",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 120,
        "sowing": "June to July",
        "harvest": "October to November",
        "rainfall_mm": "500-700",
        "temperature_c": "24-32",
        "seed_rate_kg_ha": 110.0,
        "spacing": "30 x 10 cm",
        "irrigation": "Moisture at flowering and pegging is critical",
        "common_issues": "Tikka disease, collar rot, white grub",
        "best_practices": "Use bold healthy kernels, gypsum at pegging, avoid standing water.",
        "market_use": "Edible oil, kernels, fodder",
    },
    {
        "crop": "Sesame",
        "hindi": "तिल",
        "type": "Oilseed",
        "season": "Kharif",
        "zones": ["Arid West", "Semi-arid Central", "Mewar"],
        "districts": "Pali, Jodhpur, Jalore, Bhilwara, Tonk, Sawai Madhopur",
        "soil": "Light loam, sandy loam",
        "water_need": "Low",
        "drought_fit": "Good",
        "duration_days": 90,
        "sowing": "June to July",
        "harvest": "September to October",
        "rainfall_mm": "300-500",
        "temperature_c": "25-35",
        "seed_rate_kg_ha": 4.0,
        "spacing": "30 x 10 cm",
        "irrigation": "Rainfed; avoid waterlogging",
        "common_issues": "Phyllody, leaf spot, capsule borer",
        "best_practices": "Keep drainage, thin plants after emergence, harvest before capsule shattering.",
        "market_use": "Oil, sweets, bakery, religious use",
    },
    {
        "crop": "Cumin",
        "hindi": "जीरा",
        "type": "Spice",
        "season": "Rabi",
        "zones": ["Arid West", "Semi-arid Central"],
        "districts": "Jalore, Barmer, Jodhpur, Nagaur, Pali",
        "soil": "Well-drained sandy loam",
        "water_need": "Low",
        "drought_fit": "Medium",
        "duration_days": 110,
        "sowing": "November",
        "harvest": "February to March",
        "rainfall_mm": "Low humidity with light irrigation",
        "temperature_c": "15-28",
        "seed_rate_kg_ha": 12.0,
        "spacing": "25-30 cm row spacing",
        "irrigation": "Light irrigations; avoid humid/wet conditions",
        "common_issues": "Wilt, blight, powdery mildew",
        "best_practices": "Use clean fields, treated seed, avoid dense sowing, irrigate lightly.",
        "market_use": "Spice, seed trade",
    },
    {
        "crop": "Coriander",
        "hindi": "धनिया",
        "type": "Spice",
        "season": "Rabi",
        "zones": ["Hadoti", "Mewar"],
        "districts": "Kota, Bundi, Baran, Jhalawar, Chittorgarh",
        "soil": "Black soil, loam, fertile medium soil",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 110,
        "sowing": "October to November",
        "harvest": "February to March",
        "rainfall_mm": "350-600 with irrigation",
        "temperature_c": "15-28",
        "seed_rate_kg_ha": 15.0,
        "spacing": "30 cm row spacing",
        "irrigation": "2-4 irrigations, avoid excess at flowering",
        "common_issues": "Stem gall, aphid, powdery mildew",
        "best_practices": "Split seed before sowing, maintain drainage, harvest when seeds turn brown.",
        "market_use": "Seed spice, green leaves",
    },
    {
        "crop": "Fennel",
        "hindi": "सौंफ",
        "type": "Spice",
        "season": "Rabi",
        "zones": ["Arid West", "Mewar"],
        "districts": "Sirohi, Jalore, Pali, Udaipur",
        "soil": "Well-drained loam",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 170,
        "sowing": "October",
        "harvest": "March to April",
        "rainfall_mm": "350-550 with irrigation",
        "temperature_c": "15-28",
        "seed_rate_kg_ha": 10.0,
        "spacing": "45 x 20 cm",
        "irrigation": "Regular light irrigation; avoid water stress at flowering",
        "common_issues": "Aphid, wilt, powdery mildew",
        "best_practices": "Thin plants, keep uniform moisture, harvest umbels in stages.",
        "market_use": "Seed spice, mouth freshener, medicine",
    },
    {
        "crop": "Fenugreek",
        "hindi": "मेथी",
        "type": "Spice / Leafy",
        "season": "Rabi",
        "zones": ["Semi-arid Central", "Shekhawati", "Arid West"],
        "districts": "Nagaur, Jaipur, Sikar, Jodhpur, Ajmer",
        "soil": "Loam to sandy loam",
        "water_need": "Low",
        "drought_fit": "Good",
        "duration_days": 100,
        "sowing": "October to November",
        "harvest": "January to March",
        "rainfall_mm": "250-450",
        "temperature_c": "15-27",
        "seed_rate_kg_ha": 25.0,
        "spacing": "25-30 cm rows",
        "irrigation": "Light irrigation as needed",
        "common_issues": "Powdery mildew, aphid, root rot",
        "best_practices": "Can be grown for leaves or seed; avoid overwatering and harvest leaves tender.",
        "market_use": "Green leaves, seed spice, medicine",
    },
    {
        "crop": "Isabgol",
        "hindi": "ईसबगोल",
        "type": "Medicinal",
        "season": "Rabi",
        "zones": ["Arid West"],
        "districts": "Jalore, Barmer, Sirohi, Pali",
        "soil": "Light sandy loam, well drained",
        "water_need": "Low",
        "drought_fit": "Medium",
        "duration_days": 120,
        "sowing": "November",
        "harvest": "March",
        "rainfall_mm": "Low rainfall, dry weather",
        "temperature_c": "15-30",
        "seed_rate_kg_ha": 6.0,
        "spacing": "30 cm rows",
        "irrigation": "Light irrigation; crop dislikes high humidity",
        "common_issues": "Downy mildew, wilt, seed shattering",
        "best_practices": "Sow shallow, keep weed-free, harvest during dry weather to protect husk quality.",
        "market_use": "Husk, medicine, export crop",
    },
    {
        "crop": "Cotton",
        "hindi": "कपास",
        "type": "Fiber",
        "season": "Kharif",
        "zones": ["Irrigated Canal", "Tribal South"],
        "districts": "Sri Ganganagar, Hanumangarh, Banswara, Bhilwara",
        "soil": "Deep loam, black soil, good drainage",
        "water_need": "High",
        "drought_fit": "Low",
        "duration_days": 170,
        "sowing": "April to June depending on irrigation",
        "harvest": "October to December",
        "rainfall_mm": "500-800 with irrigation support",
        "temperature_c": "21-35",
        "seed_rate_kg_ha": 2.0,
        "spacing": "90 x 45 cm, varies by hybrid",
        "irrigation": "Regular irrigation; avoid waterlogging",
        "common_issues": "Whitefly, pink bollworm, sucking pests",
        "best_practices": "Use recommended hybrids, install pheromone traps, avoid unnecessary pesticide sprays.",
        "market_use": "Lint, seed oil, oilcake",
    },
    {
        "crop": "Soybean",
        "hindi": "सोयाबीन",
        "type": "Oilseed / Pulse",
        "season": "Kharif",
        "zones": ["Hadoti", "Mewar"],
        "districts": "Kota, Baran, Jhalawar, Bundi, Chittorgarh",
        "soil": "Medium black soil, well-drained clay loam",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 100,
        "sowing": "June to July",
        "harvest": "September to October",
        "rainfall_mm": "600-900",
        "temperature_c": "22-32",
        "seed_rate_kg_ha": 75.0,
        "spacing": "45 x 5 cm",
        "irrigation": "Rainfed; drainage is very important",
        "common_issues": "Yellow mosaic, girdle beetle, stem fly",
        "best_practices": "Treat seed with rhizobium, maintain drainage, avoid very late sowing.",
        "market_use": "Oil, meal, food processing",
    },
    {
        "crop": "Urad",
        "hindi": "उड़द",
        "type": "Pulse",
        "season": "Kharif",
        "zones": ["Hadoti", "Mewar", "Tribal South"],
        "districts": "Kota, Bundi, Bhilwara, Udaipur, Chittorgarh",
        "soil": "Loam to black soil with drainage",
        "water_need": "Low",
        "drought_fit": "Medium",
        "duration_days": 80,
        "sowing": "June to July",
        "harvest": "September",
        "rainfall_mm": "400-700",
        "temperature_c": "25-35",
        "seed_rate_kg_ha": 18.0,
        "spacing": "30 x 10 cm",
        "irrigation": "Mostly rainfed; no standing water",
        "common_issues": "Yellow mosaic, whitefly, leaf spot",
        "best_practices": "Use resistant seed where available, control whitefly early, keep field drained.",
        "market_use": "Dal, papad, green manure",
    },
    {
        "crop": "Arhar",
        "hindi": "अरहर",
        "type": "Pulse",
        "season": "Kharif",
        "zones": ["Tribal South", "Mewar", "Hadoti"],
        "districts": "Udaipur, Banswara, Dungarpur, Pratapgarh, Kota",
        "soil": "Well-drained loam to black soil",
        "water_need": "Medium",
        "drought_fit": "Good",
        "duration_days": 165,
        "sowing": "June to July",
        "harvest": "December to January",
        "rainfall_mm": "600-900",
        "temperature_c": "24-34",
        "seed_rate_kg_ha": 15.0,
        "spacing": "60 x 20 cm",
        "irrigation": "Rainfed; sensitive to waterlogging",
        "common_issues": "Pod borer, wilt, sterility mosaic",
        "best_practices": "Use wider spacing, intercrop with soybean or maize where suitable, monitor pod borer.",
        "market_use": "Dal, fuelwood-like stems, fodder leaves",
    },
    {
        "crop": "Chilli",
        "hindi": "मिर्च",
        "type": "Vegetable / Spice",
        "season": "Kharif / Rabi",
        "zones": ["Semi-arid Central", "Eastern Plains", "Mewar"],
        "districts": "Jodhpur, Nagaur, Jaipur, Sikar, Ajmer, Chittorgarh",
        "soil": "Fertile loam, well-drained soil",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 150,
        "sowing": "Nursery in June-July or September; transplant after 30-40 days",
        "harvest": "Green picking starts 60-80 days after transplanting",
        "rainfall_mm": "500-700 with irrigation",
        "temperature_c": "20-32",
        "seed_rate_kg_ha": 1.0,
        "spacing": "45 x 45 cm",
        "irrigation": "Frequent light irrigation, drip is useful",
        "common_issues": "Thrips, mites, leaf curl, fruit rot",
        "best_practices": "Raise healthy nursery, use mulch/drip if possible, remove infected plants early.",
        "market_use": "Green chilli, dry chilli, powder",
    },
    {
        "crop": "Garlic",
        "hindi": "लहसुन",
        "type": "Vegetable / Spice",
        "season": "Rabi",
        "zones": ["Hadoti", "Mewar"],
        "districts": "Kota, Baran, Jhalawar, Chittorgarh, Pratapgarh",
        "soil": "Fertile loam, black soil with drainage",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 145,
        "sowing": "October to November",
        "harvest": "March to April",
        "rainfall_mm": "Irrigated rabi crop",
        "temperature_c": "12-25",
        "seed_rate_kg_ha": 500.0,
        "spacing": "15 x 10 cm",
        "irrigation": "Light irrigation every 10-15 days as needed",
        "common_issues": "Thrips, purple blotch, basal rot",
        "best_practices": "Use healthy cloves, avoid waterlogging, stop irrigation before harvest for curing.",
        "market_use": "Fresh bulb, dry bulb, processing",
    },
    {
        "crop": "Onion",
        "hindi": "प्याज",
        "type": "Vegetable",
        "season": "Rabi / Kharif",
        "zones": ["Eastern Plains", "Semi-arid Central", "Shekhawati"],
        "districts": "Alwar, Sikar, Nagaur, Jaipur, Ajmer, Bharatpur",
        "soil": "Fertile sandy loam to loam",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 130,
        "sowing": "Nursery June-July or October-November depending on season",
        "harvest": "Season based; harvest when tops fall",
        "rainfall_mm": "Irrigated vegetable crop",
        "temperature_c": "13-30",
        "seed_rate_kg_ha": 8.0,
        "spacing": "15 x 10 cm",
        "irrigation": "Frequent light irrigation, stop before harvest",
        "common_issues": "Thrips, purple blotch, bulb rot",
        "best_practices": "Use healthy seedlings, keep uniform moisture, cure bulbs properly for storage.",
        "market_use": "Fresh bulb, storage, processing",
    },
    {
        "crop": "Potato",
        "hindi": "आलू",
        "type": "Vegetable",
        "season": "Rabi",
        "zones": ["Hadoti", "Eastern Plains"],
        "districts": "Kota, Bundi, Alwar, Bharatpur, Jaipur",
        "soil": "Loose sandy loam, fertile soil",
        "water_need": "High",
        "drought_fit": "Low",
        "duration_days": 100,
        "sowing": "October to November",
        "harvest": "January to February",
        "rainfall_mm": "Irrigated crop",
        "temperature_c": "15-25",
        "seed_rate_kg_ha": 2000.0,
        "spacing": "60 x 20 cm",
        "irrigation": "Regular irrigation; ridges should remain moist but not waterlogged",
        "common_issues": "Late blight, early blight, cutworm",
        "best_practices": "Use disease-free seed tubers, ridge planting, earth up at the right stage.",
        "market_use": "Table potato, processing, seed tuber",
    },
    {
        "crop": "Tomato",
        "hindi": "टमाटर",
        "type": "Vegetable",
        "season": "Rabi / Kharif",
        "zones": ["Eastern Plains", "Mewar", "Hadoti"],
        "districts": "Jaipur, Alwar, Tonk, Chittorgarh, Kota, Udaipur",
        "soil": "Fertile well-drained loam",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 120,
        "sowing": "Nursery as per local season; transplant after 25-35 days",
        "harvest": "60-75 days after transplanting",
        "rainfall_mm": "Irrigated vegetable crop",
        "temperature_c": "18-30",
        "seed_rate_kg_ha": 0.4,
        "spacing": "60 x 45 cm",
        "irrigation": "Drip preferred; avoid irregular watering",
        "common_issues": "Fruit borer, leaf curl, early blight",
        "best_practices": "Use staking where needed, mulch, regular picking, pest monitoring.",
        "market_use": "Fresh market, sauce, processing",
    },
    {
        "crop": "Jowar",
        "hindi": "ज्वार",
        "type": "Cereal / Fodder",
        "season": "Kharif",
        "zones": ["Semi-arid Central", "Mewar", "Arid West"],
        "districts": "Ajmer, Bhilwara, Pali, Udaipur, Chittorgarh",
        "soil": "Medium black soil, loam, sandy loam",
        "water_need": "Low",
        "drought_fit": "Good",
        "duration_days": 100,
        "sowing": "June to July",
        "harvest": "September to October",
        "rainfall_mm": "350-600",
        "temperature_c": "25-35",
        "seed_rate_kg_ha": 12.0,
        "spacing": "45 cm row spacing",
        "irrigation": "Rainfed; one irrigation helps fodder yield",
        "common_issues": "Shoot fly, stem borer, grain mold",
        "best_practices": "Useful for mixed grain-fodder systems; keep first month weed-free.",
        "market_use": "Grain, green fodder, dry fodder",
    },
    {
        "crop": "Castor",
        "hindi": "अरंडी",
        "type": "Oilseed",
        "season": "Kharif",
        "zones": ["Arid West", "Mewar"],
        "districts": "Jalore, Sirohi, Pali, Barmer, Udaipur",
        "soil": "Well-drained loam to sandy loam",
        "water_need": "Low",
        "drought_fit": "Good",
        "duration_days": 180,
        "sowing": "June to July",
        "harvest": "December to February",
        "rainfall_mm": "400-700",
        "temperature_c": "20-32",
        "seed_rate_kg_ha": 10.0,
        "spacing": "90 x 60 cm",
        "irrigation": "Mostly rainfed; waterlogging is harmful",
        "common_issues": "Semilooper, wilt, capsule borer",
        "best_practices": "Keep wider spacing, remove diseased plants, harvest spikes in stages.",
        "market_use": "Industrial oil, lubricant, medicine industry",
    },
    {
        "crop": "Linseed",
        "hindi": "अलसी",
        "type": "Oilseed",
        "season": "Rabi",
        "zones": ["Hadoti", "Mewar"],
        "districts": "Kota, Bundi, Baran, Chittorgarh, Bhilwara",
        "soil": "Loam to clay loam",
        "water_need": "Low",
        "drought_fit": "Medium",
        "duration_days": 115,
        "sowing": "October to November",
        "harvest": "February to March",
        "rainfall_mm": "300-500",
        "temperature_c": "15-28",
        "seed_rate_kg_ha": 25.0,
        "spacing": "30 cm rows",
        "irrigation": "Rainfed or 1-2 irrigations",
        "common_issues": "Wilt, powdery mildew, bud fly",
        "best_practices": "Avoid late sowing and waterlogging; harvest when capsules mature.",
        "market_use": "Oil, seed, fiber in some systems",
    },
    {
        "crop": "Ajwain",
        "hindi": "अजवाइन",
        "type": "Spice",
        "season": "Rabi",
        "zones": ["Hadoti", "Mewar"],
        "districts": "Chittorgarh, Pratapgarh, Kota, Bhilwara",
        "soil": "Well-drained loam",
        "water_need": "Low",
        "drought_fit": "Medium",
        "duration_days": 140,
        "sowing": "October to November",
        "harvest": "March to April",
        "rainfall_mm": "Dry rabi weather with light irrigation",
        "temperature_c": "15-30",
        "seed_rate_kg_ha": 3.0,
        "spacing": "30 cm rows",
        "irrigation": "Light irrigation; keep field weed-free",
        "common_issues": "Aphid, powdery mildew, wilt",
        "best_practices": "Sow shallow, avoid dense stand, harvest when umbels turn brown.",
        "market_use": "Seed spice, medicine, household use",
    },
    {
        "crop": "Lentil",
        "hindi": "मसूर",
        "type": "Pulse",
        "season": "Rabi",
        "zones": ["Hadoti", "Eastern Plains"],
        "districts": "Kota, Bundi, Baran, Bharatpur, Sawai Madhopur",
        "soil": "Loam, clay loam with drainage",
        "water_need": "Low",
        "drought_fit": "Medium",
        "duration_days": 115,
        "sowing": "October to November",
        "harvest": "February to March",
        "rainfall_mm": "300-500",
        "temperature_c": "18-28",
        "seed_rate_kg_ha": 35.0,
        "spacing": "25-30 cm rows",
        "irrigation": "Usually rainfed; avoid waterlogging",
        "common_issues": "Wilt, rust, pod borer",
        "best_practices": "Seed treatment and rhizobium inoculation improve crop stand.",
        "market_use": "Dal, household pulse",
    },
    {
        "crop": "Field Pea",
        "hindi": "मटर",
        "type": "Pulse / Vegetable",
        "season": "Rabi",
        "zones": ["Eastern Plains", "Hadoti"],
        "districts": "Jaipur, Alwar, Bharatpur, Kota, Bundi",
        "soil": "Fertile loam, well-drained soil",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 95,
        "sowing": "October to November",
        "harvest": "January to March",
        "rainfall_mm": "Irrigated rabi crop",
        "temperature_c": "12-25",
        "seed_rate_kg_ha": 80.0,
        "spacing": "30 x 10 cm",
        "irrigation": "Light irrigation at flowering and pod filling",
        "common_issues": "Powdery mildew, aphid, wilt",
        "best_practices": "Use support for vegetable pea where needed, avoid waterlogging.",
        "market_use": "Green pods, dry pulse",
    },
    {
        "crop": "Rice",
        "hindi": "धान",
        "type": "Cereal",
        "season": "Kharif",
        "zones": ["Hadoti", "Tribal South", "Irrigated Canal"],
        "districts": "Bundi, Kota, Banswara, Dungarpur, Sri Ganganagar, Hanumangarh",
        "soil": "Clay loam, lowland soil, assured water fields",
        "water_need": "High",
        "drought_fit": "Low",
        "duration_days": 125,
        "sowing": "Nursery June; transplant July",
        "harvest": "October to November",
        "rainfall_mm": "800+ or assured irrigation",
        "temperature_c": "22-35",
        "seed_rate_kg_ha": 35.0,
        "spacing": "20 x 15 cm",
        "irrigation": "Assured water required; alternate wetting can save water",
        "common_issues": "Stem borer, blast, brown plant hopper",
        "best_practices": "Grow only where water is assured; use level fields and avoid excess nitrogen.",
        "market_use": "Rice grain, straw",
    },
    {
        "crop": "Berseem",
        "hindi": "बरसीम",
        "type": "Fodder",
        "season": "Rabi",
        "zones": ["Irrigated Canal", "Eastern Plains"],
        "districts": "Jaipur, Alwar, Bharatpur, Sri Ganganagar, Hanumangarh",
        "soil": "Fertile loam to clay loam",
        "water_need": "High",
        "drought_fit": "Low",
        "duration_days": 150,
        "sowing": "October to November",
        "harvest": "Multiple cuts from December to March",
        "rainfall_mm": "Irrigated fodder crop",
        "temperature_c": "15-25",
        "seed_rate_kg_ha": 25.0,
        "spacing": "Broadcast or close rows",
        "irrigation": "Regular irrigation after each cut",
        "common_issues": "Stem rot, aphid, weed competition",
        "best_practices": "Mix with oats if needed, irrigate after cutting, cut at proper height.",
        "market_use": "Green fodder, dairy animal feed",
    },
    {
        "crop": "Lucerne",
        "hindi": "रिजका",
        "type": "Fodder",
        "season": "Rabi / Perennial",
        "zones": ["Semi-arid Central", "Arid West", "Eastern Plains"],
        "districts": "Jodhpur, Pali, Nagaur, Jaipur, Ajmer",
        "soil": "Well-drained loam, alkaline-tolerant fields",
        "water_need": "Medium",
        "drought_fit": "Good",
        "duration_days": 240,
        "sowing": "October to November",
        "harvest": "Multiple cuts across season",
        "rainfall_mm": "Irrigation supported",
        "temperature_c": "15-32",
        "seed_rate_kg_ha": 20.0,
        "spacing": "Close rows or broadcast",
        "irrigation": "Irrigate after cutting; deep roots help later",
        "common_issues": "Aphid, weed competition, root rot",
        "best_practices": "Good dairy fodder; avoid waterlogging and maintain cutting interval.",
        "market_use": "Green fodder, hay",
    },
    {
        "crop": "Taramira",
        "hindi": "तारामीरा",
        "type": "Oilseed",
        "season": "Rabi",
        "zones": ["Arid West", "Shekhawati", "Semi-arid Central"],
        "districts": "Alwar, Jaipur, Sikar, Nagaur, Churu, Bikaner",
        "soil": "Sandy loam, poor fertility dryland soil",
        "water_need": "Low",
        "drought_fit": "Excellent",
        "duration_days": 100,
        "sowing": "October to November",
        "harvest": "February to March",
        "rainfall_mm": "200-350",
        "temperature_c": "18-28",
        "seed_rate_kg_ha": 5.0,
        "spacing": "30 cm rows",
        "irrigation": "Dryland crop; one irrigation can help if available",
        "common_issues": "Aphid, alternaria blight",
        "best_practices": "Useful for low-input dryland fields; avoid late sowing.",
        "market_use": "Oilseed, oilcake",
    },
    {
        "crop": "Oats",
        "hindi": "जई",
        "type": "Fodder",
        "season": "Rabi",
        "zones": ["Eastern Plains", "Irrigated Canal", "Hadoti"],
        "districts": "Jaipur, Alwar, Bharatpur, Kota, Sri Ganganagar, Hanumangarh",
        "soil": "Fertile loam",
        "water_need": "Medium",
        "drought_fit": "Medium",
        "duration_days": 100,
        "sowing": "October to November",
        "harvest": "First cut 55-60 days after sowing",
        "rainfall_mm": "Irrigation supported",
        "temperature_c": "12-25",
        "seed_rate_kg_ha": 80.0,
        "spacing": "Broadcast or 25 cm rows",
        "irrigation": "Irrigate after cutting",
        "common_issues": "Leaf rust, aphid, lodging",
        "best_practices": "Good winter fodder; combine with berseem for dairy systems.",
        "market_use": "Green fodder, hay",
    },
    {
        "crop": "Cluster Bean Vegetable",
        "hindi": "ग्वार फली",
        "type": "Vegetable",
        "season": "Kharif / Summer",
        "zones": ["Arid West", "Semi-arid Central", "Eastern Plains"],
        "districts": "Jodhpur, Jaipur, Ajmer, Nagaur, Pali, Alwar",
        "soil": "Sandy loam, well-drained soil",
        "water_need": "Low",
        "drought_fit": "Excellent",
        "duration_days": 60,
        "sowing": "February-March or June-July",
        "harvest": "Tender pods 45-60 days after sowing",
        "rainfall_mm": "250-450 or light irrigation",
        "temperature_c": "25-35",
        "seed_rate_kg_ha": 25.0,
        "spacing": "45 x 15 cm",
        "irrigation": "Light irrigation for tender pods",
        "common_issues": "Aphid, powdery mildew, bacterial blight",
        "best_practices": "Pick pods frequently and keep plants healthy for continuous harvest.",
        "market_use": "Fresh vegetable, local market",
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
    df = pd.DataFrame(RAJASTHAN_CROPS)
    df["zone_text"] = df["zones"].apply(lambda items: ", ".join(items))
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
        + df["zone_text"]
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

    crop_row = df[df["crop"] == selected_crop].iloc[0]
    hectare = area_to_hectare(area, unit)
    seed_required = hectare * float(crop_row["seed_rate_kg_ha"])

    st.success(
        f"For {area:g} {unit} of {selected_crop}, approximate seed need is {seed_required:.1f} kg. "
        f"Use local recommended variety and seed rate before purchase."
    )


def show_data_table(df: pd.DataFrame) -> None:
    st.subheader("Full Crop Data")
    export_df = df.drop(columns=["search_blob"]).copy()
    export_df["zones"] = export_df["zones"].apply(", ".join)
    st.dataframe(export_df, use_container_width=True, hide_index=True)

    st.download_button(
        "Download crop data as CSV",
        data=export_df.to_csv(index=False).encode("utf-8"),
        file_name="rajasthan_rural_crop_data.csv",
        mime="text/csv",
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
