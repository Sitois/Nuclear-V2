import random, string, os, json, asyncio

import discord

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
                "hoist": role.hoist
            })
        log.success(f"Successfully saved role: {role.name}({role.id}) from {guild.name}({guild.id}).")

    # Save @everyone's permissions
    guild_info["default_role"] = {
        "permissions": guild.default_role.permissions.value
    }
    log.success(f"Successfully saved @everyone role from {guild.name}({guild.id}).")

    # Save guild's categories
    for category in guild.categories:
        guild_info["categories"].append({
            "id": category.id,
            "name": category.name,
            "position": category.position
        })
        log.success(f"Successfully saved category: {category.name}({category.id}) from {guild.name}({guild.id}).")

    # Save guild's channels
    for channel in guild.channels:
        channel_info = {
            "id": channel.id,
            "name": channel.name,
            "type": str(channel.type),
            "position": channel.position,
            "category": channel.category_id,
            "permissions": []
        }
        log.success(f"Successfully saved channel: {channel.name}({channel.id}) from {guild.name}({guild.id}).")

        # Save channel's permissions
        for overwrite in channel.overwrites:
            allow, deny = channel.overwrites[overwrite].pair()
            channel_info["permissions"].append({
                "id": overwrite.id,
                "type": "role" if isinstance(overwrite, discord.Role) else "member",
                "allow": allow.value,
                "deny": deny.value
            })
        log.success(f"Successfully saved permissions for {channel.name}({channel.id}) from {guild.name}({guild.id}).")

        guild_info["channels"].append(channel_info)


    # Check if backups folder exists
    if not os.path.exists("backups"):
        log.alert("Unable to find the 'backups' folder!")

    # Save guild's infos in a json file
    with open(f"./backups/{guild.id}.json", "w") as f:
        json.dump(guild_info, f, indent=4)

    log.success(f"Successfully saved guild: {guild.name}({guild.id}).")



async def load_guild(guild: discord.Guild, backup, minimal_cooldown, maximum_cooldown):
    """Load the given guild into the choosen guild."""
    # Delete old channels
    for channel in guild.channels:
        try:
            await channel.delete()
            log.success(f"Successfully deleted channel: {channel.name}({channel.id}) for {guild.name}({guild.id}).")
            await asyncio.sleep(random_cooldown(minimal_cooldown, maximum_cooldown))  # Wait to avoid rate limit
        except Exception as e:
            log.fail(f"Error while trying to delete channel: {channel.name}({channel.id}): {e}")

    # Delete old roles (not @everyone, not bot roles)
    for role in guild.roles:
        if role.name != "@everyone" and not role.is_integration():
            try:
                await role.delete()
                log.success(f"Successfully deleted role: {role.name}({role.id}) for {guild.name}({guild.id}).")
                await asyncio.sleep(random_cooldown(minimal_cooldown, maximum_cooldown))  # Wait to avoid rate limit
            except Exception as e:
                log.fail(f"Error while trying to delete role: {role.name}: {e}")

    # Add backup's roles
    for role_info in backup["roles"]:
        await guild.create_role(
            name=role_info["name"],
            permissions=discord.Permissions(role_info["permissions"]),
            color=discord.Color(role_info["color"]),
            mentionable=role_info["mentionable"],
            hoist=role_info["hoist"]
        )
        log.success(f"Successfully created role: {role_info['name']}({role_info['id']}) for {guild.name}({guild.id}).")
        await asyncio.sleep(random_cooldown(minimal_cooldown, maximum_cooldown))  # Wait to avoid rate limit

    # Add backup's categories
    category_map = {}
    for category_info in backup["categories"]:
        new_category = await guild.create_category(
            name=category_info["name"],
            position=category_info["position"]
        )
        category_map[category_info["id"]] = new_category.id
        log.success(f"Successfully created category: {category_info['name']}({category_info['id']}) for {guild.name}({guild.id}).")
        await asyncio.sleep(random_cooldown(minimal_cooldown, maximum_cooldown))  # Wait to avoid rate limit

    # Add backup's channels
    for channel_info in backup["channels"]:
        overwrites = {}
        for perm in channel_info["permissions"]:
            target = guild.get_role(perm["id"]) if perm["type"] == "role" else guild.get_member(perm["id"])
        if target:
            overwrites[target] = discord.PermissionOverwrite.from_pair(
                discord.Permissions(perm["allow"]),
                discord.Permissions(perm["deny"])
            )

    category = guild.get_channel(category_map[channel_info["category"]]) if channel_info["category"] else None
    channel_type = discord.ChannelType.text if channel_info["type"] == "text" else discord.ChannelType.voice
    await guild.create_text_channel(
        name=channel_info["name"],
        position=channel_info["position"],
        overwrites=overwrites,
        category=category
    ) if channel_type == discord.ChannelType.text else await guild.create_voice_channel(
        name=channel_info["name"],
        position=channel_info["position"],
        overwrites=overwrites,
        category=category
    )
    log.success(f"Successfully created channel: {channel_info['name']}({channel_info['id']}) for {guild.name}({guild.id}).")
    await asyncio.sleep(random_cooldown(minimal_cooldown, maximum_cooldown))  # Wait to avoid rate limit

    # Set backup's @everyone permissions
    log.success(f"Successfully set @everyone permissions to: {backup['default_role']['permissions']} for {guild.name}({guild.id}).")
    await guild.default_role.edit(permissions=discord.Permissions(backup["default_role"]["permissions"]))

    log.success(f"Successfully loaded backup: {backup['name']}({backup['id']}) to {guild.name}({guild.id}).")