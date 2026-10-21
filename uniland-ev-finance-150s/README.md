# UNILAND · EV Capital Cycle · Landscape revision

新版：**1920×1080、16:9、30fps、149.53秒**。英文男声、同步英文字幕、122BPM原创配乐。原104秒竖屏版保留。

- 主成片：`renders/uniland-ev-finance-landscape-150s.mp4`
- 无配乐版：`renders/uniland-ev-finance-landscape-150s-voice-only.mp4`
- 独立HTML预览：下载并打开 `index.html`，点击Play；音频、字体、GSAP均已内嵌，可暂停、拖动、关闭BGM。
- 关键画面：`previews/landscape/`；`chart-preview.html`和previews根目录是早期竖屏图表动效研究，非最终横屏成片。

## 本次修改

三张参考图全部重绘为真实HTML/CSS/GSAP图表，未将图表图片贴入画面。保留横向布局、分类顺序、全部数值、单位、约数/下限和口径注释。柱条按4拍顺序增长，数字随之计数并贴着条尾移动；刻度按精确比例对齐。融资额单位为RMBbillion（十亿元）：35对应350亿元。

12个章节含PPT式页面翻转、横推和淡入转场。深蓝面板随内容滑入，顶部/侧边色块在章节切换时移动或改变长度，落定后保留阅读时间。炭黑背景、蓝色图表、无模糊和震屏。

放慢并重新生成口播，加入三张图的必要讲解，删减重复长句；不是机械拉长旧音频。大多数句段接近自然语速。字幕在实测句子时间窗内分组估算，未做逐词强制对齐。

汽车上传图在消息预览中几乎全黑，缺可读取原文件；已向用户说明沿用已有通用SVG线稿。**不是对上传车型的准确还原**。两处出现在行业爆发、价格与利润压力段落，没有车辆照片或3D模型。

## 数据口径

chart-data.json逐项转录用户参考图。融资额不等于亏损；负债/资产为账面比较，回收价值无保证；2025交付是选定品牌，不是全行业排名，小米缺明确数值故未补造。保留~和>。不存在折线时间序列输入，因此未虚构折线图。

来源由用户提供，网页曾被代理403阻止，未独立核实原文。原“16亿元累计利润”和“多数企业同时盈利”结论未使用。完整数据与注释见chart-data.json，原背景来源见../uniland-ev-finance-105s/scripts/content.py。

## 编辑 / HyperFrames

scripts/content.py为口播与拍点，scripts/build.py为横屏布局、动效和播放器；storyboard.json为实际章节时间。scripts/audio.py使用本地Kokoro am_michael及模型缓存生成口播和确定性122BPM打击乐底轨。

```sh
python scripts/prepare-hyperframes.py
npx hyperframes@0.8.181 preview work/hyperframes-ready
```

转换只展开内嵌音频/GSAP并移除独立播放器，保持相同注册时间线。HyperFrames CLI不接受内嵌音频，因此不能直接用离线版HTML渲染。

## 检查

已做浏览器关键帧、全部字幕分组边界、正反拖动确定性检查及HyperFrames lint/validate/inspect。单文件结构建议保留，以遵守自包含源码要求。数据精度、转场和视觉由独立审查复核，报告见review/。MP4最终元数据、解码与音轨对齐结果见review/MP4-CHECK.json；不以数值检查代替主观音色试听或原文事实核验。
