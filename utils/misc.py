import random, string, os, json, asyncio

import discord

from .logger import log
from .lang_manager import lang

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def random_cooldown(minimum: float, maximum: float) -> float:
    min_ms = int(minimum * 1000)
    max_ms = int(maximum * 1000)
    return random.randint(min_ms, max_ms) / 1000


async def save_guild(guild: discord.Guild,
                     channels):
    """|coro|

    Save the given guild into ./backups/guild_id.json
    
    Parameters
    ----------
    guild: :class:`discord.Guild`
        The guild object to save.
    channels: Sequence[:class:`discord.abc.GuildChannel`]
        Commonly given from `discord.Guild.channels`.
    """

    log.separate_text(lang.text('creating_backup'))
    guild_info = {
        "id": guild.id,
        "name": guild.name,
        "roles": [],
        "categories": [],
        "channels": []
    }

    # Save guild's roles
    for role in guild.roles:
        if not role.is_integration() and role != guild.default_role:
            guild_info["roles"].append({
                "id": role.id,
                "name": role.name,
                "permissions": role.permissions.value,
                "color": role.color.value,
                "mentionable": role.mentionable,
                "hoist": role.hoist,
                "position": role.position
            })
            log.success(f"{lang.text('save_role_success')} {role.name}({role.id}) {lang.text('from')} {guild.name}({guild.id}).")

    # Save @everyone's permissions
    guild_info["default_role"] = {
        "permissions": guild.default_role.permissions.value
    }
    log.success(f"{lang.text('save_everyone_success')} {guild.name}({guild.id}).")

    # Save guild's categories
    for category in guild.categories:
        guild_info["categories"].append({
            "id": category.id,
            "name": category.name,
            "position": category.position
        })
        log.success(f"{lang.text('save_category_success')} {category.name}({category.id}) {lang.text('from')} {guild.name}({guild.id}).")

    # Save guild's channels
    for channel in channels:
        if isinstance(channel, discord.Thread):
            continue  # Skip threads

        channel_info = {
            "id": channel.id,
            "name": channel.name,
            "type": str(channel.type),
            "position": channel.position,
            "category": channel.category_id,
            "permissions": []
        }
        log.success(f"{lang.text('save_channel_success')} {channel.name}({channel.id}) {lang.text('from')} {guild.name}({guild.id}).")

        # Save channel's permissions, excluding user permissions
        for overwrite in channel.overwrites:
            if isinstance(overwrite, discord.Role) or overwrite == guild.default_role:
                allow, deny = channel.overwrites[overwrite].pair()
                channel_info["permissions"].append({
                    "id": overwrite.id,
                    "type": "role" if isinstance(overwrite, discord.Role) else "@everyone",
                    "allow": allow.value,
                    "deny": deny.value
                })
        log.success(f"{lang.text('save_role_permission_success')} {channel.name}({channel.id}) {lang.text('from')} {guild.name}({guild.id}).")

        guild_info["channels"].append(channel_info)

    # Check if 'backups' folder exists
    if not os.path.exists("backups"):
        os.makedirs("backups")
        log.alert(lang.text('save_folder_created'))

    # Save guild's infos in a json file
    with open(f"./backups/{guild.id}.json", "w") as f:
        json.dump(guild_info, f, indent=4)

    log.success(f"{lang.text('save_guild_success')} {guild.name}({guild.id}).")
    log.separate(lang.text('creating_backup'))


