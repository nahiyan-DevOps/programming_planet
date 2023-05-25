sudo apt install python3-pip
echo "python3-pip installed"
sudo apt install python3-virtualenv
echo "python3-virtualenv installed"
virtualenv /opt/programming_planet/venv
echo "venv created"
source /opt/programming_planet/venv/bin/activate
echo "venv activated"
pip3 install -r /opt/programming_planet/requirements.txt
echo "requirements installed"
streamlit run /opt/programming_planet/app.py
echo "application running"