import os
import jinja2
import pkginfo
from fat_wheel.parse.py_file import get_py_file_meta_data, SetupPyArg

TEMPLATE_FOLDER = os.path.join(os.path.dirname(__file__), "template")
TEMPLATE_FILE = "setup.txt"


def generator(options, build_path=""):
    try:
        before_setups = options.pop(0)
        after_setups = options.pop(-1)
        template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATE_FOLDER)
        template_env = jinja2.Environment(loader=template_loader)
        template = template_env.get_template(TEMPLATE_FILE)
        output_text = template.render(before_setups=before_setups,
                                      options=options,
                                      after_setups=after_setups)
        with open(os.path.join(build_path, "setup.py"), mode="w") as s:
            s.write(output_text)
    except Exception as e:
        raise e


def generate_setup_py(fat_wheel_build_path, root_dir, pkg_name):
    meta_data = get_py_file_meta_data(os.path.join(root_dir, "setup.py"))
    default_package_data = True
    default_entry_points = True
    for meta in meta_data:
        if meta.arg == "package_data":
            default_package_data = False
            package_data_dict = meta.value
            pkg_data = ["deps/*"]
            if pkg_name in package_data_dict:
                pkg_data.extend(package_data_dict.get(pkg_name))
            package_data_dict[pkg_name] = pkg_data
        if meta.arg == "entry_points":
            default_entry_points = False
            entry_points_list = meta.value.get("console_scripts")
            entry_points = [f"{pkg_name} = {pkg_name}.runner:install"]
            entry_points_list.extend(entry_points)

    if default_entry_points:
        entry_points_dict = {"console_scripts": [f"{pkg_name} = {pkg_name}.runner:install"]}
        pkg = SetupPyArg("entry_points", entry_points_dict, "dict", 0, 0)
        meta_data.insert(-1, pkg)

    if default_package_data:
        package_data_dict = {pkg_name: ["deps/*"]}
        pkg = SetupPyArg("package_data", package_data_dict, "dict", 0, 0)
        meta_data.insert(-1, pkg)

    for m in meta_data:
        if m.arg == "before_setup" or m.arg == "after_setup":
            tmp = []
            for g in m.value:
                if g != "\n":
                    tmp.append(g[:-1])
            m.value = tmp
    # extra_options = [[[pkg_name, '"deps/*"']], [f"{pkg_name} = {pkg_name}.runner:install"]]
    generator(meta_data, build_path=fat_wheel_build_path)


def __data_files():
    all_deps = os.scandir("test_project/deps")
    all_wheel = [f'deps/{dep.name}' for dep in all_deps]
    data_files = ["data_files", f'[("deps", ({str(all_wheel)[1:-1]}))]', object]
    return data_files


def get_version(root_dir):
    """refactor it please"""
    meta_data = get_py_file_meta_data(os.path.join(root_dir, "setup.py"))
    for key in meta_data:
        if "version" in key.arg:
            return key.value


def copy_installer(dest):
    try:
        template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATE_FOLDER)
        template_env = jinja2.Environment(loader=template_loader)
        template = template_env.get_template("runner.py")
        dest_list = []
        for i in os.scandir(os.path.join(dest, "deps")):
            dest_list.append(pkginfo.get_metadata(i.path).name)
        output_text = template.render(dep_list=str(dest_list))  # this is where to put args to the template renderer
        with open(os.path.join(dest, "runner.py"), mode="w") as s:
            s.write(output_text)
    except Exception as e:
        raise e
