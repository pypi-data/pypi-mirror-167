from setuptools import setup

setup(
    name='nonebot-plugin-dialectlist',
    version='0.1.2',
    author='MYXS',
    author_email='1964324406@qq.com',
    url='https://github.com/X-Skirt-X/nonebot_plugin_dialectlist',
    description=u'一个通过数据库统计群友消息量并作为排行榜发出',
    packages=['nonebot_plugin_dialectlist'],
    install_requires=[
        'nonebot_plugin_datastore',
        'nonebot_plugin_chatrecorder',
        'nonebot-adapter-onebot',
        'nonebot_plugin_guild_patch',
        'pygal',
        'cairosvg',
        ],
)