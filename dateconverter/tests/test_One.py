import pytest
import requests

@pytest.fixture
def dataSetter_Fixture():
    url = 'http://127.0.0.1:8000/API/Date-retiver/'
    return url


@pytest.mark.parametrize("day,month,year,type",[(5,6,2001,'E'),(15,80,2022,'G'),(6,10,2022,'G'),(6,10,2012,'E')])
def test_checking_dateAcceptor(dataSetter_Fixture,day,month,year,type):
    
    currentUrl = dataSetter_Fixture + str(day)+'-'+str(month)+'-'+str(year)+'/'+type

    response = requests.get(currentUrl)
   
    assert response.status_code == 200

@pytest.mark.parametrize("day,month,year,type",[(5,6,2001,'E'),(15,80,2022,'G'),(6,10,2022,'G'),(6,10,2012,'E')])
def testing_the_actual_response(dataSetter_Fixture,day,month,year,type):
    currentUrl = dataSetter_Fixture + str(day)+'-'+str(month)+'-'+str(year)+'/'+type

    response = requests.get(currentUrl)
    length = 0
    try:
        response = response.json()
        length = len(response)
        print(response)
    except:
        pass

    assert  length == 3




    

    