async def load_guild(guild: discord.Guild,
                     channels,
                     backup,
                     minimal_cooldown,
                     maximum_cooldown):
    """|coro|

    Load the given guild into the chosen guild.

    Parameters
    ----------
    guild: :class:`discord.Guild`
        The guild to load.
    channels: Sequence[:class:`discord.abc.GuildChannel`]
        Commonly given from `discord.Guild.channels`.
    backup: :class:`dict`
        The backup to load from.
    minimal_cooldown: :class:`int`
        The minimal cooldown for the random load cooldown.
    miximum_cooldown: :class:`int`
        The maximal cooldown for the random load cooldown.
    """

    log.separate_text(lang.text('loading_backup'))
    # Delete old channels
    for channel in channels:
        try:
            await channel.delete()
            log.success(f"{lang.text('load_delete_channel_success')} {channel.name}({channel.id}) {lang.text('for')} {guild.name}({guild.id}).")
            await asyncio.sleep(random_cooldown(0.8, 10.3))  # Wait to avoid rate limit
        except Exception as e:
            log.fail(f"{lang.text('load_delete_channel_fail')} {channel.name}({channel.id}): {e}")

    # Delete old roles (not @everyone, not bot roles)
    for role in guild.roles:
        if role.name != "@everyone" and not role.is_integration():
            try:
                await role.delete()
                log.success(f"{lang.text('load_delete_role_success')} {role.name}({role.id}) {lang.text('for')} {guild.name}({guild.id}).")
                await asyncio.sleep(random_cooldown(0.7, 7.6))  # Wait to avoid rate limit
            except Exception as e:
                log.fail(f"{lang.text('load_delete_role_fail')} {role.name}: {e}")

    # Delete old categories
    for category in guild.categories:
        try:
            await category.delete()
            log.success(f"{lang.text('load_delete_category_success')}: {category.name}({category.id}) {lang.text('for')} {guild.name}({guild.id}).")
            await asyncio.sleep(random_cooldown(0.8, 6.2))  # Wait to avoid rate limit
        except Exception as e:
            log.fail(f"{lang.text('load_delete_category_fail')}: {role.name}: {e}")

    # Add backup's roles
    role_map = {}
    for role_info in backup["roles"]:
        new_role = await guild.create_role(
            name=role_info["name"],
            permissions=discord.Permissions(role_info["permissions"]),
            color=discord.Color(role_info["color"]),
            mentionable=role_info["mentionable"],
            hoist=role_info["hoist"]
        )
        role_map[role_info["id"]] = new_role
        log.success(f"{lang.text('load_create_role_success')} {role_info['name']}({role_info['id']}) {lang.text('for')} {guild.name}({guild.id}).")
        await asyncio.sleep(random_cooldown(minimal_cooldown, maximum_cooldown))  # Wait to avoid rate limit

    # Adjust role positions
    for role_info in backup["roles"]:
        role = role_map.get(role_info["id"])
        if role:
            await role.edit(position=role_info["position"])
            log.success(f"{lang.text('load_role_position_success')} {role_info['name']}({role_info['id']}) {lang.text('for')} {guild.name}({guild.id}).")
            await asyncio.sleep(random_cooldown(minimal_cooldown, maximum_cooldown))  # Wait to avoid rate limit

    # Add backup's categories
    category_map = {}
    for category_info in backup["categories"]:
        new_category = await guild.create_category(
            name=category_info["name"],
            position=category_info["position"]
        )
        category_map[category_info["id"]] = new_category.id
        log.success(f"{lang.text('load_create_category_success')} {category_info['name']}({category_info['id']}) {lang.text('for')} {guild.name}({guild.id}).")
        await asyncio.sleep(random_cooldown(minimal_cooldown, maximum_cooldown))  # Wait to avoid rate limit

    # Add backup's channels
    for channel_info in backup["channels"]:
        overwrites = {}
        for perm in channel_info["permissions"]:
            target = guild.get_role(perm["id"]) if perm["type"] == "role" else guild.default_role
            if target:
                overwrites[target] = discord.PermissionOverwrite.from_pair(
                    discord.Permissions(perm["allow"]),
                    discord.Permissions(perm["deny"])
                )

        category = guild.get_channel(category_map[channel_info["category"]]) if channel_info["category"] else None
        channel_type = discord.ChannelType[channel_info["type"]]

        if channel_type == discord.ChannelType.text:
            await guild.create_text_channel(
                name=channel_info["name"],
                position=channel_info["position"],
                overwrites=overwrites,
                category=category
            )
        elif channel_type == discord.ChannelType.voice:
            await guild.create_voice_channel(
                name=channel_info["name"],
                position=channel_info["position"],
                overwrites=overwrites,
                category=category
            )
        elif channel_type == discord.ChannelType.stage_voice:
            await guild.create_stage_channel(
                name=channel_info["name"],
                position=channel_info["position"],
                overwrites=overwrites,
                category=category
            )
        elif channel_type == discord.ChannelType.forum:
            await guild.create_forum(
                name=channel_info["name"],
                position=channel_info["position"],
                overwrites=overwrites,
                category=category
            )
        else:
            pass