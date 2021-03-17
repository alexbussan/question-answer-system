FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY embed_documents.py   ./
CMD ["embed_documents.handler"]