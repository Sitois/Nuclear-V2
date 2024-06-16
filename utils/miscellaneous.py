import random, string, os, json
import discord

import langs
import config_selfbot

from .logger import log

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def random_cooldown(minimum, maximum):
    cooldown = random.randint(minimum * 100000, maximum * 100000) / 100000
    return cooldown


async def save_guild_info(guild: discord.Guild):
    """Save the given guild into ./backups/guild_id.json"""
    guild_info = {
        "id": guild.id,
        "name": guild.name,
        "roles": [],
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
                "hoist": role.hoist
            })

    # Save @everyone's permisions
    guild_info["default_role"] = {
        "permissions": guild.default_role.permissions.value
    }

    # Save guild's channels
    for channel in guild.channels:
        channel_info = {
            "id": channel.id,
            "name": channel.name,
            "type": str(channel.type),
            "position": channel.position,
            "permissions": []
        }

        # Save channel's permissions
        for overwrite in channel.overwrites:
            allow, deny = channel.overwrites[overwrite].pair()
            channel_info["permissions"].append({
                "id": overwrite.id,
                "type": "role" if isinstance(overwrite, discord.Role) else "member",
                "allow": allow.value,
                "deny": deny.value
            })

        guild_info["channels"].append(channel_info)

    # Check if backups folder exists
    if not os.path.exists("backups"):
        log.alert(langs.backup_not_find_folder[config_selfbot.lang])

    # Save guild's infos in a json file
    with open(f"./backups/{guild.id}.json", "w") as f:
        json.dump(guild_info, f, indent=4)

    log.success(f"{langs.backup_success_save[config_selfbot.lang]}: {guild.name}({guild.id}).")