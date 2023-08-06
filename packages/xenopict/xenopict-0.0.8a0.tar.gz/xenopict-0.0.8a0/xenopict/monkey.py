from __future__ import annotations
import aspectlib


class Patch:
    _installed = False

    def __enter__(self):
        self.install()

    def __exit__(self, *args, **kwargs):
        self.uninstall()

    def install(self):
        pass

    def uninstall(self):
        pass


class Patcher(Patch):
    def __init__(self, patches: list[Patch] | None = None):
        self.patches: list[Patch] = [] if patches is None else patches

    def append(self, patch: Patch) -> None:
        self.patches.append(patch)

    def replace(self, obj, attr, new):
        self.append(Replace(obj, attr, new))

    def install(self):
        if not self._installed:
            for p in self.patches:
                p.install()
        self._installed = True

    def uninstall(self):
        if self._installed:
            for p in reversed(self.patches):
                p.uninstall()
        self._installed = False


class Replace(Patch):
    _ABSENT = []

    def __init__(self, obj, attr, replace_with):
        self.obj = obj
        self.attr = attr
        self.replace_with = replace_with
        self.absent = None

    def uninstall(self):
        if not self._installed:
            return

        if self.orig is self._ABSENT:
            if self.attr in self.obj.__dict__:
                del self.obj.__dict__[self.attr]
        else:
            self.obj.__dict__[self.attr] = self.orig

        del self.orig
        self._installed = False

    # def wrap(self, replace_with):
    #    return replace_with

    def install(self):
        if self._installed:
            return

        self.orig = self.obj.__dict__.get(self.attr, self._ABSENT)

        # wrap = self.wrap(self.replace_with)
        self.obj.__dict__[self.attr] = self.replace_with
        self._installed = True


class Wrap(Replace):
    def wrap(self, replace_with):
        return replace_with(self.orig)
