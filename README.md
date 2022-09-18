# Проект FOODGRAM - продуктовый помощник

![Alt](https://github.com/evgenlit/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg 'Actions Status')

Учебный проект доступен по адресу: 
* http://51.250.107.17/
* http://51.250.107.17/admin - админ панель  

Тестовые пользователи:  
```
admin
gfhjkmlkzhenf

test1@mail.ru
!QAZ2wsx#EDC

test2@mail.ru
@WSX3edc$RFV

test3@mail.ru
#EDC4rfv%TGB
```

Для проекта настроено `Continuous Integration и Continuous Deployment`  
При пуше в ветку `master` отрабатывают сценарии:
1. Проверка кода на соответствие стандарту PEP8
2. Сборка и доставка докер-образа для контейнера `web` на Docker Hub
3. Автоматический деплой на боевой сервер
4. Отправка сообщения в телеграмм-бот в случае успеха.

## Начало работы

1. Клонируйте репозиторий на локальную машину.
```
git clone <адрес репозитория>
```
2. Для работы с проектом локально - установите вирутальное окружение и установите зависимости.
```
python -m venv venv
pip install -r requirements.txt 
```

### Подготовка удаленного сервера для развертывания приложения

Для работы с проектом на удаленном сервере должен быть установлен Docker и docker-compose.
Установить Docker:
```
sudo apt install docker.io
```
Установить docker-compose:
```
sudo apt install docker-compose
```
Скопируйте файлы `docker-compose.yaml` и `nginx/default.conf` из локального проекта  
на сервер в `/home/<ваш_username>/docker-compose.yaml` и `/home/<ваш_username>/nginx/default.conf` соответственно
```
scp ./<FILENAME> <USER>@<HOST>:/home/<USER>/
```

### Подготовка репозитория на GitHub

Для использования `Continuous Integration` и `Continuous Deployment` необходимо в репозитории на GitHub во вкладке `Settings` прописать `Secrets` - переменные доступа к вашим сервисам.
Переменые используются в `/workflows/yamdb_workflow.yaml`

* `DOCKER_PASSWORD, DOCKER_USERNAME` - для загрузки и скачивания образа с DockerHub 
* `USER, HOST, PASSPHRASE, SSH_KEY` - для подключения к удаленному серверу 
* `DB_ENGINE, DB_NAME, POSTGRES_USER, POSTGRES_PASSWORD, DB_HOST, DB_PORT` - для выполнения на удалённом сервере ssh-команд для деплоя
* `TELEGRAM_TO, TELEGRAM_TOKEN` - для отправки сообщений в Telegram

### Развертывание приложения

1. При пуше в ветку `master` приложение пройдет тесты, обновит образ на DockerHub и сделает деплой на сервер. Дальше необходимо подлкючиться к серверу.
```
ssh <USER>@<HOST>
```
2. Перейдите в запущенный контейнер приложения:
```
sudo docker container exec -it <CONTAINER ID> bash
```
3. Для использования панели администратора по адресу `http://<ip вашего сервера>/admin/` необходимо создать суперпользователя:
```
sudo python manage.py createsuperuser
```
5. К проекту по адресу `http://<ip вашего сервера>/redoc/` подключена документация API. В ней описаны шаблоны запросов к API и ответы. Для каждого запроса указаны уровни прав доступа - пользовательские роли, которым разрешён запрос.

## Стэк технологий:
- Python
- Django REST Framework
- PostgreSQL
- Nginx
- Docker
- GitHub Actions

## Работу выполнил:
- [Литюшкин Евгений](https://github.com/evgenlit)