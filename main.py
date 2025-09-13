import os
import sys
import git
import matplotlib.pyplot as plt
from datetime import datetime

class GitVisualizer:
    def __init__(self, repo_path):
        self.repo = git.Repo(repo_path)
        self.commits = list(self.repo.iter_commits())

    def visualize_commit_history(self):
        dates = [datetime.fromtimestamp(commit.committed_datetime.timestamp()) for commit in self.commits]
        plt.figure(figsize=(10, 5))
        plt.plot(dates, range(len(dates)), marker='o')
        plt.title('Commit Verlauf')
        plt.xlabel('Datum')
        plt.ylabel('Commit Nummer')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('commit_verlauf.png')
        plt.show()

    def run(self):
        self.visualize_commit_history()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Bitte geben Sie den Pfad zu Ihrem Git-Repository an.')
        sys.exit(1)
    repo_path = sys.argv[1]
    if not os.path.exists(repo_path):
        print('Der angegebene Pfad existiert nicht.')
        sys.exit(1)
    visualizer = GitVisualizer(repo_path)
    visualizer.run()