from fat_wheel.cmd.pip import download_wheel, build
from fat_wheel.fs import copy, copy2, create_dirs
from fat_wheel.gen import generate_setup_py, copy_installer, get_version
from fat_wheel.parse.config import get_ignore_files
from fat_wheel.project_model import ProjectBuilder
from fat_wheel.utils import now, joinpath, scandir, chdir, isdir

DIST = "dist"
BUILD = "build"


def move_dist(project):
    dst = joinpath(project.root_dir, DIST, project.version)
    copy2(DIST, dst, dirs_exist_ok=True)


def process(project_dir, options):
    project = ProjectBuilder.builder().build_by_path(project_dir=project_dir).build()
    project.set_version(version=get_version(project.root_dir))
    print(project.__dict__)
    if project.is_root:
        fat_wheel_build = f"{project.name}-v{project.version}-{now()}"
        fat_wheel_build_path = joinpath(project.root_dir, BUILD, fat_wheel_build)
        create_dirs(fat_wheel_build_path)
        ignored_files = get_ignore_files(project.fat_config_yml)
        print(f"Ignored files/folder: {ignored_files}")
        required_files = list(scandir(project.root_dir))
        print(f"creating project local copy in build/{fat_wheel_build}")
        for file in required_files:
            if file.name not in ignored_files:
                print(file.path)
                if isdir(file.path):
                    dst = joinpath(fat_wheel_build_path, file.name)
                    copy2(src=file.path, dst=dst)
                else:
                    copy(src=file.path, dst=fat_wheel_build_path)
        print(f"chdir: {fat_wheel_build_path}")
        chdir(fat_wheel_build_path)
        download_wheel(project.pkg_name)
        copy_installer(project.pkg_name)
        generate_setup_py(fat_wheel_build_path, project.root_dir, project.pkg_name)
        build(options)
        move_dist(project)
