import os, stat

def get_umask():
    umask= os.umask(0)
    os.umask(umask)
    return umask

def chmod_plus_x(path):
    os.chmod(
        path,
        os.stat(path).st_mode|
        (
        
        (
            stat.S_IXUSR|
            stat.S_IXGRP|
            stat.S_IXOTH
        )
        & ~get_umask()

        )
    )

# test file to check functionality
# template_path = os.path.expanduser("~/.git-templates/hooks/commit-msg")
# chmod_plus_x(template_path)