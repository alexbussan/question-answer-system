FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY find_similarity.py   ./
CMD ["find_similarity.handler"]
