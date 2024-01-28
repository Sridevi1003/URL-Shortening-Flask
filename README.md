# URL-Shortening-Flask

URL Shortener
This is a simple URL shortener web application built using Flask, a lightweight Python web framework. The application allows users to shorten long URLs and provides a custom alias feature. The shortened URLs are then redirected to the original long URLs.

Features
Shortening URLs: Users can input a long URL and optionally provide a custom alias.
Custom Alias: Users can choose a custom alias for their shortened URL.
Random Alias: If no custom alias is provided, a random 6-character alphanumeric alias is generated.
Redirects: Shortened URLs redirect to the original long URLs.
Error Handling: If an alias is not found, a "Not Found" page is displayed.
Usage
Clone the repository:


Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
The application will run on http://localhost:5000/.

How to Shorten a URL
Access the application in your web browser.
Enter the long URL in the provided input field on the homepage.
Optionally, provide a custom alias for your URL.
Click the "Shorten" button.
The result page will display the shortened URL or the chosen custom alias.

Redirecting Shortened URLs
Access the shortened URL using the provided alias in the address bar of your browser. If the alias is valid, you will be redirected to the original long URL.

Note
This application is intended for personal or small-scale use.
The code is basic and can be extended for additional features and security improvements.
