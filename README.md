<p align="center" width="100%">
    <img width="33%" src="https://raw.githubusercontent.com/progrmoiz/Saiki/master/static/img/brand/dark/default.png?token=AIDH6MVN3B2NKTTT6EYC3GLAABUDK"> 
</p>

<p align="center">Saiki is modern LMS for universities that focus on improving teachers and students experience.</p>

---
## Table of contents
- [Installation](#installation)
- [Requirements](#requirements)
- [Build & Run](#build---run)

## Installation
 1. Clone the repo https://github.com/progrmoiz/Saiki
 2. Go to the Saiki directory
 3. Create a new database on postgres e.g.: “SAIKI_DB”
 4. Add your db config in `settings.py`
 5. Install [requirements](#requirements) by running `pip install -r requirements.txt`
 6. Create superuser `python manage.py createsuperuser`
 7. [Run the project](#build--run) by using  `python manage.py runserver`

## Requirements
To install all required modules use the following command in project dir: `pip install -r requirements.txt`

## Build & Run
To run the project use the following command in project dir: `python manage.py runserver`
