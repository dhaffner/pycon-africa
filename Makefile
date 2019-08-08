venv:
	python3 -mvenv venv
	./venv/bin/pip install -r requirements.txt
	echo "\nActivate your virtual environment by running 'source ./venv/bin/activate'"