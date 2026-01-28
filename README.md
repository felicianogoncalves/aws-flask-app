# AWS Flask App – Ephemeral CI/CD with Downtime Simulation & Rollback

This project demonstrates a **realistic DevOps workflow**: automated deployment, intentional failure, downtime observation, and recovery — all on ephemeral AWS infrastructure with zero residual cost.

Unlike typical "always-up" demos, this lab **intentionally simulates service failure** to validate rollback readiness and operational awareness.

----------------------------------------------------------------

## SKILLS DEMONSTRATED

- End-to-end CI/CD pipeline using GitHub Actions  
- Docker containerization of a Flask application  
- Ephemeral AWS EC2 provisioning and cleanup  
- Versioned deployments (Docker images tagged by Git commit)  
- Health check endpoint with version exposure  
- Simulated downtime and manual rollback  
- Secure secret management (GitHub Secrets + IAM)  
- Linux server automation and networking (Security Groups, SSH)

----------------------------------------------------------------

## ARCHITECTURE OVERVIEW

Developer  
→ GitHub Repository  
→ GitHub Actions (CI/CD)  
→ Temporary AWS EC2 (Ubuntu)  
→ Docker Container  
→ Flask Application (`/health` endpoint with version)

*All resources are automatically destroyed after execution.*

----------------------------------------------------------------

## KEY FEATURES

- ✅ **Ephemeral Infrastructure**: EC2 instance created and terminated within the same workflow  
- ✅ **Versioned Artifacts**: Docker image tagged with Git commit SHA (`flask-app:a1b2c3d`)  
- ✅ **Health Check**: `GET /health` returns `{"status": "ok", "version": "a1b2c3d"}`  
- ✅ **Downtime Simulation**: Service is stopped for 1 minute to observe failure  
- ✅ **Rollback Validation**: Same container is redeployed to restore service  
- ✅ **Zero Cost Residual**: No lingering resources after workflow completion  
- ✅ **Secure Automation**: No hardcoded credentials; all secrets via GitHub Secrets

----------------------------------------------------------------

## TECH STACK

- **Cloud**: AWS (EC2, IAM, Security Groups)  
- **CI/CD**: GitHub Actions  
- **Containerization**: Docker  
- **Backend**: Python, Flask  
- **OS**: Ubuntu Linux  
- **Networking**: Public IP, Port 80 → 5000 mapping

----------------------------------------------------------------

## DEPLOYMENT FLOW

1. Workflow triggered manually via GitHub Actions  
2. Temporary EC2 instance launched (`t2.micro`, Free Tier eligible)  
3. Docker installed and app deployed in a versioned container  
4. **1-minute window**: service live — test via `http://<IP>/health`  
5. **Container stopped** — service goes offline  
6. **1-minute downtime**: verify failure (e.g., `/health` unreachable)  
7. **Rollback**: same container re-created  
8. **1-minute recovery window**: confirm service restored  
9. EC2 instance **automatically terminated**

> This flow mirrors real-world incident response: detect → observe → recover.

----------------------------------------------------------------

## SECURITY

- AWS credentials stored in **GitHub Secrets**  
- SSH access via AWS Key Pair (private key never committed)  
- Security Group allows only:
  - Port 22 (SSH) from GitHub Actions IPs  
  - Port 80 (HTTP) from anywhere  
- No secrets in code or logs

----------------------------------------------------------------

## ACCESSING THE APPLICATION

During workflow execution, access the app at:  
`http://<EC2_PUBLIC_IP>`  
or the health endpoint:  
`http://<EC2_PUBLIC_IP>/health`

> ⏱️ You have ~3 minutes total to test (before auto-termination).

----------------------------------------------------------------

## LESSONS LEARNED

- Importance of **immutable, versioned artifacts** for reliable rollback  
- Value of **observable downtime** in testing recovery procedures  
- Why **ephemeral environments** reduce cost and drift  
- How **health checks** enable automation and monitoring  
- Practical debugging of CI/CD pipelines in cloud environments  
- Difference between *deployment* and *operational resilience*

----------------------------------------------------------------

## FUTURE IMPROVEMENTS

- Replace manual rollback with **automated health-check-triggered recovery**  
- Use **AWS ECS Fargate** to avoid EC2 management  
- Add **CloudWatch Alarms** for automatic detection  
- Implement **Infrastructure as Code (Terraform)**  
- Store Docker images in **ECR** instead of building on EC2  
- Add **unit/integration tests** in CI phase

----------------------------------------------------------------

## REFERENCES

- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)  
- [GitHub Actions](https://docs.github.com/en/actions)  
- [Docker Documentation](https://docs.docker.com/)  
- [Flask Documentation](https://flask.palletsprojects.com/)  

----------------------------------------------------------------

## AUTHOR

**Feliciano Gonçalves**  
Cloud / DevOps 
[GitHub](https://github.com/felicianogoncalves)
