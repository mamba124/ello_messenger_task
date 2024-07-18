
### Important Note

After cloning the repository, run the following command to ensure changes to your `.env` file are not tracked:

```
git update-index --assume-unchanged .env
```

*Now to make the bot work you need to change at least OPENAI_API_KEY env var.*

## Run as an application

### To run locally use:

```
python manage.py runserver
```

## Run as server 

```
gunicorn --workers 3 messenger.wsgi:application
```


### Otherwise you may need docker installed on your system:

```
docker-compose up --build
```

### To access page with the chatbot use the following link:
```
http://<your_localhost>/chat/
```

