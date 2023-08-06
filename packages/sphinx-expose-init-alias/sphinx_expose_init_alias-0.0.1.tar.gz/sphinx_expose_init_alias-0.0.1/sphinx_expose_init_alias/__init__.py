from sphinx_expose_init_alias.documenter import AliasDocumenter
from sphinx_expose_init_alias.documenter import AliasModuleDocumenter


def maybe_skip_member(app, what, name, obj, skip, options):
    if what == 'aliasmodule':
        return False


def setup(app):
    app.setup_extension('sphinx.ext.autodoc')  # Require autodoc extension
    app.add_autodocumenter(AliasDocumenter)
    app.add_autodocumenter(AliasModuleDocumenter)
    app.connect('autodoc-skip-member', maybe_skip_member)