import requests
import json

scoring_uri = 'http://7db9cffc-8915-4fab-8e4e-d16f7307818e.southcentralus.azurecontainer.io/score'
key = 'hW3hhqlSvZx0hbNRBgMW4UMyoUYajn3v'

data = {
    "data":
    [
        {
            'age': "0",
            'job': "example_value",
            'marital': "example_value",
            'education': "example_value",
            'default': "example_value",
            'housing': "example_value",
            'loan': "example_value",
            'contact': "example_value",
            'month': "example_value",
            'day_of_week': "example_value",
            'duration': "0",
            'campaign': "0",
            'pdays': "0",
            'previous': "0",
            'poutcome': "example_value",
            'emp.var.rate': "0",
            'cons.price.idx': "0",
            'cons.conf.idx': "0",
            'euribor3m': "0",
            'nr.employed': "0",
        },
        {
            'age': "17",
            'campaign': "1",
            'cons.conf.idx': "-46.2",
            'cons.price.idx': "92.893",
            'contact': "cellular",
            'day_of_week': "mon",
            'default': "no",
            'duration': "971",
            'education': "university.degree",
            'emp.var.rate': "-1.8",
            'euribor3m': "1.299",
            'housing': "yes",
            'job': "blue-collar",
            'loan': "yes",
            'marital': "married",
            'month': "may",
            'nr.employed': "5099.1",
            'pdays': "999",
            'poutcome': "failure",
            'previous': "1"
          },
          {
            "age": "87",
            "campaign": "1",
            "cons.conf.idx": "-46.2",
            "cons.price.idx": "92.893",
            "contact": "cellular",
            "day_of_week": "mon",
            "default": "no",
            "duration": "471",
            "education": "university.degree",
            "emp.var.rate": "-1.8",
            "euribor3m": "1.299",
            "housing": "yes",
            "job": "blue-collar",
            "loan": "yes",
            "marital": "married",
            "month": "may",
            "nr.employed": "5099.1",
            "pdays": "999",
            "poutcome": "failure",
            "previous": "1"
          }
    ],
}

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
