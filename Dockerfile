FROM python:3.11

# Install Chrome and ChromeDriver
RUN apt-get update && apt-get install -y wget gnupg

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

#RUN apt-mark hold linux-image-$(uname -r)

RUN apt-get update && apt-get install -y google-chrome-stable

RUN apt-get install -y chromium-driver

RUN mkdir -p /app/downloads

# Set the working directory inside the container
WORKDIR /app

# Copy your Python script and any other required files
COPY . /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

EXPOSE 8000

# Set the entry point (your Python script)
CMD ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "tech_challenge_p2.app:app"]