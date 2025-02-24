from pathlib import Path
import tests


def path_schemas(file_name):
    return str(Path(tests.__file__).parent.parent.joinpath(f'json/schema/{file_name}'))


def path_resources(file_name):
    return str(Path(tests.__file__).parent.parent.joinpath(f'json/resources/{file_name}'))