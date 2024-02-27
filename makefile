install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
run: 
	python app.py 
		streamlit run app.py
		