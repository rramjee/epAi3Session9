# Assignment 10

To understand significance of NamedTuple and it's usage. As part of this assignment we have to write 3 functions
1. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, and average age 
2. Do the same as point 1 but using Dictionary. Also prove that namedtuple is faster
3. Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value the stock market started at, what was the highest value during the day, and where did it end. Make sure your open, high, close are not totally random



## Function 1 - profilestats__namedtuple: 

1. Using Faker to create profiles of 10000 people with following information and each of the reocords stored as Named Tuple within a list.
2. Once 10000 named tuples are loaded in a list, calculate blood type, mean-current_location, oldest_person_age, and average age and store it in a new named tuple	
3. print the values in new named tuple

## Function 2 - profilestats__dict: 

1. Using Faker to create profiles of 10000 people with following information and each of the reocords stored as Dictionary within a list.
2. Once 10000 dictionary are loaded in a list, calculate blood type, mean-current_location, oldest_person_age, and average age and store it in a ne Dictionary	
3. print the values in new Dictionary

## chem100niftydaydata function using namedtuple :

1. This function is used to generate stock market data of 100 companies for a particular day using a namedtuple

a. compname - From faker
b. market cap - round(random.uniform(1,100),2)
c. date - today's date
d. scrip - first 3 characters from compname
e. open - any value between 100 and 3000 --round(random.uniform(100,3000),2)
f. high - any value higher than open price be 1 to 5 % (open + (open * random.randint(1,5))/100)
g. close - any value lower than high price  (high - (high * random.randint(-5,1))/100)


## chem100index function :

1. get the stock market data of 100 companies by calling chem100niftydaydata.
2. calculate weightage for individual companies using marketcap/totalmarketcap
3. using following formula to calculate index open high and close.
	Chem100index.open = round(sum([x.open*(x.marketcap/totalmarketvalue) for x in chem100list]),2)
	Chem100index.high = round(sum([x.high*(x.marketcap/totalmarketvalue) for x in chem100list]),2)
	Chem100index.close = round(sum([x.close*(x.marketcap/totalmarketvalue) for x in chem100list]),2)