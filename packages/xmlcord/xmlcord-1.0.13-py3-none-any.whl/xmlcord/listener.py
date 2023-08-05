import discord
import asyncio

from discord.ext import commands
from types import CoroutineType

from .hooks import HookTrigger
from .hooks import ReactionHook, MessageHook

    
class DiscordListener(commands.Cog):

    active_renderers = []
    bot = None

    def __init__(self, bot=None):
        if bot:
            type(self).bot = bot

    def add_renderer(cls, renderer_to_add):
        for renderer in cls.active_renderers:
            if renderer == renderer_to_add:
                return

        # new renderers get added to the front of the list,
        # this way they have priority when receiving input
        cls.active_renderers.insert(0, renderer_to_add)

    def remove_renderer(cls, renderer_to_remove):
        for index, renderer in enumerate(cls.active_renderers):
            if renderer == renderer_to_remove:
                break
        else:
            return

        cls.active_renderers.pop(index)

    def get_renderers(cls, func) -> []:
        renderers = []

        for renderer in cls.active_renderers:
            if func(renderer):
                renderers.append(renderer)

        return renderers

    async def on_event(cls, trigger, renderer_filter, cleanup):
        resolved_trigger = None

        if trigger.user == cls.bot.user:
            return

        for renderer in cls.get_renderers(renderer_filter):

            # hook matching is now independent of event execution,
            # so we can use it synchronously to check all renderers before resolving the trigger
            if renderer.match_trigger(trigger):
                resolved_trigger = await renderer.resolve_trigger(trigger)
                # comment out if you want a single trigger to affect multiple templates
                break

        # this attempts to delete the reactions even when the template is discarded, 
        # leading to 404 from discord, executing events after cleanup would solve this;
        # might be good now actually
        if resolved_trigger and resolved_trigger.delete_input():
            await cleanup()
        else:
            trigger.resolve()

    def reaction_cleanup(cls, reaction, user):
        async def wrapper():
            await reaction.remove(user)

        return wrapper

    @commands.Cog.listener('on_reaction_add')
    async def on_reaction(cls, reaction: discord.Reaction, user: discord.User):

        trigger = HookTrigger(ReactionHook, data=str(reaction.emoji), user=user)

        await cls.on_event(
            trigger,
            lambda r: reaction.message.id in r.messages, 
            cls.reaction_cleanup(reaction, user)
        )

    def message_cleanup(cls, message):
        async def wrapper():
            await message.delete()

        return wrapper 

    @commands.Cog.listener('on_message')
    async def on_message(cls, message: discord.Message):

        trigger = HookTrigger(MessageHook, data=message.content, user=message.author)

        await cls.on_event(
            trigger,
            lambda r: message.channel.id == r.channel.id, 
            cls.message_cleanup(message)
        )
