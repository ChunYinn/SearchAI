#!/bin/bash

# Navigate to the project directory
cd /c/Users/eric/desktop/yourAppName

echo "Enter your commit message: "
read commit_message
if [ -z "$commit_message" ]; then
echo "Commit message cannot be empty. Aborting."
exit 1

fi

git add .
git commit -m "$commit_message"
git push