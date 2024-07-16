import random, string, os, json, asyncio

import discord

import config_selfbot

from .logger import log


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def random_cooldown(minimum, maximum):
    cooldown = random.randint(minimum * 100000, maximum * 100000) / 100000
    return cooldown


# -- Save logs --


#######################
#  save              #
#    backup     !!!  #
#######################

creating_backup = {
    "fr": "CREATING BACKUP",
    "en": "CRÉATION DE LA BACKUP"
}

save_everyone_success = {
    "fr": "Rôle @everyone sauvegardé avec succès",
    "en": "Successfully saved @everyone role from"
}

save_role_success = {
    "fr": "Rôle sauvegardé avec succès:",
    "en": "Successfully saved role:"
}

save_guild_success = {
    "fr": "Serveur sauvegardé avec succès:",
    "en": "Successfully saved guild:"
}
save_role_permission_success = {
    "fr": "Permissions du rôle sauvegardé avec succès pour",
    "en": "Successfully saved role permissions for"
}

save_folder_not_found = {
    "fr": "Impossible de trouver le dossier 'backups' !",
    "en": "Can't find the 'backups' folder!"
}

_from = {
    "fr": "depuis",
    "en": "from"
}

async def save_guild(guild: discord.Guild,
                     channels):
    """|coro|

    Save the given guild into ./backups/guild_id.json
    
    Parameters:
    -----------
    guild: :class:`discord.Guild`
        The guild object to save.
    channels: Sequence[:class:`discord.abc.GuildChannel`]
        Commonly given from `discord.Guild.channels`."""

    log.separate_text(creating_backup[config_selfbot.lang])
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
            log.success(f"{save_role_success[config_selfbot.lang]} {role.name}({role.id}) {_from[config_selfbot.lang]} {guild.name}({guild.id}).")

    # Save @everyone's permissions
    guild_info["default_role"] = {
        "permissions": guild.default_role.permissions.value
    }
    log.success(f"{save_everyone_success[config_selfbot.lang]} {guild.name}({guild.id}).")

    # Save guild's categories
    for category in guild.categories:
        guild_info["categories"].append({
            "id": category.id,
            "name": category.name,
            "position": category.position
        })
        log.success(f"Successfully saved category: {category.name}({category.id}) {_from[config_selfbot.lang]} {guild.name}({guild.id}).")

    # Save guild's channels
    for channel in channels:
        channel_info = {
            "id": channel.id,
            "name": channel.name,
            "type": str(channel.type),
            "position": channel.position,
            "category": channel.category_id,
            "permissions": []
        }
        log.success(f"Successfully saved channel: {channel.name}({channel.id}) {_from[config_selfbot.lang]} {guild.name}({guild.id}).")

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
        log.success(f"{save_role_permission_success[config_selfbot.lang]} {channel.name}({channel.id}) {_from[config_selfbot.lang]} {guild.name}({guild.id}).")

        guild_info["channels"].append(channel_info)

    # Check if 'backups' folder exists
    if not os.path.exists("backups"):
        log.alert(save_folder_not_found[config_selfbot.lang])
        return

    # Save guild's infos in a json file
    with open(f"./backups/{guild.id}.json", "w") as f:
        json.dump(guild_info, f, indent=4)

    log.success(f"{save_guild_success[config_selfbot.lang]} {guild.name}({guild.id}).")
    log.separate(creating_backup[config_selfbot.lang])


# -- Load logs --

#######################
#  load               #
#    backup      !!!  #
#######################

loading_backup = {
    "fr": "CHARGEMENT DE LA BACKUP",
    "en": "LOADING BACKUP"
}

_for = {
    "fr": "pour",
    "en": "for"
}

load_delete_channel_success = {
    "fr": "Salon supprimé avec succès:",
    "en": "Successfully deleted channel:"
}

load_delete_channel_fail = {
    "fr": "Error lors de la suppression du salon:",
    "en": "Error while trying to delete channel:"
}

load_delete_role_success = {
    "fr": "Rôle supprimé avec succès:",
    "en": "Successfully deleted role:"
}

load_delete_role_fail = {
    "fr": "Error lors de la suppression du rôle:",
    "en": "Error while trying to delete role:"
}

load_delete_category_success = {
    "fr": "Catégorie supprimée avec succès",
    "en": "Successfully deleted category"
}

load_delete_category_fail = {
    "fr": "Erreur lors de la suppression de la catégorie",
    "en": "Error while trying to delete category"
}

load_create_role_success = {
    "fr": "Role créé avec succès:",
    "en": "Successfully created role:"
}

load_role_position_success = {
    "fr": "Position du rôle ajusté avec succès:",
    "en": "Successfully adjusted position for role:"
}

