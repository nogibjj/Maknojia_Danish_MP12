
# Maknojia_Danish_MP12

[![Build and Push Docker Image](https://github.com/nogibjj/Maknojia_Danish_MP12/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Maknojia_Danish_MP12/actions/workflows/cicd.yml)

This is a simple Python Flask application containerized using Docker. It demonstrates dynamic routes, JSON responses, and query parameter processing. The project includes a CI/CD pipeline to build and push the Docker image to Docker Hub.

---

## Features

- **Dynamic Routes**: Example route to greet users by name.
- **JSON Responses**: An API endpoint that returns JSON data.
- **Query Parameters**: Process form data to perform arithmetic operations.
- **Dockerized**: Run the application in a containerized environment.
- **CI/CD Support**: Build and push the Docker image to Docker Hub.

---

## Project Structure

- **`app.py`**: Main Flask application file.
- **`Dockerfile`**: Configuration for containerizing the application.
- **`Makefile`**: Automates Docker commands for building, running, cleaning, and pushing the image.

---

## Prerequisites

- Python 3.9+
- Docker
- Make

---

## Usage

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Build the Docker Image
```bash
make build
```

### 3. Run the Application
```bash
make run
```
Access the app in your browser at [http://localhost:5005](http://localhost:5005).

### 4. Push to Docker Hub
Ensure you are logged into Docker:
```bash
make login
```
Then push the image:
```bash
make push
```

### 5. Cleanup Docker
To stop and remove containers and images:
```bash
make clean
```

### 6. Show Docker Images and Containers
To list images:
```bash
make image_show
```

To list running containers:
```bash
make container_show
```

---

## Endpoints

### Home Page
**Route**: `/`  
**Method**: `GET`  
**Description**: Displays the home page.

### Greet User
**Route**: `/greet/<name>`  
**Method**: `GET`  
**Description**: Displays a greeting page for the user.

### API Info
**Route**: `/api/info`  
**Method**: `GET`  
**Description**: Returns application metadata in JSON format.

### Calculate
**Route**: `/calculate`  
**Method**: `POST`  
**Description**: Performs basic arithmetic operations (add, subtract, multiply, divide).

---

## Docker Hub Details

- **Docker Image Name**: `cinnamondanish/de_dockerdemo_2`
- **Tag**: `latest`

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
