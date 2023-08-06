# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2022 Scipp contributors (https://github.com/scipp)

try:
    from ipywidgets import Widget
except ImportError:
    Widget = None


class Displayable:

    if hasattr(Widget, '_repr_mimebundle_'):

        def _repr_mimebundle_(self, include=None, exclude=None):
            """
            Mimebundle display representation for jupyter notebooks.
            """
            return self.to_widget()._repr_mimebundle_(include=include, exclude=exclude)
    else:

        def _ipython_display_(self):
            """
            IPython display representation for Jupyter notebooks.
            """
            return self.to_widget()._ipython_display_()
