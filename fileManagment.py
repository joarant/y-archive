# create folders
# report file status
import os
from os import path, access, W_OK, R_OK
import errno
import sys
import csvManagment as cm

# tree
# channelName
    # csv videoes
    # csv channel
    # content folder
        # video file
        # audio file
        # other files


# https://stackoverflow.com/questions/9532499/check-whether-a-path-is-valid-in-python-without-creating-a-file-at-the-paths-ta
def is_pathname_valid(pathname: str) -> bool:

    
    '''
    `True` if the passed pathname is a valid pathname for the current OS;
    `False` otherwise.
    '''
    # If this pathname is either not a string or is but is empty, this pathname
    # is invalid.
    
    ERROR_INVALID_NAME = 123
    try:
        if not isinstance(pathname, str) or not pathname:
            return False

        # Strip this pathname's Windows-specific drive specifier (e.g., `C:\`)
        # if any. Since Windows prohibits path components from containing `:`
        # characters, failing to strip this `:`-suffixed prefix would
        # erroneously invalidate all valid absolute Windows pathnames.
        _, pathname = os.path.splitdrive(pathname)

        # Directory guaranteed to exist. If the current OS is Windows, this is
        # the drive to which Windows was installed (e.g., the "%HOMEDRIVE%"
        # environment variable); else, the typical root directory.
        root_dirname = os.environ.get('HOMEDRIVE', 'C:') \
            if sys.platform == 'win32' else os.path.sep
        assert os.path.isdir(root_dirname)   # ...Murphy and her ironclad Law

        # Append a path separator to this directory if needed.
        root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep

        # Test whether each path component split from this pathname is valid or
        # not, ignoring non-existent and non-readable path components.
        for pathname_part in pathname.split(os.path.sep):
            try:
                os.lstat(root_dirname + pathname_part)
            # If an OS-specific exception is raised, its error code
            # indicates whether this pathname is valid or not. Unless this
            # is the case, this exception implies an ignorable kernel or
            # filesystem complaint (e.g., path not found or inaccessible).
            #
            # Only the following exceptions indicate invalid pathnames:
            #
            # * Instances of the Windows-specific "WindowsError" class
            #   defining the "winerror" attribute whose value is
            #   "ERROR_INVALID_NAME". Under Windows, "winerror" is more
            #   fine-grained and hence useful than the generic "errno"
            #   attribute. When a too-long pathname is passed, for example,
            #   "errno" is "ENOENT" (i.e., no such file or directory) rather
            #   than "ENAMETOOLONG" (i.e., file name too long).
            # * Instances of the cross-platform "OSError" class defining the
            #   generic "errno" attribute whose value is either:
            #   * Under most POSIX-compatible OSes, "ENAMETOOLONG".
            #   * Under some edge-case OSes (e.g., SunOS, *BSD), "ERANGE".
            except OSError as exc:
                if hasattr(exc, 'winerror'):
                    if exc.winerror == ERROR_INVALID_NAME:
                        return False
                elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                    return False
    except TypeError as exc:
        return False
    else:
        return True


def createChannelFolder(channelName: str, parentPath, channelId):
    path = os.path.join(parentPath, channelName)
    if is_pathname_valid(path) == False:
        path = os.path.join(parentPath, channelId)
    try:
        os.mkdir(path)
        return path
        # luo csv ja tallenna arvot
    except OSError as error:
        print(error)
        
def createVideoFolder(videoName: str, parentPath: str, id: str):
    path = os.path.join(parentPath, videoName)
    if is_pathname_valid(path) == False:
        path = os.path.join(parentPath, id)
    try:
        print(path,"yritetään")
        os.mkdir(path)
        print(path,"tee")
    except OSError as error: 
        print(error)
        

def moveFiles(from_folder, dest_folder):
    for c_path in os.listdir(from_folder):
        os.rename(os.path.join(from_folder, c_path), os.path.join(dest_folder, c_path))
        # shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

def checkIfExsists(file_path):
    return os.path.exists(file_path)




def getPath(filePath):
    return path.join(path.dirname(path.realpath(__file__)), filePath)

def getFolderPath(folderPath):
    folder = folderPath
    if folder is None:
        folder = ""
    if not folder == "" and folder[len(folder)-1]:
        folder += "/"
    return path.join(path.dirname(path.realpath(__file__)), folder)


def checkFolderPath(filePath):
    if not path.exists(getFolderPath(filePath)): 
        print(filePath,"invalid path")
        return False
    if not access(getFolderPath(filePath), W_OK): 
        print(filePath,"no access")
        return False
    if path.isfile(filePath): 
        print(filePath,"not dir")
        return False
    return True