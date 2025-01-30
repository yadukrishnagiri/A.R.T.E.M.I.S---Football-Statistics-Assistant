# A.R.T.E.M.I.S - Football Statistics Assistant

A.R.T.E.M.I.S (Advanced Real-Time Enhanced Match Information System) is an AI-powered football statistics assistant that provides comprehensive analysis and information about football matches, players, and teams.

## Features

- Real-time match statistics
- Team performance analysis
- Player statistics
- Historical data analysis
- Interactive web interface
- RAG (Retrieval Augmented Generation) based responses

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/artemis-football.git
cd artemis-football
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up the database:
```bash
python populate_database.py
```

4. Run the application:
```bash
python app.py
```

## Project Structure

```
artemis-football/
├── app.py                 # Main Flask application
├── get_embedding_function.py  # Embedding function for RAG
├── populate_database.py   # Database population script
├── query_data.py         # Data querying functions
├── test_rag.py           # RAG testing module
├── static/               # Static assets
│   └── team logos and backgrounds
│       
├── data/                 # CSV data files
│   ├── attacking.csv
│   ├── attempts.csv
│   ├── defending.csv
│   ├── disciplinary.csv
│   ├── goalkeeping.csv
│   └── key_stats.csv
└── templates/            # HTML templates
    ├── 404.html
    ├── ajax_stats.html
    ├── bayern_stats.html
    ├── club_stats.html
    ├── general_stats.html
    ├── index.html
    ├── liverpool_stats.html
    ├── man_u_stats.html
    └── real_stats.html
```

## Usage

1. Start the server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```


