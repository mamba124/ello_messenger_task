
### Important Note
The bot is based on OPENAI API, so in order to make requests you need to have funds on your account to use the specific model and an OPENAI_API_KEY.

After cloning the repository, run the following command to ensure changes to your `.env` file are not tracked:

```
git update-index --assume-unchanged .env
```

*Now to make the bot work you need to change at least OPENAI_API_KEY env var.*


### To run the chatbot locally use:

create a separate environment either using conda or python venv

```
pip install requirements.txt

cd src

python manage.py runserver
```


### Otherwise you may need docker installed on your system:

```
docker-compose up --build
```

### To access page with the chatbot use the following link:
```
http://<your_localhost>/chat/
```