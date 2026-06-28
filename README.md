# Live-Cricket-Event-Extractor
# 🏏 Cricket Event Extractor API

A FastAPI-based REST API that leverages Google's Gemini AI to extract important cricket match events from raw commentary and return them in a structured JSON format.

## 📌 Features

* Extracts key cricket events from commentary
* Identifies:

  * 🏏 Wickets
  * 💥 Boundaries (Fours & Sixes)
  * 🎯 Half-centuries
  * 💯 Centuries
* Returns clean JSON output
* Uses **Google Gemini 1.5 Flash** for Natural Language Processing
* Built with **FastAPI** for high-performance APIs

---

## 📂 Project Structure

```
Cricket-Event-Extractor/
│
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── README.md
```

---

## 🛠 Technologies Used

* Python 3.10+
* FastAPI
* Google Generative AI (Gemini)
* Pydantic
* JSON

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Cricket-Event-Extractor.git

cd Cricket-Event-Extractor
```

### 2. Create a Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Gemini API Key

Set your Gemini API key as an environment variable.

Windows

```bash
set GEMINI_API_KEY=YOUR_API_KEY
```

Linux/macOS

```bash
export GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶ Running the API

```bash
uvicorn main:app --reload
```

The server will start at

```
http://127.0.0.1:8000
```

Swagger documentation is available at

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoint

### POST `/extract-events`

Extracts significant cricket events from commentary.

### Request Body

```json
{
    "text": "18.4 Bumrah to Smith, OUT! Smith edges to slip. 18.5 Bumrah to Labuschagne, FOUR! Beautiful cover drive."
}
```

---

### Successful Response

```json
{
    "status": "success",
    "events": [
        {
            "over": "18.4",
            "event_type": "Wicket",
            "description": "Smith edges to slip."
        },
        {
            "over": "18.5",
            "event_type": "Boundary",
            "description": "Labuschagne hits a four."
        }
    ]
}
```

---

### Partial Success Response

If Gemini returns output that is not valid JSON:

```json
{
    "status": "partial_success",
    "raw_output": "..."
}
```

---

## ⚙ How It Works

1. Accepts raw cricket commentary through a REST API.
2. Sends the commentary to Google's Gemini 1.5 Flash model.
3. Gemini extracts important match events.
4. The response is cleaned and validated as JSON.
5. Returns structured event data to the client.

---

## 🧠 Prompt Used

The model is instructed to:

* Detect important cricket events
* Ignore irrelevant commentary
* Return only valid JSON
* Include:

  * over
  * event_type
  * description

---

## ❗ Error Handling

The API handles:

* Missing Gemini API Key
* Invalid JSON returned by Gemini
* Internal server exceptions

---

## 📋 Example Output

```json
[
    {
        "over": "12.3",
        "event_type": "Boundary",
        "description": "Kohli drives the ball through covers for four."
    },
    {
        "over": "16.5",
        "event_type": "Half Century",
        "description": "Kohli reaches his fifty."
    },
    {
        "over": "19.2",
        "event_type": "Wicket",
        "description": "Maxwell is caught at long-on."
    }
]
```

---

## 🚀 Future Improvements

* Support live match commentary streams
* Detect additional events (No Ball, Wide, Run Out, LBW, etc.)
* Player-wise event statistics
* Multi-language commentary support
* Database integration for storing extracted events
* Docker containerization
* Authentication and API security
* Unit and integration testing

---

## 👨‍💻 Author

**Samarth**

Artificial Intelligence & Machine Learning Engineering Student

