from collections import namedtuple, Counter
import random

from faker import Faker
from datetime import date, timedelta, datetime
from dateutil import relativedelta	
import time


# namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, and average age"
def profilestats__namedtuple():
	"""
	namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, and average age using faker
	"""
	fake = Faker()
	Profile = namedtuple('Profile', 'bloodgroup location birthdate')
	summaryprofile = namedtuple('summaryprofile', 'largestbloodtype meancurrentlocation oldestpersonage averageage')
	summaryprofile.__doc__ = "Named Tuple With Summary Statistics of Profile"
	summaryprofile.largestbloodtype.__doc__ = "Majority Blood Type"
	summaryprofile.meancurrentlocation.__doc__ = "Mean location of longitude and latitude co-ordinates"
	summaryprofile.oldestpersonage.__doc__ = "Oldest Age of a person in the profile"
	summaryprofile.averageage.__doc__ = "Average age of sample set"
	profilelist = []
	for i in range(10000):
		profiledata = Profile(fake.profile()["blood_group"], fake.profile()["current_location"], fake.profile()["birthdate"])	
		profilelist.append(profiledata)
	summaryprofile.largestbloodtype = max(Counter(elem.bloodgroup for elem in profilelist))
	meancurrentlocationx = (sum([x[0][0] for x in zip(elem.location for elem in profilelist)])/len(profilelist))
	meancurrentlocationy = (sum([x[0][1] for x in zip(elem.location for elem in profilelist)])/len(profilelist))
	summaryprofile.meancurrentlocation = (meancurrentlocationx,meancurrentlocationy)
	summaryprofile.oldestpersonage = max(abs(relativedelta.relativedelta(elem.birthdate,date.today())).years for elem in profilelist)
	summaryprofile.averageage = sum(abs(relativedelta.relativedelta(elem.birthdate,date.today())).years for elem in profilelist)/len(profilelist)
	return summaryprofile

# namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, and average age"
def profilestats__dict():
	"""
	dict, calculate the largest blood type, mean-current_location, oldest_person_age, and average age using faker
	"""
	fake = Faker()
	#Profile = namedtuple('Profile', 'bloodgroup location birthdate')
	#profile_dict = dict(bloodgroup=None,location=None, birthdate=None)
	summaryprofile_dict = dict(largestbloodtype=None,meancurrentlocation=None,oldestpersonage=None,averageage=None)
	profilelist = []
	for i in range(10000):
		profile_dict = {}
		profile_dict["bloodgroup"] = fake.profile()["blood_group"]
		profile_dict["location"] = fake.profile()["current_location"]
		profile_dict["birthdate"] = fake.profile()["birthdate"]
		profilelist.append(profile_dict)
	summaryprofile_dict["largestbloodtype"] = max(Counter(elem["bloodgroup"] for elem in profilelist))
	meancurrentlocationx = (sum([x[0][0] for x in zip(elem["location"] for elem in profilelist)])/len(profilelist))
	meancurrentlocationy = (sum([x[0][1] for x in zip(elem["location"] for elem in profilelist)])/len(profilelist))
	summaryprofile_dict["meancurrentlocation"] = (meancurrentlocationx,meancurrentlocationy)
	summaryprofile_dict["oldestpersonage"] = max(abs(relativedelta.relativedelta(elem["birthdate"],date.today())).years for elem in profilelist)
	summaryprofile_dict["averageage"] = sum(abs(relativedelta.relativedelta(elem["birthdate"],date.today())).years for elem in profilelist)/len(profilelist)
	return summaryprofile_dict

def chem100index():
	"""
	function that generates day open high and close index of chemical companies
	"""
	chem100list = chem100niftydaydata()
	Chem100index = namedtuple('Chem100index', 'open high close')
	#tock = namedtuple('Stock','compname marketcap date1 scrip open high close')
	Chem100index.__doc__ = "Represent the Chemical Index"
	Chem100index.open.__doc__ = "Open Value of the Index"
	Chem100index.high.__doc__ = "Highest Value of the Index"
	Chem100index.close.__doc__ = "Closing Value of the Index"

	totalmarketvalue = sum([x.marketcap for x in chem100list])

	Chem100index.open = round(sum([x.open*(x.marketcap/totalmarketvalue) for x in chem100list]),2)
	Chem100index.high = round(sum([x.high*(x.marketcap/totalmarketvalue) for x in chem100list]),2)
	Chem100index.close = round(sum([x.close*(x.marketcap/totalmarketvalue) for x in chem100list]),2)

	print(f"""chem100index Open Value: {Chem100index.open}""")
	print(f"""chem100index High Value: {Chem100index.high}""")
	print(f"""chem100index Close Value: {Chem100index.close}""")
	print(type(Chem100index))
	return Chem100index


def chem100niftydaydata():
	"""
	Stock Market Values of top 100 Chemical Companies in stock market
	"""
	fake = Faker()
	Stock = namedtuple('Stock','compname marketcap date1 scrip open high close')
	Stock.__doc__ = "Represent the stock values for a particalar day"
	Stock.compname.__doc__ = "company name"
	Stock.marketcap.__doc__ = "market value of the company in billion dollars"
	Stock.date1.__doc__ = "date"
	Stock.scrip.__doc__ = "stock scrip"
	Stock.open.__doc__ = "opening value of the day"
	Stock.high.__doc__ = "highest value during the day"
	Stock.close.__doc__ = "closing value of the day"
	chem100list = []
	for _ in range(100):
		compname= fake.company()
		marketcap = round(random.uniform(1,100),2)
		date1 = str(date.today())
		scrip = compname[0:3]
		open = round(random.uniform(100,3000),2)
		high = open + (open * random.randint(1,5))/100
		close = high + (high * random.randint(-5,0))/100
		stockparam = Stock(compname =compname,
					marketcap=marketcap,
					date1 = date,
					scrip= scrip,
					open=open,
					high=high,
					close=close
					)

		chem100list.append(stockparam)
	

	return chem100list
	#print(chem100list[])

if __name__ == '__main__':

	# start = time.perf_counter()
	summaryprofilenamedtup = profilestats__namedtuple()
	#print(type(summaryprofilenamedtup.meancurrentlocation))
	# end = time.perf_counter()
	# print("Total Time Taken for Named Tuple:" + str(end-start))
	# print(f"""Largest BloodType is :{summaryprofilenamedtup.largestbloodtype} Mean Current Location: {summaryprofilenamedtup.meancurrentlocation} Oldest Person Age: {summaryprofilenamedtup.oldestpersonage} Average Person Age: {summaryprofilenamedtup.averageage}""")
	# print(summaryprofilenamedtup.__doc__)
	# start_dict = time.perf_counter()
	# summaryprofiledict = profilestats__dict()
	# end_dict = time.perf_counter()
	# print("Total Time Taken for Dictionary:" + str(end_dict-start_dict))
	# print(f"""Largest BloodType is :{summaryprofiledict["largestbloodtype"]} Mean Current Location: {summaryprofiledict["meancurrentlocation"]} Oldest Person Age: {summaryprofiledict["oldestpersonage"]} Average Person Age: {summaryprofiledict["averageage"]}""")