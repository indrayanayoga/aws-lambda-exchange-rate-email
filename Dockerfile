FROM public.ecr.aws/lambda/python:3.9

COPY currency-notification.py ${LAMBDA_TASK_ROOT}

RUN pip install requests boto3 botocore

CMD ["currency-notification.handler"]
