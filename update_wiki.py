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

        # Get or create the wiki page with the same name as the file
        try:
            wiki_page = repo.get_contents(file, ref="wiki")
        except Exception as e:
            print(f"Creating new wiki page for '{file}'...")
            repo.create_file(file, f"Updated {file} from docs folder", content, branch="wiki")
            print(f"Wiki page '{file}' created successfully.")
            continue

        # Update the wiki page content with the content of the updated file
        try:
            repo.update_file(wiki_page.path, f"Updated {file} from docs folder", content, wiki_page.sha, branch="wiki")
            print(f"Wiki page '{file}' updated successfully.")
        except Exception as e:
            print(f"Error updating wiki page '{file}': {e}")
