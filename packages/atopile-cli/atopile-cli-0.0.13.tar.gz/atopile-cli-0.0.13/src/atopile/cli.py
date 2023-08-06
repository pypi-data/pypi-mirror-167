import json
import logging
from pathlib import Path
from typing import List

import click

from . import build, options, stages, utils, git_resource
from .lib import add_lib

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def ensure_dir(dir: Path):
    if not dir.exists():
        dir.mkdir(parents=True)
        log.info(f'creating {str(dir)}')

@click.group()
@click.option('--options', '-o', 'options_list', multiple=True)
def cli(options_list: List[str]):
    if options_list:
        options_dict = {}
        for option in options_list:
            k, v = option.split('=', 1)
            v = v.strip('"\' \t\n')
            options_dict[k] = v
        options.update_options(options_dict, options.Level.CLI_OPTION)

@cli.command('options')
def cli_print_options():
    """Show information about configuration options available."""
    print(utils.reindent_str(
        """
        Configuration options.

        Settable via `-o/--options option=value` after `ato`, environment variables, etc...
        In order of increasing precedance:
        """,
        indent = 4
    ))
    for level in options.Level:
        print(f'     - {level.name}')
    print()
    options.print_options()

@cli.command('run')
@click.argument('task')
@options.project_dir.as_click_arg(required=False)
def cli_build(project_dir, task):
    """Build your project."""
    options.project_dir.set_value(project_dir, options.Level.CLICK_OPTION)

    try:
        build.build(task)
    except utils.AtopileError:
        exit(1)
    
@cli.group('lib')
def lib():
    pass

@lib.command('add')
@click.argument('repo')
@options.project_dir.as_click_arg()
@click.option('--subproject', default='*', help='subproject to add the dependency to, else it\'s added to all. Glob matches .kicad_pro files')
def cli_add_lib(repo, project_dir, subproject):
    """Add a new library to the project's dependencies."""
    options.project_dir.set_value(project_dir, options.Level.CLICK_OPTION)
    add_lib(repo, subproject)
    
@cli.group('stage-def')
def stage_def():
    pass

@stage_def.command('add')
@click.argument('path', required=False)
def cli_stage_def_add(path):
    """Add a search path to stages."""
    if not path:
        path = Path('.')
    if Path(path).exists() and not Path(path).is_dir():
        path = Path(path).parent
    
    stage_def_repo_store = git_resource.GitRepoStore(options.stage_def_dir.value).load()
    stage_def_repo_store.add(str(path))

@stage_def.command('replace')
@click.argument('path', required=False)
def cli_stage_def_replace(path):
    """Add a search path to stages."""
    if not path:
        path = Path('.')
    if Path(path).exists() and not Path(path).is_dir():
        path = Path(path).parent

    stage_def_repo_store = git_resource.GitRepoStore(options.stage_def_dir.value).load()
    stage_def_repo_store.replace(str(path))

@stage_def.command('update')
def cli_stage_def_scan_local():
    """Add a search path to stages."""
    stage_def_repo_store = git_resource.GitRepoStore(options.stage_def_dir.value).load()
    for entry in stage_def_repo_store.entries:
        entry.update()

if __name__ == '__main__':
    cli()
