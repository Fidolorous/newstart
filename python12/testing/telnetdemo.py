import http.client

# Establish a connection to the server
conn = http.client.HTTPConnection('www.dr-chuck.com')

# Send an HTTP GET request
conn.request('GET', '/page1.htm')

# Get the response from the server
response = conn.getresponse()

# Print the status code and headers
print(response.status, response.reason)
print(response.getheaders())

# Print the response body
print(response.read().decode())

# Close the connection
conn.close()
