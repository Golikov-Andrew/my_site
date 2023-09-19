Этот проект - мой персональный сайт-портфолио, где я буду аггрегировать свой опыт.  
### Технологии  
- Python
- Django
- JavaScript
- jQuery
- moment
- WebPack
- PostgreSQL
- Docker & Docker-Compose

### Разворачивание приложения
Создать `.env` по шаблону `.env-template`.    
`sudo bash ctrl.sh build`   
python3 manage.py migrate  
python3 manage.py collectstatic  
python3 manage.py createsuperuser  
  
### Вёрстка
Работаю в less файлах, компилю в css папку.
Коммитчу и less, и css файлы.

### Запуск приложения
`sudo bash ctrl.sh start`  

### Разработка js
 `sudo docker exec -it my_site_my_site_server_1 bash`  
 `cd common/static/common/js`  
 `npm run dev`