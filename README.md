# API Performance Monitor

## Overview

API Performance Monitor is a Flask-based web application that continuously monitors REST APIs and records their performance metrics. It measures response times, tracks HTTP status codes, logs failures, stores historical data in SQLite, and provides an interactive dashboard for monitoring API health.

The project is designed to demonstrate backend development, API integration, scheduling, database management, analytics, and monitoring concepts.

---

## Features

* Monitor multiple REST APIs
* Add, edit, and delete APIs through a web interface
* Configurable monitoring interval for each API
* Measure API response time
* Record HTTP status codes
* Detect request failures and exceptions
* Store monitoring history in SQLite
* Dashboard with monitoring statistics
* Recent monitoring history
* Interactive charts using Chart.js
* CSV report export
* Application logging
* REST API for analytics and monitoring data
* Auto-refresh dashboard

---

## Tech Stack

### Backend

* Python 3.12+
* Flask
* SQLAlchemy
* APScheduler
* Requests

### Database

* SQLite

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Chart.js

### Reporting

* Pandas (CSV Export)

### Logging

* Python Logging Module

---

## Project Structure

```text
api-performance-monitor/
│
├── app.py
├── config.py
├── scheduler.py
├── logger.py
├── requirements.txt
├── README.md
│
├── database/
│   ├── __init__.py
│   ├── db.py
│   └── models.py
│
├── monitor/
│   ├── __init__.py
│   ├── api_checker.py
│   ├── analytics.py
│   └── exporter.py
│
├── routes/
│   ├── __init__.py
│   └── api_routes.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── dashboard.js
│
├── logs/
│   └── app.log
│
├── exports/
│   └── metrics_report.csv
│
└── api_monitor.db
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/api-performance-monitor.git
cd api-performance-monitor
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

---

## Usage

### Add an API

Provide:

* API Name
* API URL
* HTTP Method
* Monitoring Interval

Example:

| Name       | URL                    |
| ---------- | ---------------------- |
| GitHub API | https://api.github.com |

---

## Dashboard

The dashboard displays:

* Total Requests
* Successful Requests
* Failed Requests
* Availability
* Registered APIs
* Recent Monitoring Results
* Response Time Trend
* Success vs Failed Chart

---

## REST API Endpoints

| Method | Endpoint          | Description                  |
| ------ | ----------------- | ---------------------------- |
| GET    | `/`               | Dashboard                    |
| GET    | `/apis`           | List APIs                    |
| POST   | `/apis`           | Add API                      |
| PUT    | `/apis/<id>`      | Update API                   |
| DELETE | `/apis/<id>`      | Delete API                   |
| GET    | `/summary`        | Monitoring summary           |
| GET    | `/metrics`        | Complete monitoring history  |
| GET    | `/recent-metrics` | Latest monitoring results    |
| GET    | `/chart-data`     | Data for charts              |
| GET    | `/export`         | Download CSV report          |
| GET    | `/logs`           | View recent application logs |

---

## Database Schema

### APIs Table

| Column       | Type     |
| ------------ | -------- |
| id           | Integer  |
| name         | String   |
| url          | String   |
| method       | String   |
| interval     | Integer  |
| created_at   | DateTime |
| last_checked | DateTime |

### Metrics Table

| Column        | Type     |
| ------------- | -------- |
| id            | Integer  |
| api_id        | Integer  |
| status_code   | Integer  |
| response_time | Float    |
| success       | Boolean  |
| error_message | Text     |
| checked_at    | DateTime |

---

## Logging

Application logs are stored in:

```text
logs/app.log
```

Logs include:

* API checks
* Response times
* Status codes
* Errors
* Exceptions

---

## CSV Export

Monitoring history can be exported as:

```text
exports/metrics_report.csv
```

---

## Future Enhancements

* Grafana Integration
* Email Alerts
* Authentication
* Docker Support
* PostgreSQL Support
* PDF Report Generation
* User Management
* Dark Mode
* API Health Notifications
* Deployment to Cloud

---

## Learning Outcomes

This project demonstrates:

* REST API Development
* Flask Web Framework
* Database Design
* SQLAlchemy ORM
* Background Scheduling
* API Performance Monitoring
* Exception Handling
* Logging
* Data Visualization
* Dashboard Development
* CSV Report Generation
* Software Architecture
