from yaml import load

import os.path

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class Config(object):
    def __init__(self, args):
        self.git = {
            "buildpackage_options": set(),
            "buildpackage": "buildpackage",
            "buildpackage_environ": {}
            }
        self.dch     = {"dists": {}, 'options': []}
        self.output  = {}
        self.publish = {}
        self.verbose = False

        self.read_default_config()

        self.read_config(args)

        self.verbose = self.verbose | args.verbose
        self.home_dir = args.home_dir[0]

    def read_default_config(self):
        conf_file = "/etc/gbc/gbc.conf"
        if os.path.exists(conf_file):
            self._read_config(file(conf_file, 'r'))

    def read_debian_config(self):
        debian_config = os.path.join(self.home_dir, "debian/gbcrc")
        if os.path.exists(debian_config):
            self._read_config(file(debian_config, 'r'))

    def read_config(self, args):
        if args.config is not None:
            stream = file(args.config[0], 'r')

            self._read_config(stream)

    def _read_config(self, config):
        data = load(config, Loader=Loader)

        if data.has_key('verbose'):
            self.verbose = data['verbose'] | False

        if data.has_key('lib_file'):
            self.lib_file = data['lib_file']

        if data.has_key('git') and isinstance(data['git'], dict):
            if data['git'].has_key('buildpackage'):
                self.git['buildpackage'] = data['git']['buildpackage']
            if data['git'].has_key('buildpackage_options') and isinstance(data['git']['buildpackage_options'], list):
                for i in data['git']['buildpackage_options']:
                    if isinstance(i, str):
                        self.git['buildpackage_options'].add(i)
            if data['git'].has_key('buildpackage_environ') and isinstance(data['git']['buildpackage_environ'], dict):
                for k, v in data['git']['buildpackage_environ'].items():
                    if isinstance(v, str):
                        self.git['buildpackage_environ'][k] = v

        if data.has_key('dch') and isinstance(data['dch'], dict):
            dch = data['dch']
            if dch.has_key('options') and isinstance(dch['options'], list):
                self.dch['options'] = self.dch['options'] + dch['options']
            if dch.has_key('dists') and isinstance(dch['dists'], dict):
                if dch['dists'].has_key('stable'):
                    self.dch['dists']['stable'] = str(dch['dists']['stable'])
                if dch['dists'].has_key('testing'):
                    self.dch['dists']['testing'] = str(dch['dists']['testing'])
                if dch['dists'].has_key('unstable'):
                    self.dch['dists']['unstable'] = str(dch['dists']['unstable'])

        if data.has_key('output') and isinstance(data['output'], dict):
            if data['output'].has_key('stable'):
                self.output['stable'] = str(data['output']['stable'])
            if data['output'].has_key('testing'):
                self.output['testing'] = str(data['output']['testing'])
            if data['output'].has_key('unstable'):
                self.output['unstable'] = str(data['output']['unstable'])

        if data.has_key('publish') and isinstance(data['publish'], dict):
            if data['publish'].has_key('stable'):
                self.publish['stable'] = str(data['publish']['stable'])
            if data['publish'].has_key('testing'):
                self.publish['testing'] = str(data['publish']['testing'])
            if data['publish'].has_key('unstable'):
                self.publish['unstable'] = str(data['publish']['unstable'])


    def __repr__(self):
        return "<gbc.config.Config verbose=%s lib_file=%s gbp=%s gbpoptions=\"%s\" gbpenviron=\"%s\">" % (self.verbose, self.lib_file, self.git['buildpackage'], ' '.join(self.git['buildpackage_options']), self.git["buildpackage_environ"])



# vim: ts=4 sw=4 expandtab:
