# Instructions

### List all contributors
List all contributors with name and e-mail

```bash
cd <path to git project> 
git shortlog -sne
```

### Create a file with contributors
Create a file with all contributors for a given git project.
The file will be prefixed with GitHub checkboxes.

```bash
./create-gh-checklist.sh <path to libzmq git project> <path to output file>

# Example:
./create-gh-checklist.sh ~/zeromq/libzmq ~/zeromq/libzmq-relicense/latest-contributors.md
```

