import ast
import inspect
import os
from dataclasses import dataclass
from typing import Optional

from . import globals


@dataclass
class Config():
    # NOTE: should be in sync with ui.run arguments
    host: str = os.environ.get('HOST', '0.0.0.0')
    port: int = int(os.environ.get('PORT', '8080'))
    title: str = 'NiceGUI'
    favicon: str = 'favicon.ico'
    dark: Optional[bool] = False
    reload: bool = True
    show: bool = True
    uvicorn_logging_level: str = 'warning'
    uvicorn_reload_dirs: str = '.'
    uvicorn_reload_includes: str = '*.py'
    uvicorn_reload_excludes: str = '.*, .py[cod], .sw.*, ~*'
    main_page_classes: str = 'q-ma-md column items-start'
    binding_refresh_interval: float = 0.1
    exclude: str = ''


excluded_endings = (
    '<string>',
    'spawn.py',
    'runpy.py',
    os.path.join('debugpy', 'server', 'cli.py'),
    os.path.join('debugpy', '__main__.py'),
    'pydevd.py',
    '_pydev_execfile.py',
)
for f in reversed(inspect.stack()):
    if not any(f.filename.endswith(ending) for ending in excluded_endings):
        filepath = f.filename
        break
else:
    raise Exception('Could not find main script in stacktrace')

try:
    with open(filepath) as f:
        source = f.read()
except FileNotFoundError:
    config = Config()
else:
    for node in ast.walk(ast.parse(source)):
        try:
            func = node.value.func
            if func.value.id == 'ui' and func.attr == 'run':
                args = {
                    keyword.arg:
                        keyword.value.n if isinstance(keyword.value, ast.Num) else
                        keyword.value.s if isinstance(keyword.value, ast.Str) else
                        keyword.value.value
                    for keyword in node.value.keywords
                }
                config = Config(**args)
                globals.pre_evaluation_succeeded = True
                break
        except AttributeError:
            continue
    else:
        config = Config()

os.environ['HOST'] = config.host
os.environ['PORT'] = str(config.port)
os.environ['STATIC_DIRECTORY'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
os.environ['TEMPLATES_DIRECTORY'] = os.path.join(os.environ['STATIC_DIRECTORY'], 'templates')

globals.config = config
