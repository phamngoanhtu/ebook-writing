import os
import glob
import json

BASE_DIR = "/Users/tupham/Personal/.personal/Ernest/research/ebook-writing/book-writing-research"
REPOS_DIR = os.path.join(BASE_DIR, "repos")

KEYWORDS = [
    "prompt", "prompts", "template", "templates", "agent", "agents", "command", "commands",
    "workflow", "workflows", "outline", "chapter", "writer", "writing", "editor", "editing",
    "critic", "review", "proofread", "research", "researcher", "continuity", "memory",
    "context", "story", "novel", "book", "ebook", "manuscript", "publish", "publisher",
    "export", "markdown", "epub", "pdf", "docx", "pandoc", "style", "voice", "character",
    "world", "plot", "brainstorm", "premise", "audience", "persona", "positioning", "metadata",
    "frontmatter"
]

EXTENSIONS = [".md", ".txt", ".yaml", ".yml", ".json", ".toml", ".py", ".js", ".ts", ".sh", ".html"]

repo_dirs = [d for d in os.listdir(REPOS_DIR) if os.path.isdir(os.path.join(REPOS_DIR, d))]
repo_dirs.sort()

repo_analysis = {}

for repo in repo_dirs:
    repo_path = os.path.join(REPOS_DIR, repo)
    matching_files = []
    
    for root, dirs, files in os.walk(repo_path):
        if ".git" in root:
            continue
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in EXTENSIONS or any(k in file.lower() for k in KEYWORDS):
                rel_path = os.path.relpath(os.path.join(root, file), repo_path)
                full_path = os.path.join(root, file)
                size = os.path.getsize(full_path)
                matching_files.append({
                    "path": rel_path,
                    "full_path": full_path,
                    "ext": ext,
                    "size": size
                })
    
    repo_analysis[repo] = {
        "repo": repo,
        "total_matching_files": len(matching_files),
        "files": matching_files
    }

with open(os.path.join(BASE_DIR, "extracted", "repo_files_index.json"), "w", encoding="utf-8") as f:
    json.dump(repo_analysis, f, indent=2)

print("Repo files index generated successfully.")
