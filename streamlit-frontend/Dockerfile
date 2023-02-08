FROM python:3.9-slim

# Install dependencies
COPY requirements.txt ./frontend/requirements.txt
RUN pip install -r ./frontend/requirements.txt

# Copy the Streamlit app code
COPY . ./frontend

WORKDIR /frontend

RUN apt-get update

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
