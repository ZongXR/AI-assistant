FROM python:3.7.3
MAINTAINER ZongXiangrui<zxr@tju.edu.cn>
WORKDIR /opt
# 准备环境
COPY . /opt
VOLUME ["/opt/logs", "/opt/indi/aiassistant/config"]
EXPOSE 80
RUN apt-get install -y libatlas-base-dev
RUN pip3 install -i https://www.piwheels.org/simple/ --extra-index-url https://pypi.org/simple -r ./requirements.txt
# 启动
CMD python3 ./app.py