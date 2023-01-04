echo "Build Start"
python -m pip install -r requirements.txt
python3 -m manage.py collectstatic --noinput --clear
echo "Build Done"