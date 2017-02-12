**Smart Crawler v1.0**

>Crawls e-commerce websites such as Amazon and Flipkart and extracts structured information

### Python Version
`2.7.10`


### Running locally
1. Clone the repo
2. Create a virtual environment (here is the [doc](http://docs.python-guide.org/en/latest/dev/virtualenvs/))
3. Activate the virtual environment
4. Just in case, I have also committed my virtual env (for Mac) if you want to activate it directly
5. Navigate to the root directory through terminal
   and execute `pip install requirements.txt`
6. Edit `run.py` and specify the `url` variable, give the path
   of first page of results to be extracted
7. You can specify the number of desired results in the `run.py` file (`Crawler(total_items_to_scrape=your_desired_number)`)
8. Run the `run.py` file, utf8 output in console, csv output in output/output.csv

### Magic

>Since the similar elements belong to the same header, we can easily use nlp to rename the headers

