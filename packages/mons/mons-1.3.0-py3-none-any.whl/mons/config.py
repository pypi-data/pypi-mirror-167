import configparser
import os
from contextlib import AbstractContextManager

from click import edit
from click import get_app_dir

from mons.install import Install

config_dir = get_app_dir("mons", roaming=False)

CONFIG_FILE = "config.ini"
INSTALLS_FILE = "installs.ini"
CACHE_FILE = "cache.ini"

# Config, Installs, Cache
Config_DEFAULT = {}
Install.DEFAULTS = {
    "PreferredBranch": "stable",
}


def get_default_install():
    return os.environ.get("MONS_DEFAULT_INSTALL", None)


def loadConfig(file, default={}):
    config = configparser.ConfigParser()
    config_file = os.path.join(config_dir, file)
    if os.path.isfile(config_file):
        config.read(config_file)
    else:
        config["DEFAULT"] = default
        os.makedirs(config_dir, exist_ok=True)
        with open(config_file, "x") as f:
            config.write(f)
    return config


def saveConfig(config, file):
    with open(os.path.join(config_dir, file), "w") as f:
        config.write(f)


def editConfig(config: configparser.ConfigParser, file):
    saveConfig(config, file)
    edit(
        filename=os.path.join(config_dir, file),
        editor=config.get("user", "editor", fallback=None),
    )
    return loadConfig(file, config["DEFAULT"])


class UserInfo(AbstractContextManager):
    def __enter__(self):
        self.config = loadConfig(CONFIG_FILE, Config_DEFAULT)
        installs = loadConfig(INSTALLS_FILE)
        cache = loadConfig(CACHE_FILE)

        def load_install(name: str):
            if not cache.has_section(name):
                cache.add_section(name)
            return Install(
                name, installs[name]["Path"], cache=cache[name], data=installs[name]
            )

        self.installs = {name: load_install(name) for name in installs.sections()}
        if not self.config.has_section("user"):
            self.config["user"] = {}
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        saveConfig(self.config, CONFIG_FILE)
        installs = configparser.ConfigParser()
        cache = configparser.ConfigParser()
        for k, v in self.installs.items():
            installs[k] = v.serialize()
            cache[k] = v.cache
        saveConfig(installs, INSTALLS_FILE)
        saveConfig(cache, CACHE_FILE)
