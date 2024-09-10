# Blockhouse Dashboard Application

## Overview

This project consists of a web application built with Next.js for the frontend and Django for the backend. The application features a dashboard with multiple charts (Candlestick, Line Chart, Bar Chart, and Pie Chart), with data retrieved from a Django API.

## Project Structure

- **Frontend**: Next.js application for rendering the charts.
- **Backend**: Django API providing data for the charts.

## Frontend: Next.js Setup

### Requirements

- Node.js (v14 or higher)
- npm or yarn

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Vineeth0502/next-dashboard.git
    cd next-dashboard
    ```

2. Install the dependencies:

    ```bash
    npm install
    ```

3. Start the development server:

    ```bash
    npm run dev
    ```

   The application will be available at [http://localhost:3000](http://localhost:3000).

### Charts Implementation

The dashboard page (`pages.jsx`) includes four types of charts:

- **Candlestick Chart**
- **Line Chart**
- **Bar Chart**
- **Pie Chart**

Data for these charts is fetched from the Django API and displayed using the `recharts` library.

## Backend: Django API Setup

### Requirements

- Python (v3.8 or higher)
- Django
- Django REST Framework

### Installation

1. Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install the dependencies:

    ```bash
    pip install django djangorestframework
    ```

3. Apply migrations and start the server:

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

   The API will be available at [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/).

### API Endpoints

The Django API provides the following endpoints:

- `/api/candlestick-data/` – Returns JSON data for the Candlestick chart.
- `/api/line-chart-data/` – Returns JSON data for the Line chart.
- `/api/bar-chart-data/` – Returns JSON data for the Bar chart.
- `/api/pie-chart-data/` – Returns JSON data for the Pie chart.

## Docker Setup

### Requirements

- Docker
- Docker Compose

### Running with Docker

1. Build and start the Docker containers:

    ```bash
    docker-compose up --build
    ```

   This command will build the Docker images and start the containers for both the frontend and backend.

2. The frontend (Next.js) will be available at [http://localhost:3000](http://localhost:3000), and the backend (Django API) will be available at [http://localhost:8000/api/](http://localhost:8000/api/).

### Docker Configuration

- **Dockerfile** (Frontend): Contains instructions for building the Next.js application.
- **Dockerfile** (Backend): Contains instructions for building the Django application.
- **docker-compose.yml**: Defines the services for both the frontend and backend, including their build contexts and ports.

### Example Docker Compose File

Here’s an example `docker-compose.yml` file to get you started:

```yaml
version: '3'

services:
  frontend:
    build:
      context: ./next-dashboard
    ports:
      - "3000:3000"
    depends_on:
      - backend

  backend:
    build:
      context: ./myproject
    ports:
      - "8000:8000"
