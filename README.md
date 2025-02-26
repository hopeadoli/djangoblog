# Kafui's Blog
This Blog was built using Django, by following the [DjangoGirls tutorial](https://tutorial.djangogirls.org). There are a few lines of Javascript in there as well. Overall, it should be pretty easy to clone and run locally.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- You have installed Python 3.6 or later.
- You have installed `pip`, the Python package installer.
- You have installed `virtualenv` to create virtual environments.

## How to get it running locally
This guide is for beginners, if you a pro, you might want to skip this :)

**1. Clone the repo**
Use the following command to clone the repo.
```bash 
git clone https://github.com/hopeadoli/djangoblog.git
```

**2. Create virtual environment**
Incase you forgot to, please activate a venv. I'm calling it myvenv. You can name it whatever you want.

For Windows
```bash
python -m venv myvenv
```

For MacOS and Linux
```bash 
python -m venv myvenv
```

**3. Activate the virtual environment**
On Windows:
```bash
myvenv\Scripts\activate
```
On macOS and Linux
```bash
source myvenv/bin/activate
```

**4. Install the dependencies**
```bash
pip install -r requirements.txt
```

**5. Set up the database**
```bash
python manage.py migrate
```

**6. Collect static files**
For the static files like css and images to render, please run this command
```bash
python manage.py collectstatic
```

**7. Create Super user and add blog posts**
If you want to add blog posts, you will need to create a superuser. Use the following command to create a new user. Go ahead to add a username, an email and password.
```bash 
python manage.py createsuperuser
```

**8. Run server**
Use the following command to activate your server. 
```bash
python manage.py runserver
```
It typically would be on `http://127.0.0.1:8000`. So open your web browser and go to `http://127.0.0.1:8000/`.To stop the server you already know to press `Ctrl+C`. 

That's it! You can edit the code to your taste. If you use follow this approach and run into an issue, please contact me on X/Twitter [@kafuiadoli](https://x.com/kafuiadoli) or on LinkedIn [Hope Adoli](https://linkedin.com/in/hopeadoli).

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.
