# PLAYROOM

H4S2O8 的游戏门户，访问 https://h4s2o8.github.io/demos/ 。

仅收录用户确认的四款游戏：`platformer-game`、`platformer-3d`、`ouyang-qing`、`seven-sins-playtest`。
纯静态 HTML/CSS/JavaScript，无构建步骤、第三方字体或运行时依赖。游戏入口在 HTML 中直接可用，关闭 JavaScript 后仍可浏览和进入游戏。

本地预览：在仓库根目录执行 `python3 -m http.server 18765 --bind 127.0.0.1`，打开 http://127.0.0.1:18765/demos/ 。

修改 `index.html` 中的卡片即可调整名称、介绍和链接；随机推荐从卡片读取内容。图片位于 `assets/`：平台游戏使用实际网页截图，视觉小说使用该游戏仓库的 `app/game/background/cover_b.png` 封面转换版，七罪暗队使用线上版标题页的网页截图。

发布沿用此仓库现有的 GitHub Pages `master` 分支根目录配置，仅新增 `/demos/`，不改其他游戏或域名配置。
