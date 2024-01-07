import requests

# Initialize an empty list to store the data
data_pack = []

# Example for loop (8 loops)
for i in range(8):
    # Build the data for each iteration
    data = {
        "date": "date-here2",
        "scaleId": i,
        "value": i * 2
    }
    
    # Append the data to the list
    data_pack.append(data)

# After the loop, print the entire data pack
print(data_pack)

# Define the URL to which you want to make the POST request
url = 'https://hook.make.com'

# Send the POST request with the data pack as JSON
response = requests.post(url, json=data_pack)

# Check the response status code
if response.status_code == 200:
    print('POST request was successful!')
    print('Response content:', response.text)
else:
    print(f'POST request failed with status code {response.status_code}')

