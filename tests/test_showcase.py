from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SHOWCASE = ROOT / "showcase"


class ShowcaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (SHOWCASE / "index.html").read_text(encoding="utf-8")
        cls.js = (SHOWCASE / "app.js").read_text(encoding="utf-8")

    def test_core_content_is_available_without_javascript(self):
        for text in (
            "灵感小记 · 自媒体内容创作工作台",
            "定位",
            "素材",
            "选题",
            "稿件",
            "排期",
            "复盘",
            "8 个助手",
            "5 种内容形式",
            "75 项后端自动化测试",
            "390px",
            "静态流程演示",
        ):
            self.assertIn(text, self.html)

    def test_exactly_three_demo_controls_exist(self):
        buttons = re.findall(r'<button[^>]+data-demo-id="[^"]+"[^>]*>', self.html)
        self.assertEqual(3, len(buttons))
        for button in buttons:
            self.assertIn("aria-pressed", button)

    def test_page_uses_only_local_runtime_assets(self):
        resources = re.findall(r'(?:src|href)="([^"]+)"', self.html)
        external_assets = [
            value
            for value in resources
            if value.startswith(("http://", "https://"))
            and "github.com/kexinyang74-web/media-topic-assistant" not in value
        ]
        self.assertEqual([], external_assets)

    def test_demo_data_represents_three_verified_flows(self):
        for text in (
            "material-to-work",
            "version-production",
            "publish-review",
            "定位快照",
            "Markdown / CSV",
            "观察天数",
            "资料不足",
        ):
            self.assertIn(text, self.js)

    def test_source_link_is_public_repository(self):
        self.assertIn(
            "https://github.com/kexinyang74-web/media-topic-assistant",
            self.html,
        )

    def test_private_runtime_data_is_ignored(self):
        ignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
        for pattern in (".env", "data/", "test-results/", ".worktrees/"):
            self.assertIn(pattern, ignore)

    def test_pages_workflow_uploads_showcase_directory(self):
        workflow = (
            ROOT / ".github" / "workflows" / "deploy-pages.yml"
        ).read_text(encoding="utf-8")
        self.assertIn("branches: [main]", workflow)
        self.assertIn("pages: write", workflow)
        self.assertIn("id-token: write", workflow)
        self.assertIn("path: ./showcase", workflow)

    def test_readme_links_demo_and_explains_static_boundary(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(
            "https://kexinyang74-web.github.io/media-topic-assistant/", readme
        )
        self.assertIn("静态流程演示", readme)
        self.assertIn("不调用 DeepSeek", readme)


if __name__ == "__main__":
    unittest.main()

