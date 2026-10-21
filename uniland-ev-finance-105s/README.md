# UNILAND · China EV Market Brief

按2026-10-21确认的精简英文稿制作。1080×1920 / 30fps / 104.27秒 / 122 BPM。

## 使用

下载ZIP并解压，双击 `index.html`，点击 **Play**。配音、音乐、字体、GSAP均已内嵌；正常播放不需网络，不会自动播放或导出视频。可暂停、拖动进度、重播、静音，或关闭BGM保留英文口播。展开 Sources & production notes 查看来源链接。

另已按用户后续要求导出 **MP4成片：renders/uniland-ev-finance-105s.mp4**，包含相同英文口播、字幕和配乐。HTML仍可独立预览。本环境Chromium的企业策略禁止file://，因此实际测试使用本地HTTP，确认无外部网络请求。HTML按普通浏览器离线使用设计；若你的浏览器限制本地页面，可在本目录运行 `python -m http.server 3035` 并访问 http://localhost:3035 。

## 内容与视觉

- 炭黑纯色、深蓝细线、灰白排版和浅蓝数字。无照片、图片贴图、3D模型、表情或多余图标。
- 所有主要文字按小节重拍淡入和轻微上移；数字平滑计数后保持。年份2014按年份显示，无千位逗号。
- 行业爆发与品牌竞争两段含原创内联SVG汽车轮廓，这是用户确认的例外。
- 122 BPM原创合成打击乐/低音铺底；商务英文合成男声 Kokoro am_michael。
- 按确认稿删除“全行业净利润16亿元”和“多数企业盈利”的笼统表述。保留融资/国资投入、销量/交付、报道样本/全行业的区别。
- 原文网页访问被网络代理403阻止。来源为用户提供，未声称独立核实；数据画面保留Reported提示。没有增加零食支出、法律指控等支线。
- 字幕按已测量句子时长分组估算，未做逐词强制对齐。第二段约195词/分钟，信息较密；其余段落约126–171词/分钟。人声音色及主观听感仍需试听确认。

## 编辑源码

`index.html` 是完整独立成品。末尾的SPEC、CAPTIONS、时间线与播放器逻辑可编辑；CSS在头部，内嵌字体和音频占大部分文件体积。`storyboard.json` 保存确认稿与时间点，`DESIGN.md` 保存设计和例外。

开发生成器位于 scripts/：content.py为口播/来源，build.py为版式与动画，audio.py为本地TTS/原创配乐。重建依赖本地Kokoro模型及Python音频库；现有HTML播放无需这些依赖。字体许可见FONT-LICENSE.txt，GSAP版权声明保留在HTML中。

## HyperFrames兼容方式

单文件预览内嵌音频并包含用户点击控制。HyperFrames CLI 0.8.181的规则禁止base64音频和手动控制托管媒体，因此不要直接对离线版运行render。

如需以后使用HyperFrames Studio/CLI，在本目录执行：

```sh
python scripts/prepare-hyperframes.py
npx hyperframes@0.8.181 preview work/hyperframes-ready
```

转换脚本只把相同音频和GSAP展开为相对路径文件，移除独立播放器，保留同一注册时间线；脚本本身不调用渲染。MP4使用该转换版本经HyperFrames CLI导出。转换版本lint零错误，12个结构建议来自按要求保留单HTML、未拆子合成；validate对比度检查通过，inspect关键时刻零布局问题。完整报告见review/。

## 验证范围

离线依赖检查（本地HTTP）、浏览器执行、十镜截图、正反拖动确定性、手机控制布局、按键播放、BGM开关与音频数值检查。抽查播放时两音轨误差在约一帧内。后续MP4交付的媒体元数据、关键帧及音画对齐检查另外记录在review/MP4-CHECK.json。不宣称逐词字幕对齐、音色主观试听或原网页事实核验已通过。

video-shotcraft的Remotion、Gallery复现、戏剧性结尾和专用工作台默认流程，按本次单HTML、HyperFrames、简约文字和不渲染要求进行适配，未伪称实现那些默认功能。已做独立HTML/画面审查。
