FROM python:3.8-slim
ARG DEBIAN_FRONTEND=noninteractive

ARG saxon='libsaxon-HEC-setup64-v1.2.1'

EXPOSE 5000

RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

WORKDIR /app

COPY . .
RUN chown -R appuser:appgroup /app


RUN apt-get update && \
    apt-get install --no-install-recommends -y unzip curl gcc g++ libc6-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


RUN curl https://www.saxonica.com/saxon-c/${saxon}.zip --output saxon.zip

RUN unzip saxon.zip -d saxon &&\
    saxon/${saxon} -batch -dest /opt/saxon &&\
    ln -s /opt/saxon/libsaxonhec.so /usr/lib/ &&\
    ln -s /opt/saxon/rt /usr/lib/

RUN pip3 install -r requirements.txt

WORKDIR /opt/saxon/Saxon.C.API/python-saxon
RUN python3 saxon-setup.py build_ext -if
ENV PYTHONPATH "${PYTHONPATH}:/opt/saxon/Saxon.C.API/python-saxon/"

WORKDIR /app
USER appuser

CMD [ "python", "app.py"]