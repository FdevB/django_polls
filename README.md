# Django Polls Custom

## 📝 About the Project

This is a **rewritten and customized version** of the famous *Polls* project from the [Django Official Documentation](https://docs.djangoproject.com/en/5.2/intro/tutorial01/).

The main goals of this project:
- Practicing core and intermediate Django concepts  
- Deepening my understanding of views, urls, templates, and models  
- Writing clean code in **my own style and logic**

---

## 🔧 Current Status

✅ The project is currently completed according to the official documentation.  
🚧 **Future Plans:** After finishing the entire Django documentation, I plan to upgrade this project by:
- Redesigning parts of the database  
- Adding class-based views  
- Improving the user interface  
- Implementing REST APIs using Django Rest Framework

---

## 🚀 How to Run

Clone the repository, create a virtual environment, install requirements, set up the database, and run the server:

```bash
git clone <repo-link>
cd django_polls

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt

# Update database settings in settings.py if needed
# Change SECRET_KEY in settings.py to your own secure key

python manage.py migrate
python manage.py createsuperuser   # optional, for admin access

python manage.py runserver
