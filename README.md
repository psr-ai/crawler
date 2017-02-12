**Smart Crawler v1.0**

>Crawls e-commerce websites such as Amazon and Flipkart and extracts structured information

### Python Version
`2.7.10`


### Running locally
1. Clone the repo
2. Create a virtual environment (here is the [doc](http://docs.python-guide.org/en/latest/dev/virtualenvs/))
3. Activate the virtual environment
4. Navigate to the root directory through terminal
   and execute `pip install requirements.txt`
5. Edit `run.py` and specify the `url` variable, give the path
   of first page of results to be extracted
6. You can specify the number of desired results in the `run.py` file (`Crawler(total_items_to_scrape=your_desired_number)`)
7. Run the `run.py` file, it outputs as a csv file in output folder in root directory

