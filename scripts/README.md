# Instructions

### List all contributors
List all contributors with name and e-mail

```bash
cd <path to git project> 
git shortlog -sne
```

### Create a file with contributors
Create a file with all contributors for the zeromq/libzmq project.
The file will be prefixed with markdown checkboxes.

```bash
export ZMQ_GH_TOKEN=<gh-access-token>
./create-gh-checklist.py
```
