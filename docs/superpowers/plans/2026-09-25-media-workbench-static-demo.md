# 自媒体内容创作工作台静态演示实施计划

1. **公开基线与安全测试**
   - 为公开演示补充密钥、数据库、测试产物和工作树的忽略校验。
   - 确认现有仓库公开、主分支和远程地址正确。

2. **测试先行实现静态页**
   - 先增加 `tests/test_showcase.py` 和 `tests/showcase_logic.test.mjs`，覆盖页面文案、三类案例、本地资源、公开仓库链接、静态边界及选择逻辑。
   - 在测试失败后实现 `showcase/index.html`、`showcase/styles.css`、`showcase/app.js`。
   - 用浏览器检查三项切换、控制台、键盘焦点、390px 与 1440px 布局。

3. **部署与文档**
   - 增加 `.github/workflows/deploy-pages.yml`，发布 `showcase/`。
   - README 增加在线演示入口并说明静态边界。
   - 运行 75 项后端测试、静态页测试、Node 逻辑测试和 Python 编译。

4. **推送和线上验收**
   - 将功能分支推送为远程 `main`，等待 Pages 工作流成功。
   - 验证 HTML/CSS/JS 均返回 200，标题、三个案例和源码链接存在。

5. **作品集更新**
   - 将作品集中的 `media-topic-assistant` 链接改为 Pages 演示地址，并将描述改为可核验的技术方案、问题和效果。
   - 构建、推送并等待作品集部署；验证线上标题和演示链接。

