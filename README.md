# ✈️ Agentic AI-Based Travel Planning Assistant

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red.svg)
![Claude AI](https://img.shields.io/badge/Claude-AI-purple.svg)

> An intelligent, AI-powered travel planning system that autonomously creates personalized trip itineraries using LangChain agents, Claude AI, and real-time data integration.

---

## 📋 Table of Contents
- [Problem Statement](#problem-statement)
- [Business Use Cases](#business-use-cases)
- [Project Objectives](#project-objectives)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [How to Run](#how-to-run)
- [Usage Guide](#usage-guide)
- [Architecture](#architecture)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)

---

## 🎯 Problem Statement

Planning a trip requires choosing flights, hotels, and attractions while considering time, budget, weather, distance, and personal preferences. Travelers often:
- Switch between multiple websites
- Compare inconsistent information
- Manually build itineraries that may be inefficient or unrealistic
- Struggle with real-time information and optimization

**Solution:** An intelligent, automated system that handles real-time information, reasons like a travel expert, and provides optimized itineraries tailored to user preferences.

---

## 💼 Business Use Cases

This AI Travel Agent can benefit:
- **Travel Agencies** - Automate itinerary design
- **Hotel Platforms** - Personalized recommendations
- **Airline Aggregators** - Smart flight suggestions
- **Tourism Companies** - Reduce customer support workload

**Benefits:**
- ✅ Reduce customer support workload
- ✅ Provide personalized recommendations
- ✅ Automate itinerary design
- ✅ Improve customer satisfaction
- ✅ Save users time and money

Companies like **MakeMyTrip**, **Booking.com**, **ClearTrip**, and **Ixigo** are adopting similar AI-driven solutions.

---

## 🎯 Project Objectives

### Primary Objectives
1. ✅ Build an agentic AI system using LangChain with autonomous decision-making
2. ✅ Integrate tools for:
   - Flight search (JSON dataset)
   - Hotel suggestions (JSON dataset)
   - Places/POIs discovery (JSON dataset)
   - Real-time weather (Open-Meteo API)
3. ✅ Enable multi-step reasoning and decision-making (ReAct agents)
4. ✅ Generate structured itineraries with:
   - Day-wise plan
   - Accommodation recommendations
   - Weather forecasts
   - Budget estimation

### Secondary Objectives
5. ✅ Implement filtering, ranking, and optimization
6. ✅ System can justify decisions with AI reasoning
7. ✅ Clean JSON + human-readable outputs
8. ✅ Beautiful, interactive Streamlit interface

---

## ✨ Features

### 🌍 **NEW! Global Destination Support**
> **Plan trips to ANY location worldwide!**  
> The app now uses **AI-powered dynamic data generation** when cities are not in the database. Whether you're traveling from Nanded to Pune, Delhi to Dubai, or Mumbai to New York - the app automatically generates realistic flight, hotel, and attraction data for you!  
> 📖 **[Learn more about Global Support →](GLOBAL_SUPPORT.md)**

### 🤖 AI-Powered Features
- **Intelligent Trip Planning** - Claude AI analyzes preferences and creates optimal itineraries
- **Multi-Tool Reasoning** - Agent autonomously decides which tools to use
- **Personalized Recommendations** - Hotels, flights, and attractions tailored to your needs
- **AI Insights** - Explains reasoning behind each recommendation
- **Dynamic Data Generation** - Works for ANY city, even if not in database

### 🗺️ Interactive Features
- **Live Weather Integration** - Real-time forecasts using Open-Meteo API
- **Interactive Map** - Visual route display with markers and flight paths
- **Clickable Locations** - Direct Google Maps links for hotels and attractions
- **Weather Charts** - Beautiful Plotly visualizations

### 📊 Smart Tools
- **Budget Breakdown** - Detailed cost analysis (flights, hotels, food, local transport)
- **Smart Packing Checklist** - Weather-based packing recommendations
- **Food Recommendations** - Location-specific cuisine suggestions
- **Transportation Guide** - Local transport options and tips
- **Travel Tips & Safety** - Expert advice for safe travel

### 🎨 Premium UI/UX
- **Animated Gradient Backgrounds** - Eye-catching visuals
- **Glassmorphism Cards** - Modern, frosted glass effects
- **Smooth Animations** - Float, pulse, and glow effects
- **Responsive Design** - Works on all screen sizes
- **Custom Scrollbar** - Gradient-themed scrolling

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.9+** | Core programming language |
| **LangChain** | Agentic AI framework |
| **Claude AI (Anthropic)** | Large Language Model |
| **Streamlit** | Web application framework |
| **Folium** | Interactive maps |
| **Plotly** | Data visualization |
| **Open-Meteo API** | Real-time weather data |
| **JSON** | Data storage (flights, hotels, places) |

---

## 📁 Project Structure

```
Agentic_AI_Travel_Planner/
│
├── .venv/                      # Virtual environment
├── agent/
│   ├── __init__.py
│   ├── agent.py                # Main trip planning logic
│   ├── langchain_agent.py      # LangChain ReAct agent
│   └── langchain_tools.py      # LangChain tool definitions
│
├── data/
│   ├── flights.json            # Flight dataset
│   ├── hotels.json             # Hotel dataset
│   └── places.json             # Places/attractions dataset
│
├── tools/
│   ├── __init__.py
│   ├── flights.py              # Flight search tool
│   ├── hotels.py               # Hotel recommendation tool
│   ├── places.py               # Places discovery tool
│   ├── weather.py              # Weather API integration
│   └── budget.py               # Budget calculation tool
│
├── ui/
│   ├── app.py                  # Streamlit application
│   └── hero_banner.png         # Hero image
│
├── .env                        # Environment variables
├── .gitignore
├── README.md                   # This file
└── requirements.txt            # Python dependencies
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip package manager
- Anthropic API key (Claude AI)

### Step 1: Clone the Repository
```bash
git clone <your-repo-url>
cd Agentic_AI_Travel_Planner
```

### Step 2: Create Virtual Environment
```bash
python -m venv .venv
```

### Step 3: Activate Virtual Environment
**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install streamlit requests langchain-anthropic langgraph plotly folium streamlit-folium pillow python-dotenv
```

### Step 5: Set Up Environment Variables
Create a `.env` file in the root directory:
```env
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

**Get your API key from:** https://console.anthropic.com/

---

## ▶️ How to Run

### Option 1: Using Command Line
```bash
# Activate virtual environment
.venv\Scripts\activate

# Set API key (Windows PowerShell)
$env:ANTHROPIC_API_KEY='your_api_key_here'

# Run the application
streamlit run ui/app.py
```

### Option 2: Direct Run
```bash
streamlit run ui/app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 📖 Usage Guide

### Planning Your Trip

1. **Enter Trip Details**
   - From City (e.g., Delhi)
   - Destination City (e.g., Goa)
   - Trip Duration (1-7 days)

2. **Click "Generate My Dream Trip"**
   - AI analyzes your request
   - Tools are called autonomously
   - Itinerary is generated

3. **Review Your Plan**
   - AI reasoning and insights
   - Flight details
   - Hotel recommendations
   - Weather forecast (chart + map)
   - Day-wise itinerary
   - Budget breakdown
   - Travel route map

4. **Interactive Features**
   - Click on hotels → Opens Google Maps
   - Click on places → Opens Google Maps
   - Explore the route on interactive map
   - Check packing checklist
   - View food recommendations
   - Read travel tips

---

## 🏗️ Architecture

### Agent Workflow

```
User Input → LangChain Agent → Tool Selection
                ↓
    ┌───────────┴───────────┐
    ↓           ↓           ↓
Flight Tool  Hotel Tool  Places Tool  Weather Tool  Budget Tool
    ↓           ↓           ↓           ↓             ↓
JSON Data   JSON Data   JSON Data   API Call    Calculations
    ↓           ↓           ↓           ↓             ↓
    └───────────┬───────────┘           │             │
                ↓                       │             │
        Agent Reasoning ←───────────────┴─────────────┘
                ↓
        Structured Output
                ↓
        Streamlit UI Display
```

### Tool Descriptions

1. **Flight Search Tool**
   - Reads `flights.json`
   - Filters by source and destination
   - Returns cheapest/fastest options

2. **Hotel Recommendation Tool**
   - Reads `hotels.json`
   - Filters by city, rating, amenities
   - Ranks by stars and price

3. **Places Discovery Tool**
   - Reads `places.json`
   - Recommends attractions by type and rating
   - Distributes across days

4. **Weather Lookup Tool**
   - Calls Open-Meteo API
   - Provides 7-day forecast
   - Returns temperature data

5. **Budget Estimation Tool**
   - Calculates total cost
   - Flight + Hotel + Food + Local expenses
   - Returns detailed breakdown

---

## 📸 Screenshots

### Main Interface
- Hero banner with tropical travel imagery
- Glassmorphism input cards
- Animated gradient background

### Trip Results
- AI reasoning insights
- Flight and hotel cards with clickable links
- Interactive weather chart
- Route map with markers
- Day-wise itinerary with icons
- Budget breakdown

### Additional Features
- Smart packing checklist
- Location-specific food recommendations
- Transportation guide
- Travel tips and safety
- Climate information

---

## 🔮 Future Enhancements

### Planned Features
- [ ] Multi-city trip support
- [ ] Flight booking integration
- [ ] Hotel booking integration
- [ ] User accounts and saved trips
- [ ] Trip sharing functionality
- [ ] PDF itinerary download
- [ ] Email itinerary feature
- [ ] Currency conversion
- [ ] Multi-language support
- [ ] Mobile app version

### Advanced AI Features
- [ ] Image recommendations for places
- [ ] Restaurant recommendations
- [ ] Activity booking
- [ ] Real-time price alerts
- [ ] Collaborative trip planning
- [ ] Social travel recommendations

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is created for educational purposes.

---

## 👨‍💻 Author

**Pruthviraj Shyamrao Tarode**

---

## 🙏 Acknowledgments

- **LangChain** for the agentic AI framework
- **Anthropic** for Claude AI
- **Streamlit** for the web framework
- **Open-Meteo** for free weather API
- **Folium** for interactive maps

---

## 📞 Support

For questions or issues, please:
1. Check the documentation above
2. Review the code comments
3. Test with sample inputs
4. Verify API key is set correctly

---

## ✅ Project Completion Checklist

- [x] Problem statement addressed
- [x] Business use cases identified
- [x] All primary objectives completed
- [x] All secondary objectives completed
- [x] JSON datasets integrated
- [x] Weather API integrated
- [x] LangChain agent implemented
- [x] All 5 tools created
- [x] Streamlit UI developed
- [x] Code is modular and clean
- [x] Error handling implemented
- [x] Documentation complete
- [x] Interactive features added
- [x] Premium UI/UX design

---

**Built with ❤️ using Python • Streamlit • Claude AI • LangChain • Folium • Plotly**
