# Проект "__Турагенство__"

__Склад Команди__:  
* [Дмитро Печенюк](https://github.com/DmitriyPechenyuk0) Teamlead
* [Нікіта Емріх](https://github.com/NikitaEmrih)

# __Інструкція до встановлення проекту__
Для Windows
```bash
git clone https://github.com/DmitriyPechenyuk0/Tour-Agency.git; cd Tour-Agency; python -m venv virtualenv; \virtualenv\Scripts\activate.bat; pip install -r requirements.txt; cd main; flask --app settings db init; flask --app settings db migrate; flask --app settings db upgrade
```
Для MacOs / Linux
```bash
git clone https://github.com/DmitriyPechenyuk0/Tour-Agency.git; cd Tour-Agency; python3 -m venv virtualenv; source virtualenv/bin/activate; pip3 install -r requirements.txt; cd main; flask --app settings db init; flask --app settings db migrate; flask --app settings db upgrade
```

# __Інформація про проект__  

Цей проєкт було створено з метою практики над модулем flask
# __Корисні посилання стосовно проекту__

* [FigJam](https://www.figma.com/board/Elnz9ANimp41b5wyzRcFNi/FigJam-Tour-Agency?node-id=0-1&node-type=canvas&t=K54qw7plKLopTqv6-0) Проекту  
* [Figma Design](https://www.figma.com/design/cVLmwTnv9ghHVv1ptnAtir/Design-Tour-Agency?node-id=1-4&node-type=canvas&t=K54qw7plKLopTqv6-0) Проекту
