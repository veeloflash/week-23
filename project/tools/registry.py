class ToolRegistry:
    """Register and execute tools by name without hard-coding workflow calls."""

    def __init__(self):
        self._tools = {}

    def register(self, name, tool):
        self._tools[name] = tool

    def names(self):
        return tuple(self._tools)

    def execute(self, name, method, **kwargs):
        tool = self._tools[name]
        return getattr(tool, method)(**kwargs)