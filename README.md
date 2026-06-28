# Live-Cricket-Event-Extractor
🏏 Cricket Event Extractor API

A FastAPI-based REST API that leverages Google's Gemini AI to extract important cricket match events from raw commentary and return them in a structured JSON format.

📌 Features
Extracts key cricket events from commentary
Identifies:
🏏 Wickets
💥 Boundaries (Fours & Sixes)
🎯 Half-centuries
💯 Centuries
Returns clean JSON output
Uses Google Gemini 1.5 Flash for Natural Language Processing
Built with FastAPI for high-performance APIs
📂 Project Structure
Cricket-Event-Extractor/
│
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── README.md
🛠 Technologies Used
Python 3.10+
FastAPI
Google Generative AI (Gemini)
Pydantic
JSON
📦 Installation
1. Clone the repository
git clone https://github.com/your-username/Cricket-Event-Extractor.git

cd Cricket-Event-Extractor
2. Create a Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

Linux / macOS

python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Gemini API Key

Set your Gemini API key as an environment variable.

Windows

set GEMINI_API_KEY=YOUR_API_KEY

Linux/macOS

export GEMINI_API_KEY=YOUR_API_KEY
