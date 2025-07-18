from importlib.metadata import version as get_version

if __package__:
    __version__ = get_version(__package__)
else:
    __version__ = "0.0.0"
