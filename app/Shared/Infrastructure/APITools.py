import requests
from flask import current_app

class APITools:
    def __init__(self):
        pass
    
    def get(
        self,
        url: str,
        params: dict = None,
        headers: dict = None,
    ) -> requests.Response:        
        response = requests.get(
            current_app.config['HOST'] + url,
            params=params,
            headers=headers,
        )
        response.raise_for_status()
        return response

    def post(
        self,
        url: str,
        data: dict = None,
        json: dict = None,
        headers: dict = None
    ) -> requests.Response:
        response = requests.post(
            current_app.config['HOST'] + url,
            data=data,
            json=json,
            headers=headers
        )
        response.raise_for_status()
        return response
    
    def createExcelFromAPIResponse(
        self,
        data: dict,
        filename: str
    ) -> None:

        import pandas as pd

        df = pd.DataFrame(data)
        df.to_excel('.' + '/output/' + filename, index=False)