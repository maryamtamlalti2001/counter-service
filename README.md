# Counter-service

![image](https://github.com/user-attachments/assets/b19e20b6-6522-4928-93e0-dd8236098523)
## Project Goals

The objective of this project is to develop a web service called `counter-service` and create a CI/CD for this Python service using GitHub Actions and AWS. Here is the main goals:

- Maintains a counter for the number of POST requests it has served.
- Returns the counter value for every GET request.
- Is built into a Docker image and deployed as a Docker container to an EC2 instance.
- Passes CI/CD checks and ends up as a running Docker container on the EC2 instance with minimal downtime during re-deployment.
- Includes security and quality tests using snyk and sonarcloud as part of the CI/CD pipeline to ensure code robustness and security.

## Features

- **GET `/`**: Returns the current counter value and a CSRF token.
- **POST `/`**: Increments the counter and returns the updated counter value.
- **GET `/health`**: Checks the health of the service to ensure it's running properly.

## Prerequisites

- Python 3.x
- Flask
- Flask-WTF
- Docker
- AWS CLI (for deployment)
- AWS EC2 instance
- Snyk
- Sonarcloud
- 
1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/counter-service.git
   cd counter-service
