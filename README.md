SKILLS DEMONSTRATED

- CI/CD pipeline using GitHub Actions
- Docker containerization of a Flask application
- Automated deployment on AWS EC2
- Secure access using IAM and GitHub Secrets
- Linux server configuration and troubleshooting
- Cloud networking (VPC, Security Groups, Internet Gateway)


AWS Flask App – CI/CD with Docker on EC2

This project demonstrates a complete end-to-end deployment of a Flask web application on AWS EC2 using Docker and GitHub Actions.

It covers application containerization, infrastructure provisioning, and automated deployment, following real-world DevOps practices.

----------------------------------------------------------------

ARCHITECTURE OVERVIEW

Developer
→ GitHub Repository
→ GitHub Actions (CI/CD)
→ AWS EC2 (Ubuntu)
→ Docker
→ Flask Application

----------------------------------------------------------------

KEY FEATURES

- Automated EC2 provisioning using AWS CLI
- Secure SSH access using AWS Key Pair and GitHub Secrets
- Dockerized Flask application
- Docker port mapping (80:5000)
- Fully automated deployment pipeline
- Publicly accessible web application via EC2 Public IP

----------------------------------------------------------------

TECH STACK

Cloud: AWS (EC2, IAM, Security Groups)
CI/CD: GitHub Actions
Containerization: Docker
Backend: Python, Flask
Operating System: Ubuntu Linux

----------------------------------------------------------------

FLASK APPLICATION

The Flask application runs inside a Docker container and listens on port 5000, following container best practices.

Application configuration:

app.run(host="0.0.0.0", port=5000)

Docker exposes the application externally via port 80:

docker run -d -p 80:5000 flask-app

This separation between application port and host port reflects real-world production setups.

----------------------------------------------------------------

CI/CD PIPELINE (GITHUB ACTIONS)

The GitHub Actions workflow performs the following steps:

1. Checkout source code
2. Configure AWS credentials securely using GitHub Secrets
3. Launch a new EC2 instance
4. Wait for the instance to become available
5. Install Docker on the EC2 instance
6. Copy project files to the instance via SCP
7. Build the Docker image on EC2
8. Run the Docker container automatically

This ensures a reproducible and automated deployment process.

----------------------------------------------------------------

SECURITY

- AWS credentials are stored securely using GitHub Secrets
- SSH access is managed through an AWS Key Pair
- Security Group allows inbound traffic on port 80 only
- No secrets or credentials are hardcoded in the repository

----------------------------------------------------------------

ACCESSING THE APPLICATION

After deployment, the application can be accessed via the EC2 public IP address:

http://<EC2_PUBLIC_IP>

----------------------------------------------------------------

LESSONS LEARNED

- Difference between container ports and host ports
- Docker networking and port mapping
- Debugging real CI/CD deployment issues
- Importance of consistent port configuration
- AWS networking fundamentals (VPC, Security Groups, Internet Gateway)
- Practical troubleshooting in cloud environments

----------------------------------------------------------------

FUTURE IMPROVEMENTS

- Use Elastic IP to avoid changing public IPs on redeploy
- Migrate deployment to ECS Fargate
- Add an Application Load Balancer
- Implement health check endpoints
- Infrastructure as Code using Terraform
- Improve deployment strategy to avoid recreating EC2 instances

----------------------------------------------------------------

REFERENCES

AWS EC2 Documentation
https://docs.aws.amazon.com/ec2/

AWS IAM Documentation
https://docs.aws.amazon.com/iam/

Docker Documentation
https://docs.docker.com/

Flask Documentation
https://flask.palletsprojects.com/

GitHub Actions Documentation
https://docs.github.com/en/actions

----------------------------------------------------------------

AUTHOR

Feliciano Gonçalves
Cloud / DevOps Engineer

GitHub
https://github.com/felicianogoncalves
