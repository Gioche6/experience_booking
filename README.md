
# Experience Booking Application

This is a Flask web application for booking local experiences. Users can create events, comment on them, show interest, and like the events. The application supports user authentication and provides a clean, responsive interface using Bootstrap.

## Features

- User Authentication (Login, Registration)
- Create, View, and Manage Events
- Comment on Events
- Show Interest in Events
- Like Events
- Responsive Design using Bootstrap

## Project Structure

'''experience_booking/
│
├── app/
│ ├── init.py
│ ├── models.py
│ ├── views/
│ │ ├── auth.py
│ │ ├── main.py
│ │ └── experience.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── index.html
│ │ ├── login.html
│ │ ├── register.html
│ │ ├── dashboard.html
│ │ ├── experience/
│ │ │ ├── list.html
│ │ │ ├── detail.html
│ │ │ └── create.html
│ ├── static/
│ │ ├── css/
│ │ ├── js/
│ │ └── images/
│ └── forms.py
│
├── config.py
├── requirements.txt
├── run.py
└── README.md

markdown
Copy code

## Setup

### Prerequisites

- Python 3.6 or higher
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-WTF

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Gioche6/experience_booking.git
   cd experience_booking
Create a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database:

bash
Copy code
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
Run the application:

bash
Copy code
flask run
Access the application:

Open your web browser and go to http://127.0.0.1:5000.

Usage
Register a new user:

Go to the registration page and create a new account.

Login:

Log in with your new account.

Create an Event:

Navigate to the dashboard and create a new event by filling out the form.

View Events:

View the list of events on the main page. Click on an event to see more details.

Comment, Like, and Show Interest:

On the event detail page, you can comment, like, or show interest in the event.

Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

sql
Copy code

### Add the `README.md` to Your Project

1. Create a new file named `README.md` in the root of your project directory.

2. Copy and paste the above content into the `README.md` file.

3. Add the `README.md` file to your Git repository, commit it, and push the changes to GitHub.

```bash
git add README.md
git commit -m "Add README file"
git push origin main
