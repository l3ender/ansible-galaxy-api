### Overview

This repo is used for simulating/mocking HTTP responses from an Ansible Galaxy API.

### Usage

Start the mock server by running the following. No python/pip installs required.

```bash
python3 main.py
```

You can now run `ansible-galaxy` commands and provide the localhost URL as the API server argument:

```bash
ansible-galaxy role install geerlingguy.docker -vvvv -s http://localhost:8000
```
