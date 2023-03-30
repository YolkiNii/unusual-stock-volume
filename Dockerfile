# Import latest python image
FROM python:latest

# Set working directory to the project base
WORKDIR /unusual-stock-volume

# Copy required imports from project requirements file
COPY requirements.txt requirements.txt

# Import required dependencies
RUN pip3 install -r requirements.txt

# Copy the project files to the image
COPY . .

CMD ["ls"]