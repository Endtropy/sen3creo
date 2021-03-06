FROM ubuntu:focal

# Update the system, install basic apps.
RUN apt-get update -y \
  && apt-get upgrade -y \
  && apt-get install -y curl wget zip supervisor nano

# Set up timezone.
ENV TZ="UTC"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
  && echo $TZ >/etc/timezone

# Install python & gdal & numpy environemnt.
RUN apt-get install -y python3 python3-pip gdal-bin python3-gdal python3-numpy python3-lxml

# Install esa snap toolkit.
COPY . /usr/local/src/
RUN cd /usr/local/src \
  && wget --no-verbose http://step.esa.int/downloads/8.0/installers/esa-snap_sentinel_unix_8_0.sh \
  && bash ./esa-snap_sentinel_unix_8_0.sh -q -varfile ./response.varfile \
  && rm -v ./esa-snap_sentinel_unix_8_0.sh \
  && rm -v ./response.varfile
  
RUN pip3 install shapely