load_create_category_success = {
    "fr": "Catégorie créée avec succès:",
    "en": "Successfully created category:"
}

load_create_channel_success = {
    "fr": "Salon créé avec succès:",
    "en": "Successfully created channel:"
}

load_everyone_permissions = {
    "fr": "Permissions de @everyone configuré avec succès en:",
    "en": "Successfully set @everyone permissions to:"
}

load_backup_success = {
    "fr": "Backup chargée avec succès:",
    "en": "Successfully loaded backup:"
}

async def load_guild(guild: discord.Guild,
                     channels,
                     backup,
                     minimal_cooldown,
                     maximum_cooldown):
    """|coro|

    Load the given guild into the chosen guild.

    Parameters:
    -----------
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

    log.separate_text(loading_backup[config_selfbot.lang])
    # Delete old channels
    for channel in channels:
        try:
            await channel.delete()
            log.success(f"{load_delete_channel_success[config_selfbot.lang]} {channel.name}({channel.id}) {_for[config_selfbot.lang]} {guild.name}({guild.id}).")
            await asyncio.sleep(random_cooldown(0.8, 10.3))  # Wait to avoid rate limit
        except Exception as e:
            log.fail(f"{load_delete_channel_fail[config_selfbot.lang]} {channel.name}({channel.id}): {e}")

    # Delete old roles (not @everyone, not bot roles)
    for role in guild.roles:
        if role.name != "@everyone" and not role.is_integration():
            try:
                await role.delete()
                log.success(f"{load_delete_role_success[config_selfbot.lang]} {role.name}({role.id}) {_for[config_selfbot.lang]} {guild.name}({guild.id}).")
                await asyncio.sleep(random_cooldown(0.7, 7.6))  # Wait to avoid rate limit
            except Exception as e:
                log.fail(f"{load_delete_role_fail[config_selfbot.lang]} {role.name}: {e}")

    # Delete old categories
    for category in guild.categories:
        try:
            await category.delete()
            log.success(f"{load_delete_category_success[config_selfbot.lang]}: {category.name}({category.id}) {_for[config_selfbot.lang]} {guild.name}({guild.id}).")
            await asyncio.sleep(random_cooldown(0.8, 6.2))  # Wait to avoid rate limit
        except Exception as e:
            log.fail(f"{load_delete_category_fail[config_selfbot.lang]}: {role.name}: {e}")

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
        log.success(f"{load_create_role_success[config_selfbot.lang]} {role_info['name']}({role_info['id']}) {_for[config_selfbot.lang]} {guild.name}({guild.id}).")
        await asyncio.sleep(random_cooldown(minimal_cooldown, maximum_cooldown))  # Wait to avoid rate limit

    # Adjust role positions
    for role_info in backup["roles"]:
        role = role_map.get(role_info["id"])
        if role:
            await role.edit(position=role_info["position"])
            log.success(f"{load_role_position_success[config_selfbot.lang]} {role_info['name']}({role_info['id']}) {_for[config_selfbot.lang]} {guild.name}({guild.id}).")
            await asyncio.sleep(random_cooldown(minimal_cooldown, maximum_cooldown))  # Wait to avoid rate limit

    # Add backup's categories
    category_map = {}
    for category_info in backup["categories"]:
        new_category = await guild.create_category(
            name=category_info["name"],
            position=category_info["position"]
        )
        category_map[category_info["id"]] = new_category.id
        log.success(f"{load_create_category_success[config_selfbot.lang]} {category_info['name']}({category_info['id']}) {_for[config_selfbot.lang]} {guild.name}({guild.id}).")
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
        channel_type = discord.ChannelType.text if channel_info["type"] == "text" else discord.ChannelType.voice
        if channel_type == discord.ChannelType.text:
            await guild.create_text_channel(
                name=channel_info["name"],
                position=channel_info["position"],
                overwrites=overwrites,
                category=category
            )
        else:
            await guild.create_voice_channel(
                name=channel_info["name"],
                position=channel_info["position"],
                overwrites=overwrites,
                category=category
            )
        log.success(f"{load_create_channel_success[config_selfbot.lang]} {channel_info['name']}({channel_info['id']}) for {guild.name}({guild.id}).")
        await asyncio.sleep(random_cooldown(minimal_cooldown, maximum_cooldown))  # Wait to avoid rate limit

    # Set backup's @everyone permissions
    await guild.default_role.edit(permissions=discord.Permissions(backup["default_role"]["permissions"]))
    log.success(f"{load_everyone_permissions[config_selfbot.lang]} {backup['default_role']['permissions']} for {guild.name}({guild.id}).")

    log.success(f"{load_backup_success[config_selfbot.lang]} {backup['name']}({backup['id']}) to {guild.name}({guild.id}).")
    log.separate(loading_backup[config_selfbot.lang])