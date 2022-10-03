"""
All rights reserved to Dave™
"""
import argparse
import os

def get_args():
    """
    This simple tool was created to help teams download desired openshift versions,
    and simplify the preparation to the whitening process for them.
    All rights reserved to Dave™
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Process args for usage in the script')
    parser.add_argument(
        '--pull-secret', type=str, required=True,
        help='Pull secret location to pull the openshift version')
    parser.add_argument(
        '--version-path', type=str, required=True,
        help='Where to store the version images')
    parser.add_argument(
        '--ocp-version', type=str, required=True,
        help='The openshift version you are trying to download')
    parser.add_argument(
        '--dry-run', required=False, default=False, action='store_true',
        help='Dry run your image copying process')
    args = parser.parse_args()
    return args

def main():
    """
    All rights reserved to Dave™
    """
    args = get_args()
    if args.dry_run:
        action = ('oc adm release mirror -a %s --to-dir=%s/mirror '
                  'quay.io/openshift-release-dev/ocp-release:%s-x86_64 --dry-run')
    else:
        action = ('oc adm release mirror -a %s --to-dir=%s/mirror '
                  'quay.io/openshift-release-dev/ocp-release:%s-x86_64')
    action = action % (args.pull_secret, args.version_path, args.ocp_version)

    if args.dry_run:
        os.system(action)


if __name__ == "__main__":
    main()
