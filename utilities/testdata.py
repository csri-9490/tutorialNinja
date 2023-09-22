import pytest

class test_data:

    @pytest.fixture(params=[{"email": "reddy.csri@gmail.com", "Password": "Shivaya1@"},
                            {"email": "reddy.csri1@gmail.com", "Password": "Shivaya2@"}])
    def getData(self ,request):
        return request.param