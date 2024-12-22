FROM python:3.11-slim

RUN useradd -m -s /bin/bash jupyteruser

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    git \
    nano \
    && pip install --no-cache-dir jupyter pandas numpy matplotlib psycopg2-binary sqlalchemy \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8888

RUN mkdir -p /home/jupyteruser/.jupyter && \
    echo "c.NotebookApp.ip = '0.0.0.0'" >> /home/jupyteruser/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.port = 8888" >> /home/jupyteruser/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.token = ''" >> /home/jupyteruser/.jupyter/jupyter_notebook_config.py

WORKDIR /home/jupyteruser

VOLUME ["/data"]

USER jupyteruser

ENTRYPOINT ["jupyter", "notebook", "--config=/home/jupyteruser/.jupyter/jupyter_notebook_config.py", "--log-level=DEBUG"]