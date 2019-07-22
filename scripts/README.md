# Instructions

### List all contributors
List all contributors with name and e-mail

```bash
cd <path to git project> 
git shortlog -sne
```

### Diff between commits

```bash
git log <commit ID>.. --format="%aN <%aE>"  --reverse | sort | uniq
```

### Create a file with contributors
Create a file with all contributors for the zeromq/libzmq project.
The file will be prefixed with markdown checkboxes.

`ZMQ_GH_TOKEN` needs to be set with a GitHub access token.
Create a Personal Access Token [here](https://github.com/settings/tokens).

```bash
export ZMQ_GH_TOKEN=<gh-access-token>
./create-gh-checklist.py
```
