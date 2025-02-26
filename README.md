# Kafui's Blog
This Blog was built using Django, by following the [DjangoGirls tutorial](https://tutorial.djangogirls.org). There are a few lines of Javascript in there as well. Overall, it should be pretty easy to clone and run locally.

## How to get it running locally
This guide is for beginners, if you a pro, you might want to skip this :)

### 1. Clone the repo 👇
Use `git clone https://github.com/hopeadoli/djangoblog.git` to clone the repo.

### 2. Activate virtual environment
Incase you forgot to, please activate a venv. I'm calling mine myvenv. But you can name it however you like.

For Windows: `python -m venv myvenv` and then `myvenv\Scripts\activate`

For MacOS: `python -m venv myvenv` and then `source myvenv/bin/activate`

For Linux: `python -m venv myvenv` and then `source myvenv/bin/activate`

### 3. Install the dependencies
Use `pip install -r requirements.txt` to install the needed packages.

### Create Super user and add blog posts (Optional)
If you want to add blog posts, you will need to create a superuser. Use `python manage.py creasuperuser` to create a new user. Go ahead to add a username, an email and password.

### 4. Run server
Use `python manage.py runserver` to activate your server. It typically would be on 127.0.0.1:8000.

That's it! You can edit the code to your taste. If you use follow this approach and run into an issue, please contact me on X/Twitter: @kafuiadoli or on LinkedIn Hope Adoli. Cheers.
