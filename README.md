E-cell Golden Task

Please not that it may take upto a minute to load the site, since its hosted on a free render server.


The scraper uses a apify to scrape data, which is converted to JSON and displayed on a web-based dashboard
deployment URL - https://e-cell-golden-task-5.onrender.com

To build, follow the steps-

1.clone the repo.

2.pip install -r requirements.txt

3.uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

4.Open your browser at http://127.0.0.1:8000

to change the Instagram handles,
change the dictionary elements in main.py to the desired ones.



