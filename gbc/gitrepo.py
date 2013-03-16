
import git
import re

class NotGitRepo(Exception):
    pass

class Repo(object):
    def __init__(self, config):
        self.config = config

        try:
            self.git_repo = git.Repo(self.config.home_dir)
        except git.exc.NoSuchPathError as e:
            raise NotGitRepo("%s is not a git repository" % self.config.home_dir)


        self.tags = self.git_repo.tags
        self.hash_tags = {}
        for i in self.tags:
            self.hash_tags[i.name] = i

        self.branches = self.git_repo.branches
        self.hash_branches = {}
        for i in self.branches:
            self.hash_branches[i.name] = i

    def stable_targets(self):
        targets = set()
        for i in self.tags:
            match = re.match("debian/(([0-9\.]+)-.+)", i.name)
            if match is not None:
                debian_version = match.group(1)
                upstream_version = match.group(2)
                if self.hash_tags.has_key(upstream_version):
                    targets.add(tuple([upstream_version, debian_version]))

        return targets

    def testing_targets(self):
        targets = set()
        for i in self.tags:
            if self.hash_branches.has_key("debian/%s-x" % i.name):
                targets.add(i)

        return targets

    def unstable_targets(self):
        targets = set()
        for i in self.branches:
            if self.hash_branches.has_key("debian/%s" % i.name):
                targets.add(i)

        return targets



# vim: ts=4 sw=4 expandtab:
