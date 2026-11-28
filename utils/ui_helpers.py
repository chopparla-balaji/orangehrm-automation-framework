class UiHelpers:

    @staticmethod
    def format_locator_text(locator: tuple[str, str], kwargs: dict[str, str]) -> tuple[str, str]:
        """Format locator with dynamic values."""
        return locator[0], locator[1].format(**kwargs)