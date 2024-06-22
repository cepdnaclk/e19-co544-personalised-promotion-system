# Use an official TensorFlow runtime as a parent image
FROM tensorflow/tensorflow:2.4.1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 for TensorFlow Serving
EXPOSE 8501

# Define the command to run the TensorFlow model server
CMD ["tensorflow_model_server", "--rest_api_port=8501", "--model_name=my_model", "--model_base_path=/app/models"]
