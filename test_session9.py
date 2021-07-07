from session9 import *
from datetime import datetime
import pytest
from io import StringIO 
import sys
import time
import inspect
import os
import session9
import re
import math

def test_profilestats__namedtuple():
    assert bool(session9.profilestats__namedtuple()), 'no value true returned something is wrong'

def test_profilestats__namedtuple_docsrting():
    summaryprofilenamedtup = session9.profilestats__namedtuple()
    assert bool(summaryprofilenamedtup.__doc__), 'no docstring for named tuple  something is wrong'
def test_meancurrentlocation():
    summaryprofilenamedtup = session9.profilestats__namedtuple()
    assert str(type(summaryprofilenamedtup.meancurrentlocation)).__contains__('tuple'), "mean location needs to be a tuple"

def test_allvalues():
    summaryprofilenamedtup = session9.profilestats__namedtuple()
    assert bool(summaryprofilenamedtup.meancurrentlocation), "no value for mean current location"
    assert bool(summaryprofilenamedtup.averageage), "no value for average age"
    assert bool(summaryprofilenamedtup.largestbloodtype), "no value for largest blood type"
    assert bool(summaryprofilenamedtup.oldestpersonage), "no value for oldest person age"
    

def test_oldestage():
    summaryprofilenamedtup = session9.profilestats__namedtuple()
    assert summaryprofilenamedtup.averageage <= summaryprofilenamedtup.oldestpersonage, "average age cannot be more than oldest age"

def test_profilestats__dict():
    assert bool(session9.profilestats__dict()), 'no value true returned something is wrong'


def test_meancurrentlocation_dict():
    summaryprofilenameddict = session9.profilestats__dict()
    assert str(type(summaryprofilenameddict["meancurrentlocation"])).__contains__('tuple'), "mean location needs to be a tuple"

def test_allvalues_dict():
    summaryprofilenameddict = session9.profilestats__dict()
    assert bool(summaryprofilenameddict["meancurrentlocation"]), "no value for mean current location"
    assert bool(summaryprofilenameddict["averageage"]), "no value for average age"
    assert bool(summaryprofilenameddict["largestbloodtype"]), "no value for largest blood type"
    assert bool(summaryprofilenameddict["oldestpersonage"]), "no value for oldest person age"
    

def test_oldestage_dict():
    summaryprofilenameddict = session9.profilestats__dict()
    assert summaryprofilenameddict["averageage"] <= summaryprofilenameddict["oldestpersonage"], "average age cannot be more than oldest age"

def test_dict():
    summaryprofilenameddict = session9.profilestats__dict()
    assert str(type(summaryprofilenameddict)).__contains__('dict'), "should return a dictionary"

def test_chem100index():
    assert bool(session9.chem100index()), 'no value true returned something is wrong'

def test_chem100niftydaydata():
    assert bool(session9.chem100niftydaydata()), 'no value true returned something is wrong'

def test_chem100index_high_check():
    Chem100index = session9.chem100index()
    assert Chem100index.high >= Chem100index.close , "close cannot be greater than high value"
    assert Chem100index.high >= Chem100index.open , "open cannot be greater than high value"

def test_chem100index_reasonable():
    Chem100index = session9.chem100index()
    assert math.isclose(Chem100index.high,Chem100index.close,abs_tol=500), "close cannot be greater than high value"
    #assert Chem100index.high >= Chem100index.open , "open cannot be greater than high value"

def test_def_chem100niftydaydata():
    assert bool(session9.chem100niftydaydata()), 'no value true returned something is wrong'

def test_chem100index_allvalues():
    Chem100index = session9.chem100index()
    assert bool(Chem100index.high), "no value for high"
    assert bool(Chem100index.open), "no value for open"
    assert bool(Chem100index.close), "no value for close"

def test_chem100niftydaydata_allvalues():
    chem100niftydaydata = session9.chem100niftydaydata()
    assert bool(chem100niftydaydata[0].compname), "no value for compname"
    assert bool(chem100niftydaydata[0].marketcap), "no value for marketcap"
    assert bool(chem100niftydaydata[0].date1), "no value for date1"
    assert bool(chem100niftydaydata[0].scrip), "no value for scrip"
    assert bool(chem100niftydaydata[0].open), "no value for open"
    assert bool(chem100niftydaydata[0].close), "no value for close"
    assert bool(chem100niftydaydata[0].high), "no value for high"

def test_chem100index_docstring():
    chem100index = session9.chem100index()
    assert bool(chem100index.__doc__), 'no docstring for named tuple  something is wrong'
    assert bool(chem100index.high.__doc__), 'no docstring for named tuple  something is wrong'
    assert bool(chem100index.open.__doc__), 'no docstring for named tuple  something is wrong'
    assert bool(chem100index.close.__doc__), 'no docstring for named tuple  something is wrong'

def test_chem100niftydaydata_docstring():
    chem100niftydaydata = session9.chem100niftydaydata()
    assert bool(chem100niftydaydata[0].__doc__), 'no docstring for named tuple  something is wrong'

def test_chem100niftydaydata_highlow_verify():
    chem100niftydaydata = session9.chem100niftydaydata()
    assert chem100niftydaydata[0].open <= chem100niftydaydata[0].high, "high must the highest value in a day"
if __name__ == '__main__':
    test_profilestats__namedtuple()