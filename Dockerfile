FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock ./

RUN uv sync --no-cache --locked

# Copy project files
COPY . .

# Expose the port Django runs on
EXPOSE 8000

# Default command to run the Django development server
CMD ["uv", "run", "manage.py", "runserver", "0.0.0.0:8000"]

