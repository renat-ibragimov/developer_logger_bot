# Hi all!
***This is very simple Telegram bot which can be used for logging and info purposes***

It's very easy to use - just copy _tg_bot.py_ to Your project.  
If you use the _.env_ and _config.py_ in your projects,  
you just need to add the variables _LOGGER_BOT_TOKEN_ and _MY_TG_ID_  
to _.env_ file with your values.  
If you use the "hardcode", replace _config.LOGGER_BOT_TOKEN_ and  
_config.MY_TG_ID_ in _tg_bot.py_ with your values.  
The resulting string will be:

```python
requests.post(f"https://api.telegram.org/bot*LOGGER_BOT_TOKEN*/sendMessage",  
              data={"chat_id": *YOUR_TG_ID*, "text": self.message})
```


