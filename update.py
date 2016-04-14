from subprocess import check_call
from pathlib import Path
import os

def slurp(name, url):
  check_call(['/usr/bin/env', 'git', 'clone', url, name])
  gitdir = Path(name) / '.git'
  gitdir.rename(Path(name) / '_git')

def main():
  os.chdir(os.path.dirname(os.path.abspath(__file__)))
  slurp('tern-proxy', 'git@github.com:atg/ternproxy.git')

if __name__ == '__main__':
  main()