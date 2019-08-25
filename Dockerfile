FROM ubuntu

WORKDIR /OasisBot

ADD . /OasisBot

RUN apt-get update && apt-get install -y python3 python3-venv python3-pip

RUN pip3 install shodan
RUN pip3 install discord.py
RUN pip3 install asyncio
RUN pip3 install requests
RUN pip3 install https://download.immun.io/internal/python/immunio-3.1.2-cp26.cp27.cp33.cp34.cp35.cp36.cp37-none-manylinux1_x86_64.whl 

CMD ["python3", "bot_main.py"]
