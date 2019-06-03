import pkg_resources


def list_packages():
    pkgs = pkg_resources.working_set
    pkgs_list = sorted([f'{i.key}=={i.version}' for i in pkgs])
    print("\n".join(pkgs_list))


if __name__ == '__main__':
    list_packages()
