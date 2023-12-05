#  Deployment REACT API
## Overview

This Flask-based web application provides a secure interface for deploying updates and checking the status of the Financio server. It uses Python for backend development and ensures security through password-based authentication.
## Features

- Deployment Endpoint: Securely run deployment scripts with password authentication.
- Status Check Endpoint: Retrieve server status, including nginx, CPU, and RAM usage, with password protection.

## Requirements

- Python 3.x
- Flask
- Access to the server where the application is hosted.

## Installation

1. Clone the repository to your local machine/server.
2. Install Flask: pip install Flask
3. Place your API password in api_password.txt in the root directory.
4. Copy the provided apiForDeploy.service file to /etc/systemd/system/.

## Systemd Service Setup

To run the API as a service:

1. Copy the named apiForDeploy.service to the /etc/systemd/system/ directory.
2. Enable the service: `sudo systemctl enable apiForDeploy`
3. Start the service: `sudo systemctl start apiForDeploy`
4. Check the service status: `sudo systemctl status apiForDeploy`

## Permissions

- Make sure to `chmod +x` the python script and bash scripts
- Also add permissions `chmod +r` (or `chmod 600` if you have multiple users)
