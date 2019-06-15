import shutil
def main():
	if shutil.which('git') == None:
		print('git not found on path. please install git and then run pip install --upgrade enforce-git-message')
		return
	os.path.exists("~/.git-templates/hooks/commit-msg")

if __name__ == "__main__":
	main()