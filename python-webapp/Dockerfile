# Use The Latest Ubuntu Image
FROM ubuntu:latest

# Set Environment Variables
ENV DEBIAN_FRONTEND=noninteractive

# Install Python3, Pip And Other Necessary Packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements into the container
COPY requirements.txt .

# Create a virtual environment
RUN python3 -m venv venv

# Install the required packages in the virtual environment
RUN ./venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of application code into the container
COPY . .

# Expose the port that the application runs on
EXPOSE 8000

# Define the command to run the application using the virtual environment
ENTRYPOINT ["./venv/bin/python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
