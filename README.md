# Italy Traffic Intelligence

Real-time traffic intelligence and analytics project based on publicly accessible Italian motorway traffic data.

The project collects, processes, analyzes, and visualizes traffic events using Python, Pandas, and Matplotlib.

Main goals:
- monitor traffic incidents
- analyze road event patterns
- aggregate structured traffic datasets
- generate analytical summaries and visual reports

---

## Technologies Used

- Python
- Pandas
- Requests
- JSON APIs
- Matplotlib
- CSV Data Pipelines

---

## Workflow

Traffic endpoint
↓
JSON data collection
↓
Data cleaning and normalization
↓
Aggregation with Pandas
↓
CSV exports
↓
Visualization and reporting

---

## Project Structure

```bash
italy-traffic-intelligence/
│
├── analyze_events.py
├── summarize_events.py
├── plot_events.py
├── inspect_endpoint.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── events_by_category.csv
│   ├── events_by_road.csv
│   ├── main_issue_by_road.csv
│   └── road_category_summary.csv
│
├── charts/
│   └── stacked_traffic_issues_horizontal.png
│
└── .env
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Environment Variables

```env
TRAFFIC_ENDPOINT=your_endpoint_here
```

---

## Run Pipeline

Download and process traffic events:

```bash
python3 analyze_events.py
```

Generate summaries:

```bash
python3 summarize_events.py
```

Create charts:

```bash
python3 plot_events.py
```

---

## Key Features

- Real-time traffic event collection
- Structured JSON processing
- Traffic issue aggregation
- CSV export pipelines
- Automated analytical summaries
- Traffic visualization dashboards

---

## Example Chart

![Traffic Dashboard](charts/stacked_traffic_issues_horizontal.png)

---

## Data Source

Traffic event data is collected from publicly accessible motorway traffic feeds and structured JSON endpoints used by Italian traffic information systems.

The project is intended for educational, analytical, and portfolio purposes only.

---

## Future Improvements

- Interactive dashboards
- Automated scheduled data collection
- Traffic anomaly detection
- Severity scoring system
- Geographic traffic mapping

---

## Author

Yurii Vasylenko