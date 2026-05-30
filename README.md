# Socket Lab

Learning WebSockets in Django Channels with synchronous and asynchronous consumers.

---

## Project Architecture Overview

This project uses **Django Channels** to handle real-time WebSocket connections alongside traditional HTTP traffic. 

* **HTTP Traffic:** Handled by Django's standard ASGI application layer.
* **WebSocket Traffic:** Routed via a centralized `routing.py` to separate synchronous and asynchronous consumers.

---

## 🛠️ Initial Project Setup

Follow these steps to initialize the environment and get the project running locally.

### 1. Prerequisites
Ensure you have the following installed on your system:
* **Python** (Developed using version `3.12.3`)


### 2. Virtual Environment Setup
Clone the repository, navigate to the project root, and spin up an isolated environment:

```bash
# Create the virtual environment
python -m venv .venv

# Activate the virtual environment
# Windows (Command Prompt/PowerShell):
.\.venv\Scripts\activate

# Ubuntu / macOS:
source .venv/bin/activate