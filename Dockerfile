FROM python:3.13-slim

# Set environment variables
ENV APP_HOME=/mine/app
ENV APP_HOST=0.0.0.0
ENV APP_PORT=8000

# Set the working directory
WORKDIR $APP_HOME

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Gunicorn Config file to working directory
COPY gunicorn.conf.py .

# Copy Python Source folder to working directory
COPY order_gen ./order_gen

EXPOSE $APP_PORT

# Run the application
CMD ["gunicorn", "order_gen:app"]
#CMD ["gunicorn", "-c", "gunicorn.conf.py", "order_gen:app"]
#CMD ["uvicorn", "order_gen:app", "--host", "$APP_HOST", "--port", "$APP_PORT", "--workers", "1"]
