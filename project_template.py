import os
import re
from dataclasses import dataclass


def show_all_methods(module):
    """
    This method is used to show the methods that are included
    in the library without showing the private mthodd of the module.
    """
    methods = dir(module)
    methods = [i for i in methods if re.match(pattern=r"^[a-z].*", string=i)]
    print(methods)


@dataclass
class ProjectStructureConfig:
    # 1. Enter the root directory of the project in place of project_name_root
    root_dir_path = "project_name_root"

    # 2.0 Enter the directories or the folder names in the root directory and
    # their sub directories some are default
    # eg. 'src' in root, 'src/components' src has components folder in it
    # You can also enter the folder specific file name eg src/file_name.py
    folders = [
        "docs",
        "src",
        "src/components",
        "srci/logs/log/gg.py",
    ]

    # 2.1 You can use this folder creation method instead
    # This can be used instead of the above folders method
    # If you want to create many folders in any folder and
    # dont want to repeat the name of parent
    # folder again and again use the following method
    folders_1 = {
        "docs": [],
        "src": ["components", "__init__.py"],
        "src/components": ["__init__.py"],
        "src/logs": [],
    }

    # 3. Enter the files in the root directory
    # The files that should be present in the root directory of our folder
    files = [
        "README.md",
        "requirements.txt",
        "setup.py",
        ".gitignore",
    ]

    # 4. Enter the allowed extensions here
    # The extensions that need to be used can be set here
    # If you specifiy any extension not in this it will be considered as folder
    extensions = [
        ".py",
        ".md",
        ".txt",
    ]


class MakeProjectStructure:
    def __init__(self):
        self.project_structure = ProjectStructureConfig()
        if not os.path.isdir(
            os.path.join(os.getcwd(), self.project_structure.root_dir_path)
        ):
            os.mkdir(os.path.join(os.getcwd(), self.project_structure.root_dir_path))

    def create_folders(self):
        """
        This function creates the folder and files in the project directory as
        mentioned in the folders [] in ProjectStructureConfig class above

        """

        os.chdir(os.path.join(os.getcwd(), self.project_structure.root_dir_path))
        for folder in self.project_structure.folders:
            os.makedirs(folder, exist_ok=True)
        os.chdir("../")

    def create_files(self):
        """
        This function creates the files that should be in the root directory of the
        Project. The file names are taken from files [] in ProjectStructureConfig class

        """

        for file in self.project_structure.files:
            if not os.path.isfile(
                os.path.join(self.project_structure.root_dir_path, file)
            ):
                with open(
                    os.path.join(self.project_structure.root_dir_path, file), "w"
                ):
                    pass

    def add_init(self, exclude=None):
        """
        This method will add all the __init__.py files to all the folders except for
        the root folder in our project

        """

        for i in os.walk(self.project_structure.root_dir_path):
            if i[0] != self.project_structure.root_dir_path:
                if not exclude is None and os.path.basename(i[0]) not in exclude:
                    with open(os.path.join(i[0], "__init__.py"), "w"):
                        pass

    def create_folders_and_files(self):
        """
        This function also creates the files and folders written in folders_1 []
        in the ProjectStructureConfig class

        """

        os.chdir(self.project_structure.root_dir_path)
        for key in self.project_structure.folders_1.keys():
            os.makedirs(os.path.join(os.getcwd(), key), exist_ok=True)
            if len(self.project_structure.folders_1[key]) > 0:
                for sub_folder in self.project_structure.folders_1[key]:
                    path = os.path.join(key, sub_folder)
                    if os.path.splitext(path)[1] in self.project_structure.extensions:
                        path, file = os.path.split(path)
                        os.makedirs(path, exist_ok=True)
                        with open(os.path.join(path, file), "w"):
                            pass
                    else:
                        os.makedirs(path, exist_ok=True)
        os.chdir("../")


if __name__ == "__main__":
    obj = MakeProjectStructure()

    "Uncomment th follwing if you have added folders and files in folders list[]"
    # obj.create_folders()

    "Uncomments the following if you want to create the structure using folder_1{}"
    obj.create_folders_and_files()

    "Uncomment th follwing if you want to add files in root dir"
    # obj.create_files()

    "Uncomment the following to add __init__.py in all folders except root automatically"
    # obj.add_init(['docs', 'src'])
