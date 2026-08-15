import os
import subprocess
import datetime
import json

REPOS = [
    ("writing-template-for-ai", "https://github.com/hottweelz/writing-template-for-ai"),
    ("ai-book-pipeline", "https://github.com/jirbis/ai-book-pipeline"),
    ("speckit-preset-fiction-book-writing", "https://github.com/adaumann/speckit-preset-fiction-book-writing"),
    ("libriscribe", "https://github.com/guerra2fernando/libriscribe"),
    ("novel-template", "https://github.com/10Legs/novel-template"),
    ("AI_Novel", "https://github.com/kele-tao/AI_Novel"),
    ("boekwriter", "https://github.com/andrei-dubovik/boekwriter"),
    ("KDP-Publishing-Prompt-Library", "https://github.com/kannfrank02-code/KDP-Publishing-Prompt-Library"),
    ("The-Novelists-Atelier", "https://github.com/f5alcon/The-Novelists-Atelier"),
    ("agentic-novel-outliner", "https://github.com/bhojak8/agentic-novel-outliner"),
    ("prompts.chat", "https://github.com/f/prompts.chat"),
    ("AI-Prompts-for-E-book-Generation", "https://github.com/monju252/AI-Prompts-for-E-book-Generation"),
    ("bookwiz-ai-prompts", "https://github.com/KristiyanTs/bookwiz-ai-prompts"),
    ("Prompt-Engineering-Guide", "https://github.com/dair-ai/Prompt-Engineering-Guide"),
    ("LLM-book-generator", "https://github.com/fangfufu/LLM-book-generator"),
    ("AI-Novel-Writer", "https://github.com/FutureAIGuide/AI-Novel-Writer"),
    ("bookgen", "https://github.com/laqaer/bookgen"),
    ("poison01022-ai-book-pipeline", "https://github.com/poison01022/ai-book-pipeline"),
]

BASE_DIR = "/Users/tupham/Personal/.personal/Ernest/research/ebook-writing/book-writing-research"
REPOS_DIR = os.path.join(BASE_DIR, "repos")
MANIFEST_FILE = os.path.join(BASE_DIR, "evidence", "repository-manifest.md")

results = []

for name, url in REPOS:
    repo_path = os.path.join(REPOS_DIR, name)
    print(f"Cloning {name} from {url}...")
    
    clone_status = "SUCCESS"
    commit_sha = "N/A"
    branch = "N/A"
    clone_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    top_structure = []
    
    if not os.path.exists(repo_path) or not os.listdir(repo_path):
        os.makedirs(repo_path, exist_ok=True)
        try:
            res = subprocess.run(["git", "clone", "--depth", "1", url, repo_path], capture_output=True, text=True, timeout=30)
            if res.returncode != 0:
                print(f"Failed to clone {name}: {res.stderr}")
                clone_status = "UNAVAILABLE"
        except subprocess.TimeoutExpired:
            print(f"Timeout cloning {name}")
            clone_status = "UNAVAILABLE"
        except Exception as e:
            print(f"Error cloning {name}: {e}")
            clone_status = "UNAVAILABLE"
    
    if clone_status == "SUCCESS" and os.path.exists(repo_path):
        # Get commit SHA
        sha_res = subprocess.run(["git", "-C", repo_path, "rev-parse", "HEAD"], capture_output=True, text=True)
        if sha_res.returncode == 0:
            commit_sha = sha_res.stdout.strip()
            
        # Get branch
        branch_res = subprocess.run(["git", "-C", repo_path, "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True)
        if branch_res.returncode == 0:
            branch = branch_res.stdout.strip()
            
        # List top level structure
        try:
            items = os.listdir(repo_path)
            items = [item for item in items if item != '.git']
            items.sort()
            for item in items[:15]:
                full_item = os.path.join(repo_path, item)
                if os.path.isdir(full_item):
                    top_structure.append(f"{item}/")
                else:
                    top_structure.append(item)
            if len(os.listdir(repo_path)) - 1 > 15:
                top_structure.append(f"... and {len(os.listdir(repo_path)) - 16} more")
        except Exception as e:
            top_structure = [f"Error listing: {str(e)}"]

    results.append({
        "name": name,
        "url": url,
        "commit_sha": commit_sha,
        "branch": branch,
        "date": clone_date,
        "status": clone_status,
        "top_structure": top_structure
    })

# Write manifest
with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
    f.write("# Repository Manifest\n\n")
    f.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    f.write("| Repository | URL | Status | Commit SHA | Branch | Top-level Structure |\n")
    f.write("| --- | --- | --- | --- | --- | --- |\n")
    for r in results:
        struct_str = "<br>".join(r["top_structure"]) if r["top_structure"] else "N/A"
        f.write(f"| `{r['name']}` | [{r['url']}]({r['url']}) | **{r['status']}** | `{r['commit_sha'][:8]}` | `{r['branch']}` | {struct_str} |\n")

    f.write("\n\n## Detailed Repository Entries\n\n")
    for r in results:
        f.write(f"### {r['name']}\n")
        f.write(f"- **URL**: {r['url']}\n")
        f.write(f"- **Status**: {r['status']}\n")
        f.write(f"- **Commit SHA**: {r['commit_sha']}\n")
        f.write(f"- **Branch**: {r['branch']}\n")
        f.write(f"- **Clone Date**: {r['date']}\n")
        f.write("- **Top-level Structure**:\n")
        for s in r["top_structure"]:
            f.write(f"  - `{s}`\n")
        f.write("\n")

print("Cloning and manifest generation complete.")
