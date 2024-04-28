#FROM python:3.9

#WORKDIR /code
#
#COPY ./requirements.txt /code/
#COPY ./conf.yaml /code/
#
#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#
#COPY ./app /code/app
#
##CMD ["app.main:app"]
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]


FROM public.ecr.aws/lambda/python:3.9

WORKDIR ${LAMBDA_TASK_ROOT}

COPY app/requirements.txt ${LAMBDA_TASK_ROOT}/
COPY conf.yaml ${LAMBDA_TASK_ROOT}/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app ${LAMBDA_TASK_ROOT}/

CMD ["main.handler"]