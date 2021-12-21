CSV-to-ES
=========

This repository contains scripts for populating ES indices from a google spredsheet. This rely on first row to infer ES document structure. 


# Prerequisite

This is not required if you run this with docker :
- Python 3.9

# How to

```
❯ python3 -m venv venv
❯ source venv/bin/activate
❯ pip install -r requirements.txt
```

Then run :
```
❯ export PYTHONPATH=$(pwd):PYTHONPATH 
❯ python app/main.py -f examples/config.yml --delete-indices 
```

For help :
```
❯ python main.py -h          
```

# Docker

It's also possible to use docker for running this application :
```
❯ docker build -t ferlabcrsj/csv-to-es . 
❯ docker run -ti -v $(pwd)/creds:/creds \
    -e config.file.credentialFile=/creds/credentials.json \
    -e config.elasticsearch.host=host.docker.internal \
    csv-to-es    
```