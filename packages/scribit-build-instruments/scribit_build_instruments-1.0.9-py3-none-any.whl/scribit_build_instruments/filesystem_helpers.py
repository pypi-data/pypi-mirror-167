import os
import logging 
import platform

g_directory_stack = []

def pushd(target):
    g_directory_stack.append(os.path.join(os.path.abspath("."), target))
    os.chdir(target)

def popd():
    if len(g_directory_stack) > 1:
        g_directory_stack.pop(-1)
        os.chdir(g_directory_stack[-1])
    if len(g_directory_stack) == 1:
        os.chdir(g_directory_stack[0])

def create_directory_if_not_exists(path, level=logging.DEBUG):
    logger = logging.getLogger("logger")
    logger.setLevel(level)
    logger.addHandler(logging.StreamHandler())

    exists = os.path.isdir(path)
    if not exists:
        logger.debug(str(path) + " does not exist, creating ...")
        os.makedirs(path) 

def get_cache_directory(level=logging.DEBUG):
    logger = logging.getLogger("logger")
    logger.setLevel(level)
    logger.addHandler(logging.StreamHandler())

    if platform.system().lower() == "windows":
        return os.path.expandvars(R"%localappdata%")
    elif platform.system().lower() == "linux":
        return os.path.expanduser(r"~")
    elif platform.system().lower() == "darwin":
        return os.path.expanduser(r"~")
    
    logger.error("Could not determine platform")
    return ""

def get_git_directory(level=logging.DEBUG):
    logger = logging.getLogger("logger")
    logger.setLevel(level)
    logger.addHandler(logging.StreamHandler())

    logger.debug("Looking for git directory ... ")
    current_working_directory = os.path.normpath(os.getcwd())
    git_directory_name = '.git'
    git_directory = __find_folder_in_current_or_above(git_directory_name, current_working_directory, level)

    logger.info("Git directory found: " + git_directory)
    return git_directory

def get_root_directory(level=logging.DEBUG):
    logger = logging.getLogger("logger")
    logger.setLevel(level)
    logger.addHandler(logging.StreamHandler())

    logger.debug("Looking for root directory ... ( dependant on the git directory )")
    root_directory = os.path.normpath(os.path.join(get_git_directory(level), os.pardir))

    logger.info("Root directory found: " + root_directory)
    return root_directory

def get_source_directory(sourceDirName, level=logging.DEBUG):
    root_dir = get_root_directory(level)
    source_directory = __find_folder_in_current_or_above(sourceDirName, root_dir, level)

    return source_directory

def __find_folder_in_current_or_above(dirname, currentdir, level=logging.DEBUG):
    logger = logging.getLogger("logger")
    logger.setLevel(level)
    logger.addHandler(logging.StreamHandler())

    while_counter = 0
    max_while_counter = 100
    
    logger.debug("Looking for " + dirname)
    
    dirname_target = ""
    active_directory = currentdir

    while dirname_target == "" and while_counter < max_while_counter:
        ## Prevent infinite loop
        sub_folders = __get_subfolders(active_directory)
        while_counter += 1

        # for sf in sub_folders:
        #     print("\tdepth: " , while_counter , "found directories: " , os.path.normpath(sf))

        indices = [i for i, elem in enumerate(sub_folders) if elem.endswith(dirname)]
        if not indices:
            prev_active_directory = active_directory
            active_directory = os.path.join(active_directory, os.pardir)
            active_directory = os.path.normpath(active_directory)
            
            if active_directory == prev_active_directory:
                logger.error("\t\tWe reached the root of our directory")
                logger.error("\t\tCould not find directory " + dirname)
                break

            continue

        dirname_target = sub_folders[indices[0]]
        dirname_target = os.path.normpath(dirname_target)
    
    if dirname_target == "":
        logger.error("\t\tCould not find directory " + dirname +". Max iterations reached(=100)")

    return dirname_target

def __get_subfolders(dirname):
    return [f.path for f in os.scandir(dirname) if f.is_dir()]