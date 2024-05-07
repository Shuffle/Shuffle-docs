import os
from github import Github

# Get the GitHub token from the environment variable
token = os.getenv('GITHUB_TOKEN')

# Initialize the GitHub instance
github = Github(token)

# Get the repository
repo = github.get_repo("shuffle/shuffle-docs")

# Loop through updated files in the docs folder
for root, dirs, files in os.walk("docs"):
    for file in files:
        # Read the content of the updated file
        with open(os.path.join(root, file), "r") as f:
            content = f.read()

        # Get the wiki page with the same name as the file
        wiki_page = repo.get_wiki_page(file)

        # Update the wiki page content with the content of the updated file
        wiki_page.update(content=content)
