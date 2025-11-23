# WayneKok Docker Application

A simple web application built with Flask backend and Nginx frontend, containerized using Docker.


## Project Structure

```
.
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py 
├── frontend/
│   ├── nginx.conf
│   └── index.html
├── logs/
├── docker-compose.yml
└── README.md
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Build and Run with Docker Compose

```bash
docker compose up --build
```

This command will:
- Build the backend Docker image from `./backend`
- Pull the Nginx image
- Start both containers
- Mount necessary volumes

### 3. Access the Application

Once the containers are running, open your browser and navigate to:
```
http://localhost:8089
```
Log the access
```
curl http://localhost:8089/api/log
```

## Usage

### Running in Detached Mode

To run the containers in the background:
```bash
docker compose up -d
```

### Stopping the Application

```bash
docker compose down
```

### Viewing Logs

To view application logs:
```bash
# View all logs
docker compose logs

# View backend logs only
docker compose logs backend

# View frontend logs only
docker compose logs frontend

# Follow log output
docker compose logs -f
```


### Rebuilding After Changes

If you make changes to the code:
```bash
docker compose down
docker compose up --build
```



