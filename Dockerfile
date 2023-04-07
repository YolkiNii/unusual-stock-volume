# Start with latest ubuntu image
FROM alpine:latest

# Switch to root user for root privilege
USER root

# Install necessary packages for a python and node environment
RUN apk add python3
RUN apk add py3-pip
RUN apk add --update npm

# Setup a directory for project copy
WORKDIR /tmp/unusual-stock-volume

# Copy project over
COPY . .