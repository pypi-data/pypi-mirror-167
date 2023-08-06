import click

from apkcat import __version__
from apkcat.core import main


@click.version_option(version=__version__)
@click.command(no_args_is_help=True)
@click.option(
    "-f",
    "--target_file",
    is_flag=False,
    help="APK or DEX file",
)
def entry_point(target_file):
    """APKCAT"""

    main(target_file)


if __name__ == "__main__":
    entry_point()
