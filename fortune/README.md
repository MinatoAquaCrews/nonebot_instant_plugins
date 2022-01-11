<div align="center">

# Tarot

<!-- prettier-ignore-start -->
<!-- markdownlint-disable-next-line MD036 -->
_🙏 今日运势 🙏_
<!-- prettier-ignore-end -->

</div>
</p>

## 安装

1. `git clone`；

2. 将`fortune`文件夹加入你的`bot/plugins`下；`resource`内抽签签底及文案、字体资源放置于`./data/fortune`下；

3. *可选：在`env`内配置`FORTUNE_PATH`：

```python
FORTUNE_PATH="./data/fortune"   # 抽签签底及文案、字体资源储存路径，默认位于./data/fortune
```

4. 占卜一下你的今日运势！🎉

## 功能

1. 随机抽取今日运势，配置四种签底：原神、PCR、VTB、东方；

2. 可设置随机签种或特定签种，也可指定角色签（例如可莉、魔理沙、凯露、阿夸🥰）；

3. 每人一天限抽签一次，0点刷新（贪心的人是不会有好运的哦🤗）；

4. *TODO* 
   - 增加权限功能：仅管理员和超管有权更改抽签设置；
   - 每个群聊的抽签设置单独管理；
   - 抽签后，会生成`./data/fortune/out`文件夹，文件夹下为当天群友抽签生成的图片，或许需要每天更新时自动清理一遍？

## 命令

1. 一般抽签：今日运势、抽签、运势；
2. 指定抽签：指定[xxx]签（具体有哪些查看源码，可以自己加哦）；
3. 配置签种：
   - 设置[原神/PCR/东方/vtb]签：设置抽签的签底；
   - 重置抽签：设置抽签签底为随机；

4. 抽签设置：查看当前抽签的配置；

## 本插件改自：

1. [opqqq-plugin](https://github.com/opq-osc/opqqq-plugin)，除功能函数外，由于要适配nonebot2底层已大改
2. 感谢江樂丝提供东方签底，:point_left:~~女孩子有点害羞诶~~