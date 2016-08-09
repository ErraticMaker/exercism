from invoke import task
#!/usr/bin/env invoke
"""Tasks automation script"""
import os
from itertools import chain
from invoke import task


def _files_ending(path, ending, exception=''):
    ending_lower = ending.lower()
    filepaths = (os.path.join(dirpath, filename) for (dirpath, _, filenames)
                 in os.walk(path) for filename in filenames
                 if filename.lower().endswith(ending_lower))
    if exception != '':
        exception_lower = exception.lower()
        return (filepath for filepath in filepaths
                if not filepath.lower().endswith(exception_lower))
    return filepaths


def _find_test_file(path):
    if os.path.isdir(path):
        return _files_ending(path, 'test.py')
    return iter((path,))


def _find_readme_file(path):
    if os.path.isdir(path):
        return chain(_files_ending(path, 'readme.md'),
                     _files_ending(path, 'readme.markdown'))
    return iter((path,))


def _find_exercise_file(path):
    if os.path.isdir(path):
        return _files_ending(path, '.py', 'test.py')
    return iter((path,))


def _default_filename(exercise):
    if os.path.isdir(exercise):
        return os.path.join(exercise, '.'.join((exercise, 'py')))
    return exercise


def _get_editor():
    return os.environ.get('EDITOR', 'nano')


@task
def clean(ctx):
    """Clean"""
    ctx.run('rm -rf **/*.pyc **/__pycache__')


@task
def test(ctx, exercise, pep8=True):
    flags = '--color=yes -x --ff'
    if pep8:
        flags = flags + ' --pep8'
    test_files = ' '.join(_find_test_file(exercise))
    ctx.run('py.test {} {}'.format(flags, test_files))
