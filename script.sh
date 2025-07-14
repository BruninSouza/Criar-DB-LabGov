python3 -m venv venv
source venv/bin/activate
pip install pandas
pip install openpyxl
for f in codigos/*.py; do python3 "$f"; done