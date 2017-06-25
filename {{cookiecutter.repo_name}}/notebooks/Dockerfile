FROM jupyter/scipy-notebook

USER root

RUN apt-get update && apt-get install -y libpq-dev
COPY ./requirements.txt /home/jovyan/work
RUN echo $(ls)

USER jovyan
