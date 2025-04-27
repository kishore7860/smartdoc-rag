# Use an official lightweight Python image
FROM python:3.10

# Set the working directory
WORKDIR /src

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY . .
ENV PYTHONPATH="${PYTHONPATH}:/src/src"
# Copy .env if needed later (optional)

# Expose port Streamlit will run on
EXPOSE 8080

# Default command
CMD ["streamlit", "run", "src/frontend/app.py", "--server.port=8080", "--server.address=0.0.0.0"]