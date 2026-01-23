AWS Flask App

A simple Flask web application deployed on AWS EC2 with CI/CD automation via GitHub Actions.

---

Project Overview

This project demonstrates a full AWS DevOps workflow:

- Python Flask application (CRUD example)
- Docker containerization
- Automatic deployment to EC2 using GitHub Actions
- Basic monitoring and logging
- Designed for learning and showcasing AWS cloud and DevOps skills

---

Technologies Used

- Python 3.x
- Flask
- Docker
- AWS EC2
- GitHub Actions (CI/CD)
- Bash scripting for EC2 setup

---

Features

- Flask web application with a simple web page
- Automatic build and deployment to AWS EC2 using GitHub Actions
- Organized folder structure and requirements.txt
- Fully automated EC2 setup with ec2-setup.sh
- Demonstrates practical AWS DevOps concepts:
  - Continuous Integration / Continuous Deployment
  - Infrastructure as Code principles
  - Security Group configuration for controlled access

---

Architecture

GitHub Actions --> Docker build --> EC2 (Flask app)
                   │
                   └── Security Group for HTTP access

- GitHub Actions: Builds Docker image and deploys to EC2 on push to main branch
- EC2 Instance: Hosts the Flask application
- Security Group: Restricts access to HTTP (port 80)

(Optional: add a diagram image here for better visualization)

---

Getting Started

1. Clone the repository

git clone https://github.com/felicianogoncalves/aws-flask-app.git
cd aws-flask-app

2. Setup EC2 instance

- Launch EC2 with an Ubuntu AMI
- Run setup script:

bash ec2-setup.sh

- This will:
  - Install Python3, pip, Flask
  - Pull Docker container
  - Start Flask app

3. Access the App

- Open your browser and go to:

http://<your-ec2-public-ip>

---

Screenshots

(Add GIF or screenshots of the running app and GitHub Actions workflow here)

---

Why This Project

- Demonstrates real AWS cloud deployment
- Shows ability to create CI/CD pipelines
- Highlights automation, containerization, and cloud infrastructure management
- Ideal portfolio piece for DevOps or Cloud Engineer interviews

---

Links

- GitHub Repository: https://github.com/felicianogoncalves/aws-flask-app
- AWS Documentation: https://aws.amazon.com/documentation/

---

Notes

- Designed for learning and demonstration purposes
- Costs: Running an EC2 instance may incur AWS charges




