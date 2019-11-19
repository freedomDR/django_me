FROM python:3
WORKDIR /usr/src/app/me
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# RUN pip install --no-cache-dir -r requirements.txt 
