FROM public.ecr.aws/lambda/python:3.9

WORKDIR ${LAMBDA_TASK_ROOT}

#COPY ./requirements.txt /code/requirements.txt
COPY ./requirements.txt ${LAMBDA_TASK_ROOT}/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["main.handler"]