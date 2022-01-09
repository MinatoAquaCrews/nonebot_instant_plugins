import re
import random
from nonebot import on_command, logger
from nonebot.typing import T_State
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.event import GroupMessageEvent
from nonebot.adapters.cqhttp.permission import GROUP
from src.utils.self_mute_utils.role_utils import RoleChecker # Change this path

self_mute = on_command(
    '口我',
    # 使用run_preprocessor拦截权限管理, 在default_state初始化所需权限
    state={
        '_matcher_name': 'self_mute',
        '_command_permission': True,
        '_permission_level': 10,
        '_cool_down': 15
    },
    aliases={'口球', '禁言礼包', '禁言套餐'},
    permission=GROUP,
    priority=10,
    block=True)


@self_mute.handle()
async def handle_self_mute(bot: Bot, event: GroupMessageEvent, state: T_State):
    args = str(event.get_plaintext()).strip()
    # 检查是否有倍数参数
    if multiple_text := re.search(r'^(\d+)倍$', args):
        multiple = int(multiple_text.groups()[0])
    else:
        multiple = 1

    # 检查bot和用户身份
    if not (await RoleChecker(group_id=event.group_id, user_id=event.self_id, bot=bot).is_group_admin()):
        await self_mute.finish('Bot非群管理员, 无法执行禁言操作QAQ☹')
    if await RoleChecker(group_id=event.group_id, user_id=event.user_id, bot=bot).is_group_admin():
        await self_mute.finish('管理员口不了管理员哦🤔', at_sender=True)

    # 随机禁言时间
    random_time = 2 * int(random.gauss(128 * multiple, 640 * multiple // 10))
    act_time = 60 if random_time < 60 else (random_time if random_time < 2591940 else 2591940)
    msg = f'获得了一份{act_time // 60}分{act_time % 60}秒的口球套餐🤗'

    await bot.set_group_ban(group_id=event.group_id, user_id=event.user_id, duration=act_time)
    logger.info(f'Group: {event.group_id}, User: {event.user_id} 抽取了 {act_time} 秒的口球套餐')
    await self_mute.finish(msg, at_sender=True)
