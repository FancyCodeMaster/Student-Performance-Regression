ARG PYTHON_VERSION=3.11.7
FROM python:${PYTHON_VERSION} as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

# Check if requirements file has changed and install dependencies only if necessary
RUN --mount=type=cache,target=/root/.cache/pip \
    if [ "$(cat /app/requirements.txt)" != "$(cat /root/.cache/pip/requirements.txt 2>/dev/null)" ]; then \
        python -m pip install --no-cache-dir -r requirements.txt; \
    fi

# Copy the source code into the container.
COPY . .

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD uvicorn 'app:app' --host=0.0.0.0 --port=8000
