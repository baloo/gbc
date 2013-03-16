import argparse
import sys

import gbc.config
import gbc.gitrepo
import gbc.build


def main():
    """ Gbc entrypoint
    """

    parser = argparse.ArgumentParser(description="Git-buildpackage-continuous")
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--home-dir', metavar="PATH", type=str, 
      nargs=1, help="path to the git directory of your package",
      required=True)
    parser.add_argument('-c', '--config', metavar="CONFIG", type=str, nargs=1,
      help="path to your optional config file")

    args = parser.parse_args()

    config = gbc.config.Config(args)

    try:
        repo = gbc.gitrepo.Repo(config)
    except gbc.gitrepo.NotGitRepo as e:
        print "FATAL: %s" % e.message
        sys.exit(1)


    build = gbc.build.Builder(config, repo)
    build.stable()

    build = gbc.build.Builder(config, repo)
    build.testing()

    build = gbc.build.Builder(config, repo)
    build.unstable()

    #print repo.stable_targets()
    #print repo.testing_targets()
    #print repo.unstable_targets()



# vim: ts=4 sw=4 expandtab:
