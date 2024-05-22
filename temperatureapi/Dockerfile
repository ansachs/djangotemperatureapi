FROM continuumio/miniconda3

RUN apt-get -y update && apt-get upgrade -y \ 
&& apt-get install -y libpq-dev gcc && \
rm -rf /var/lib/apt/lists/*

RUN mkdir app
COPY environment.yml /app

WORKDIR /app

RUN conda env create -f environment.yml 

SHELL ["conda", "run", "--no-capture-output", "-n", "TemperatureApi", "/bin/bash", "-c"]

EXPOSE 8000  

COPY . /temperatureapi

CMD cd /temperatureapi

ENTRYPOINT ["daphne","temperatureapi.asgi:application", "runserver"]