#!/bin/bash

# 1. Look up the Process ID (PID) utilizing port 8000
sudo lsof -t -i:8000

# 2. Kill that process directly to free up the port
sudo kill -9 $(sudo lsof -t -i:8000)