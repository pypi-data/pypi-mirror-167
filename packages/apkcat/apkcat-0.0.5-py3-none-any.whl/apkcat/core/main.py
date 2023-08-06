from apkcat.core import check_is_apk, check_is_dex, APKinfo, DEXinfo


def main(file_path):
    if check_is_apk(file_path):

        apk_analysis = APKinfo(file_path)

        for item in apk_analysis.get_strings():
            print(item)

    elif check_is_dex(file_path):
        dex_analysis = DEXinfo(file_path)

        for item in dex_analysis.get_strings():
            print(item)

    else:
        print("File Format is wrong")


if __name__ == "__main__":
    pass
