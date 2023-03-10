# Job programs
I am product owner, but sometimes I have to create programs which help our analyst at work.
We need to automate our work and also python helps me to calculate some measures faster than excel.

Bond_ctd: this program calculates which bond is the cheapest to deliver in contract future. It contains: downloading data from API, algorithm calculating CTD bond, inserting data in SQL. 
Benchmark: inserting data from different websites. I need to download data from different website so i prepare couple of algorithms to get these data. This program needs file 'idbenchmark.xlsx' where we see which data will be downloaded.
ETF duration: downloading data from API. We create API which download data from eurex and then i need to get duration of ETF to insert this in SQL.
Foreign_stock_informations: downloading data from API for instrument from sql. At first I need to get equity instruments from portfolio in SQL. Then I send a request to BDL using API to get data about number of votes. At the end I insert these data to SQL.
INSTR_PUBLICO: getting data from XML. We have a special file in XML extension. So i need to get data from this type of file and create another one XML with my data
Liability_issuers: getting data from excel. At first i prepare list of instruments/issuers, and then i try to download information about their emission. At the end i import these data to sql
