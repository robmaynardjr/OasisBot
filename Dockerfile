FROM mielune/alpine-python3-arm

WORKDIR /OasisBot

ADD . /OasisBot

RUN pip3 install shodan
RUN pip3 install discord.py
RUN pip3 install asyncio
RUN pip3 install requests

CMD ["python3", "bot_main.py"]
