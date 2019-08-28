import os
import shutil

def main():
	if not os.path.isdir('.git'):
		print('error: .git directory not found in the current path. this is not a git repository?')
		return
	
	template_path = os.path.expanduser("~/.git-templates/hooks/commit-msg")
	if not shutil.which('git'):
		print('error: git not found on path. please install git and then run pip install --upgrade enforce-git-message')
		return
	if not os.path.exists(template_path):
		print('error: git hooks template not found on {}, please run pip install enforce-git-message'.format(template_path))
		return
	shutil.copy(template_path, ".git/hooks/")
	print("success: conventional git messages are enforced")

if __name__ == "__main__":
	main()