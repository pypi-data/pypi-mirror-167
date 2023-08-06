import os
import yaml
import re
import shutil


VERSION_FILES = [ 
    { 
        "file": "src/extension.yml", 
        "format": "yml",
        "location": "extension.version"
    },
    { 
        "file": "script.yml", 
        "format": "yml",
        "location": "script.version"
    },
    { 
        "file": "src/extension.py", 
        "format": "regex",
        "location": r"^\s*(gl_version|version|__version__)\s*=\s*[\"']+([^\"']+)[\"']+",
        "group": 2
    },
    { 
        "file": "src/__init__.py", 
        "format": "regex",
        "location": r"^\s*(gl_version|version|__version__)\s*=\s*[\"']+([^\"']+)[\"']+",
        "group": 2
    },
    { 
        "file": "src/templates/scriptUnix", 
        "format": "regex",
        "location": r"^\s*(gl_version|version|__version__)\s*=\s*[\"']+([^\"']+)[\"']+",
        "group": 2
    },
    { 
        "file": "src/templates/scriptWindows", 
        "format": "regex",
        "location": r"^\s*(gl_version|version|__version__)\s*=\s*[\"']+([^\"']+)[\"']+",
        "group": 2
    },
    { 
        "file": "src/templates/script", 
        "format": "regex",
        "location": r"^\s*(gl_version|version|__version__)\s*=\s*[\"']+([^\"']+)[\"']+",
        "group": 2
    }
]

def safeget(dct, *keys):
    for key in keys:
        try:
            dct = dct[key]
        except KeyError:
            return None
    return dct

def safeset(dct, value, *keys):
    _dct = dct
    for key in keys[:-1]:
        try:
            dct = dct[key]
        except KeyError:
            return None
    dct[keys[-1]] = value
    return _dct

def find_current_version(version_files=None):
    versions = []
    if version_files is None:
        version_files = VERSION_FILES
    for file_desc in version_files:
        file_path = file_desc["file"]
        if os.path.exists(file_path):
            format =  file_desc.get("format")
            if format in ["yaml", "yml"]:
                location = file_desc.get("location", "").split(".")
                with open(file_path) as f:
                    conf = yaml.safe_load(f)
                    _version = safeget(conf, *location)
                    print(f"{file_path} : {_version}")
                    if _version not in versions:
                        versions.append(_version)
            elif format in ["py", "python", "script", "regex", "regexp"]:
                location = file_desc.get("location", "")
                group = file_desc.get("group", 1)
                with open(file_path) as f:
                    content = f.read()
                regex = re.compile(location, re.MULTILINE)
                matches = regex.finditer(content)
                for match in matches:
                    _version = match.group(group)
                    print(f"{file_path} : {_version}")
                    if _version not in versions:
                        versions.append(_version)

    _versions = set(versions)
    if len(_versions) > 1:
        print(f"There are multiple versions: {_versions}")
    
    return list(_versions)

def get_new_version(method, version):
    _version = version.split(".")
    release, major, minor = [1,0,0]
    if len(_version) > 0:
        release = int(_version[0])
    
    if len(_version) > 1:
        major = int(_version[1])

    if len(_version) > 2:
        minor = int(_version[2])

    if method == "release":
        release += 1
        major = 0
        minor = 0
    elif method == "major":
        major += 1
        minor = 0
    else:
        minor += 1
    
    return f"{release}.{major}.{minor}"


def update_version(old_version, new_version, version_files=None):
    versions = []
    update = False
    if version_files is None:
        version_files = VERSION_FILES
    for file_desc in version_files:
        file_path = file_desc["file"]
        if os.path.exists(file_path):
            format =  file_desc.get("format")
            if format in ["yaml", "yml"]:
                location = file_desc.get("location", "").split(".")
                with open(file_path) as f:
                    conf = yaml.safe_load(f)

                _version = safeget(conf, *location)
                if _version == old_version:
                    conf = safeset(conf, new_version, *location)
                    with open(file_path, "w") as f:
                        yaml.dump(conf, f, sort_keys=False)
                        print(f"{file_path} : {old_version} -> {new_version}")

            elif format in ["py", "python", "script", "regex", "regexp"]:
                location = file_desc.get("location", "")
                group = file_desc.get("group", 1)
                with open(file_path) as f:
                    content_lines = f.readlines()
                
                content = "\n".join(content_lines)
                regex = re.compile(location, re.MULTILINE)
                matches = regex.search(content)
                if matches is None:
                    print(f"skipping {file_path}")
                    continue

                new_file_path = file_path + ".tmp"
                with open(new_file_path, "w") as f:
                    for line in content_lines:
                        match = regex.search(line)
                        if match is not None:
                            _version = match.group(group)
                            if _version == old_version:
                                line = line.replace(old_version, new_version)
                                print(f"{file_path} : {old_version} -> {new_version}")
                
                        f.write(line)

                shutil.move(file_path, file_path + ".bckp")
                os.rename(new_file_path, file_path)
