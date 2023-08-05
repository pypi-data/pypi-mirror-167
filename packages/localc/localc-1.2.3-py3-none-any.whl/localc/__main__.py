from .proposition import Proposition
from traitlets.config.loader import Config
from IPython.terminal.embed import InteractiveShellEmbed

if __name__ == '__main__':
    cfg = Config()
    ipshell = InteractiveShellEmbed(
        config=cfg,
        banner1="Localc (Logic Calculator), Version 1.2.3"
    )
    ipshell()
