import click

from apkcat import __version__
from apkcat.core.main import APKinfo


@click.version_option(version=__version__)
@click.command(no_args_is_help=True)
@click.option(
    "-a",
    "--apk",
    is_flag=False,
    help="APK file",
)
def entry_point(apk):
    """APKCAT"""
    analysis = APKinfo(apk)

    for item in analysis.get_strings():
        print(item)


if __name__ == "__main__":
    entry_point()
