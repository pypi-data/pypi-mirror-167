from pathlib import Path

import click

path_project = Path()
# path_component = path_project.absolute()

help_op = {
    "help": [
        "Name of the application!",
        "Template of the application! Ex: react-ts (default) or react",
        "Style of the application! Ex: styled-components (default) or tailwindcss"
    ]
}


@click.group()
def rpx():
    pass


@click.command(name="vite")
@click.option(
    "-n",
    "--name",
    prompt="Enter name",
    default="app",
    help=help_op["help"][0]
)
@click.option(
    "-t",
    "--template",
    prompt="Enter template",
    default="react-ts",
    help=help_op["help"][1]
)
@click.option(
    "-s",
    "--style",
    prompt="Enter type style",
    default="styled-components",
    help=help_op["help"][2]
)
def create_project(name, template, style):
    from os import system
    create = f"yarn create vite {name} --template {template} || npm init vite@latest {name} -- --template {template}"
    delete_files = f"cd {name} && rm -r public && cd src && unlink App.css && cd assets && unlink react.svg"
    if style == "tailwindcss":
        initialize = f"cd {name} && yarn || npm install && yarn add -D {style} postcss autoprefixer || npm install -D {style} postcss autoprefixer && npx tailwindcss init"
    else:
        if template == "react-ts":
            initialize = f"cd {name} && yarn || npm install && yarn add {style} @types/{style} || npm install {style} @types/{style}"
        else:
            initialize = f"cd {name} && yarn || npm install && yarn add {style} || npm install {style}"

    system(create)
    system(delete_files)
    system(initialize)


@click.command(name="component")
@click.option("-n", "--name", prompt="Enter component name", help="Name of the component")
def create_component(name):
    from os import makedirs

    src = path_project / "src"
    suffix_file = list(src.glob("main.*"))[0].suffix

    def write_file(name: str, file: Path):
        with file.open("a+") as fw:
            fw.write("// import * as S from './styles';\n\n")
            fw.write(f"export const {name} = () => {{\n")
            fw.write("  return (\n")
            fw.write("      <div>\n")
            fw.write("      </div>\n")
            fw.write("  )\n")
            fw.write("}\n")

    def c_files(name: str, path: Path, suffix: str):
        file = path / f"index.{suffix}"
        file.touch()
        write_file(name, file)

    def c_component(name: str, path: Path, suffix: str):
        component_name = name.capitalize()
        # component_path = f"{path}/src/components/{component_name}"
        component_path = path / "src" / "components" / component_name
        makedirs(component_path)
        c_files(component_name, component_path, suffix)

    c_component(name, path_project, suffix_file)


rpx.add_command(create_project)
rpx.add_command(create_component)
