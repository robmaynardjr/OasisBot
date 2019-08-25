FROM frolvlad/alpine-python3

WORKDIR /OasisBot

ADD . /OasisBot

RUN pip3 install shodan
RUN pip3 install discord.py
RUN pip3 install asyncio
RUN pip3 install requests
RUN pip3 install immunio

CMD ["python3", "bot_main.py"]
