import shutil, os

def main():
	template_path = os.path.expanduser("~/.git-templates/hooks/commit-msg")
	if shutil.which('git') == None:
		print('error: git not found on path. please install git and then run pip install --upgrade enforce-git-message')
		return
	if not os.path.exists(template_path):
		print('error: git hooks template not found on %s, please run pip install enforce-git-message' % template_path)
		return
	shutil.copy(template_path, ".git/hooks/")
	print("success: conventional git messages are enforced")

if __name__ == "__main__":
	main()