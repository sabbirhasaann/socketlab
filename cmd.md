# Commands

1. .\.venv/Scripts/Activate.ps1
Activate the virtual environment on Windows PowerShell.

2. pip install -r requirements.txt

3. source .venv/bin/activate // activate virtual env in linux

4. generate secret key
    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
