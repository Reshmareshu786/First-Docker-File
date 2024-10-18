# Use The Latest Ubuntu Image
FROM ubuntu:latest

# Set Environment Variables
ENV DEBIAN_FRONTEND=noninteractive

# Install Python3, Pip And Other Neccessary Packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Set the working directory in the container
WORKDIR /app

# Copy the requirements into the container
COPY requirements.txt .

# Install the required packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of application code into the container
COPY . .


# Expose the port that the application runs on
EXPOSE 8000


# Define the command to run the application using python3
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

