import os
def search_files(path):
    files = [os.path.join(os.path.abspath(path), x) for x in os.listdir(path) if os.path.isfile(x) and x.find(".py") > 0]
    dirs = [os.path.join(os.path.abspath(path), x) for x in os.listdir(path) if os.path.isdir(x)]
    print(files)
    for dir in dirs:
        search_files(dir)
search_files(os.path.abspath(r"D:\Users\gyyin\Desktop\project\py"))