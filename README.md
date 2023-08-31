## Project Architecture
File: `flask-sever.py`
This is the main Flask server code that will be listening on the port `5000`.

## Server in Express (Express Server):
File: `express-sever.js`
This is the main code for your Express server, running on port `5600`.
The WebSocket code on port `5800` has been included in the same File for ease of understanding. However, it is recommended to separate these functionalities into separate Files in the future.

## HTML Pages:
Files: `index.html` and `page2.html`
These are the HTML Files that are rendered by Flask.
  * `index.html`: This is the home page HTML File which contains a title and a subtitle. It also includes a JavaScript script, index.js, located in the Scripts folder, which handles WebSocket.
  * `page2.html`: This is the HTML File of page 2 that displays information received as parameters.

## Client JavaScript:
File: `index.js`
This is the JavaScript File for the `index.html` page that runs on the client to handle the WebSocket and redirection to `page2.html`.

## Request Code via POST:
File: flask-to-express.py
This is the Python code to make a POST request to the Express server

## Definition of routes
#### Route to Homepage:
We define a route to the home page that renders the `index.html` template.

#### Route to Get Employees:
We define a route that returns a JSON containing employee information.

#### Dynamic Route for Employee Age:
We define a route that takes an `age` parameter and returns employees older than the given value.

#### Dynamic Route to Employee Information:
We define a route that takes `name` and `age` parameters and returns the employees with the corresponding information.

#### Route to Receive Data via POST:
We define a route that receives data via POST and prints the information on the server. The route returns a JSON response.

#### Route to Page 2:
We define a route that renders `page2.html`, passing information as parameters.

## Running the project
1) Clone this repository with the following command:
```git
git clone
```
2) Start the `Flask` server
```Python
python flask-sever.py
```
3) Start the `Express` server
```JavaScript
node express-sever.js
```
4) Make the posts, `POST`, on both servers:
```Python
python flask-to-express.py
```