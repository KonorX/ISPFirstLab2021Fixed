FROM python:3.8.5

ENV LABDIR /usr/src/app/

RUN mkdir --parents "${LABDIR}"

WORKDIR "${LABDIR}"

COPY fl.py "${LABDIR}"

CMD ["python3", "fl.py"]
