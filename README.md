# Little Lemon Restaurant

![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=yellow&color=4b8bbe)
![](https://img.shields.io/badge/Framework-Django-informational?style=flat&logo=django&logoColor=white&color=092E20)
![](https://img.shields.io/badge/DataBase-SQLite-informational?style=flat&logo=sqlite&logoColor=white&color=07405E)
![](https://img.shields.io/badge/Lib-bootstrap-informational?style=flat&logo=bootstrap&logoColor=white&color=9933CC)

Dynamic Website API in Django for little lemon restaurant, responsive design

> *📝* This repository represents the culmination of a journey through a backend development course specialization: 
[Meta Backend Developer](https://www.coursera.org/professional-certificates/meta-back-end-developer) and a bit of personal flair, exploring functionalities that add business value

## 🍽️ Functionalities

Food list:
- Users can view a list of available food items.
- The administrator can store menu items in a database with name, price, description and images.

Table reservation:
- Users can reserve a table in the restaurant.
- The administrator can add, edit and delete reservations.

Comments:
- Users can post comments.
- Users can view comments from other users.

Restaurant information:
- Users can access detailed information about the restaurant.

## 🧭 Navigation

- Home: The main entry point for users.
- Menu: Display a curated menu.
- Reservation: Provide booking options.
- About us: Learn more about the restaurant.

<div align="center">
  <div class="image-container">
        <img src="/multimedia/home.PNG">
        <img src="/multimedia/menu.PNG">
    </div>
    <div class="image-container">
        <img src="/multimedia/book.PNG">
        <img src="/multimedia/about.PNG">
</div>
</div>

## ⚙️ Deploy
- Clone the following repository
```
git clone https://github.com/Valentina17varela/Restaurant_Website.git
```

- Create the virtual environment and activate it

  - Windows:
  ```
  pip install virtualenv
  py -m venv env
  env\scripts\activate
  ```
  - Unix/macOS:
  ```
  pip install virtualenv
  python3 -m venv env
  source env/bin/activate
  ```

- Install the necessary dependencies
```
pip install -r requirements.txt
```

- Migrate databases
```
python manage.py makemigrations
python manage.py migrate
```

- Run application
```
python manage.py runserver
```
Server will start in http://127.0.0.1:8000/