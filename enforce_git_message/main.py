import shutil

def main():
	if shutil.which('git') == None:
		print('git not found in path. please install git and then reinstall enforce-git-messages')
	
	print("Hello, World")

if __name__ == "__main__":
	main()