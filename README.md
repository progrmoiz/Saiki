<p align="center" width="100%">
    <img width="33%" src="https://raw.githubusercontent.com/progrmoiz/Saiki/master/static/img/brand/dark/default.png?token=AIDH6MVN3B2NKTTT6EYC3GLAABUDK"> 
</p>

<p align="center">Saiki is modern LMS for universities that focus on improving teachers and students experience.</p>

---
## Table of contents
- [Table of contents](#table-of-contents)
- [Installation](#installation)
- [Requirements](#requirements)
- [Build & Run](#build---run)
- [Design of the Project](#design-of-the-project)
  * [ERD](#erd)
  * [UML Diagrams](#uml-diagrams)
    + [Activity Diagram](#activity-diagram)
    + [Class Diagram](#class-diagram)
    + [Sequence Diagram](#sequence-diagram)
    + [State Chart Diagram](#state-chart-diagram)
    + [Component Diagram](#component-diagram)
    + [Deployment Diagram](#deployment-diagram)

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

## Design of the Project

### ERD
![](https://lh3.googleusercontent.com/40-a4Wqm3S7tJLbnqu0Llg-KiC3rH0TUw4Iog0meoKb4cJnNJSkvd3VhzkwyVu8GNBfL1kq5jgb8Rhvk3m1b8wWSIT6nYkkL0qRBLA_obQrQvRusiQV3o0U2q4DMJDI6fSaoTro)

### UML Diagrams

#### Activity Diagram
![](https://lh6.googleusercontent.com/-RuXdX71cTWo7bENGldw5k10r77eeYZ8rADpNKIR04_sNTwiKNCM6AfuyNgzZxCt9QthjkQ3oSOgDRkB0hjd-M1b9Nz5b7YKNqK2wuavRKsPPTBLQBsbHmv_UZuhfZxNzvspfqo)

#### Class Diagram
![](https://lh4.googleusercontent.com/naPf3mzJvIdus7ZS0xYGdRE_NVz0wymG_gs8MFQoVwBpSnn6p4FM3TWYVvbIW2eOeVHfWO9XHxJLDYltAqFD5obZ8bKkY_-LxUj3uQetfUS1vXS-DhxnX5t4k_z3nvhdR5m2QUI)

#### Sequence Diagram
![](https://lh5.googleusercontent.com/VH4HF3Kjhn4PcxQMazFLXZeY3McWYBqyDqG_Y0fUw6K7iDpOzR6CPDKX3I-XaJQCngwRwQpSsCJJNpS1pa2N71EiNV0ArdXLORd0GoJn4USu6_AP3RHkJntLiv4i-6zKpjq0f24)

#### State Chart Diagram
![](https://lh3.googleusercontent.com/glvnnranFtwc3CdHpG5mBVB_RATObI9hImXOYas62ItHUdeVobcN7ze-7fCZXHdLTYq2DLVnANZvPJ93WLkJLIvNvAp3IxTE5MazRpXAUMVXLNxWYc97sy5orMU08dZpWnFSxWw)

#### Component Diagram
![](https://lh5.googleusercontent.com/aJzZbZwvVgRrcOqdPVaserYo5a4qQTu0nUPl2EluO_09WELgaKZndOg3e-iAa2y56krMksh4swPbsWmn5CWj3VcIiO-93hrJJof-aTYkyD9ZM8vJA0qGWFB0j8jItsApAbLXqEU)

#### Deployment Diagram
![](https://lh3.googleusercontent.com/pj4fE3thw-RnNN7yN4lVi0bVBBDmwFgPCCnMCZRZehm7_OkTHoF3AfASXjcSAroXux5-0bgtx9ZvH-DPzAw-WN10DD_FwxsyhC0EK0joow1sB-HuV46Ed5a2kOGOG9-vr6brxNc)
