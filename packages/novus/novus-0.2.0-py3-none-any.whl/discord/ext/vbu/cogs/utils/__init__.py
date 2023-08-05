import re as _re
import gettext as _gettext
import typing as _typing

import discord as _discord
from discord.ext import commands as _dpy_commands

from . import checks, converters, errors, menus, types
from .context_embed import Embed
from .custom_bot import MinimalBot, Bot
from .custom_cog import Cog
from .custom_context import Context, AbstractMentionable, PrintContext, SlashContext
from .database import DatabaseWrapper, DatabaseTransaction
from .redis import RedisConnection, RedisChannelHandler, redis_channel_handler
from .statsd import StatsdConnection
from .time_value import TimeValue
from .paginator import Paginator
from .help_command import HelpCommand
from .string import Formatter
from .component_check import component_check, component_id_check
from .embeddify import Embeddify
from .twitch_stream import TwitchStream


__all__ = (
    'checks',
    'converters',
    'errors',
    'menus',
    'types',
    'Embed',
    'MinimalBot',
    'Bot',
    'Cog',
    'Context',
    'AbstractMentionable',
    'PrintContext',
    'SlashContext',
    'DatabaseWrapper',
    'DatabaseTransaction',
    'RedisConnection',
    'RedisChannelHandler',
    'redis_channel_handler',
    'StatsdConnection',
    'TimeValue',
    'Paginator',
    'HelpCommand',
    'Formatter',
    'component_check',
    'component_id_check',
    'Embeddify',
    'TwitchStream',
    'minify_html',
    'translation',
    'format',
    'embeddify',
    'DatabaseConnection',
    'Database',
    'Redis',
    'Stats',
)


_html_minifier = _re.compile(r"\s{2,}|\n")
def minify_html(text: str) -> str:
    return _html_minifier.sub("", text)


def translation(
        ctx: _typing.Union[_dpy_commands.Context, _discord.Interaction, _discord.Locale, str],
        domain: str,
        *,
        use_guild: bool = False,
        **kwargs,
        ) -> _typing.Union[_gettext.GNUTranslations, _gettext.NullTranslations]:
    """
    Get a translation table for a given domain with the locale
    stored in a context.

    Examples
    ----------
    >>> # This will get the locale from your context,
    >>> # and will get the translation from the "errors" file.
    >>> vbu.translation(ctx, "errors").gettext("This command is currently unavailable")

    Parameters
    -----------
    ctx: Union[:class:`discord.ext.commands.Context`, :class:`discord.Interaction`, :class:`discord.Locale`, :class:`str`]
        The context that you want to get the translation within, or
        the name of the locale that you want to get anyway.
    domain: :class:`str`
        The domain of the translation.
    use_guild: :class:`bool`
        Whether or not to prioritize the guild locale over the user locale.

    Returns
    --------
    Union[:class:`gettext.GNUTranslations`, :class:`gettext.NullTranslations`]
        The transation table object that you want to ``.gettext`` for.
    """

    if isinstance(ctx, (_dpy_commands.Context, _discord.Interaction)):
        languages = [ctx.locale, ctx.locale.split("-")[0]]
        if use_guild and ctx.guild and ctx.guild_locale:
            languages = [ctx.guild_locale, ctx.guild_locale.split("-")[0], *languages]
    elif isinstance(ctx, _discord.Locale):
        languages = [ctx.value, ctx.value.split("-")[0]]
    elif isinstance(ctx, str):
        languages = [ctx]
    else:
        raise TypeError()
    return _gettext.translation(
        domain=domain,
        localedir=kwargs.get("localedir", "./locales"),
        languages=languages,
        fallback=kwargs.get("fallback", True),
    )


format = Formatter().format
embeddify = Embeddify.send
DatabaseConnection = DatabaseWrapper
Database = DatabaseWrapper
Redis = RedisConnection
Stats = StatsdConnection
