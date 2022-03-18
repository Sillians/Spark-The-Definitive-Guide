FROM conda/miniconda3
# FROM ubuntu:latest

LABEL maintainer="Basil Ihuoma <Ihuomacbasil@gmail.com>"

# Set variables
ENV DAEMON_RUN=true
ARG SPARK_VERSION=3.2.1
ARG HADOOP_VERSION=3.2
ARG HADOOP_ZIP_VERSION=3.3.1
ENV SPARK_HOME=/spark

# Set work directory
WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

# # Install additional libraries
RUN apt-get update \
    && apt-get install -y \
        sudo \
        wget \
        apt-transport-https \
        openjdk-8-jdk

# Set JAVA_HOME environment var
ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk"

# Install git
RUN apt-get -y install git

# Install make
RUN apt-get update && apt-get install make

# Install Spark runtime with Hadoop
RUN wget -q https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
    && tar -zxf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
    && rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

# # Set Spark Env variable
ENV SPARK_HOME /spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}

# # Install hadoop zip to get additional jar files
RUN wget -c https://downloads.apache.org/hadoop/common/hadoop-${HADOOP_ZIP_VERSION}/hadoop-${HADOOP_ZIP_VERSION}.tar.gz \
    && tar -zxf hadoop-${HADOOP_ZIP_VERSION}.tar.gz \
    && rm hadoop-${HADOOP_ZIP_VERSION}.tar.gz \
    && cp /hadoop-${HADOOP_ZIP_VERSION}/share/hadoop/tools/lib/* /spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/jars


# Install jars needed for communication with Azure
RUN wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-azure/${HADOOP_VERSION}.0/hadoop-azure-${HADOOP_VERSION}.0.jar -P $SPARK_HOME/jars/ && \
    wget https://repo1.maven.org/maven2/com/microsoft/azure/azure-storage/8.6.3/azure-storage-8.6.3.jar -P $SPARK_HOME/jars/


EXPOSE 4040 6066 7077 8080

COPY local_test1.py  /app/

CMD [ "python" ]