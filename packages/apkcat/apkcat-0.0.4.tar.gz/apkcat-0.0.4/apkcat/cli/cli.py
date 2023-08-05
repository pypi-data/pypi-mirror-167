import click

from apkcat import __version__
from apkcat.core.main import APKinfo, DEXinfo, check_is_apk, check_is_dex


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
    if check_is_apk(target_file):

        apk_analysis = APKinfo(target_file)

        for item in apk_analysis.get_strings():
            print(item)

    elif check_is_dex(target_file):
        dex_analysis = DEXinfo(target_file)

        for item in dex_analysis.get_strings():
            print(item)

    else:
        print("File Format is wrong")


if __name__ == "__main__":
    entry_point()
