"""Browser smoke test for the dependency-free static showcase."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    handler = partial(SimpleHTTPRequestHandler, directory=ROOT)
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    url = f"http://127.0.0.1:{server.server_port}/showcase/"

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page(viewport={"width": 1440, "height": 1000})
            output = ROOT / "test-results"
            output.mkdir(exist_ok=True)
            errors: list[str] = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(url)
            assert page.get_by_role("heading", name="把真实经历， 慢慢变成作品。").is_visible()

            buttons = page.locator("[data-demo-id]")
            assert buttons.count() == 3
            expected = (
                "从一条真实学习记录创建作品",
                "把初稿推进到可执行的制作清单",
                "让发布数据回到下一轮选题",
            )
            for index, title in enumerate(expected):
                buttons.nth(index).click()
                assert page.locator("[data-demo-title]").inner_text() == title
                assert buttons.nth(index).get_attribute("aria-pressed") == "true"

            page.screenshot(path=str(output / "showcase-desktop.png"), full_page=True)

            page.reload()
            page.keyboard.press("Tab")
            assert page.locator(":focus").count() == 1
            for width in (1440, 390):
                page.set_viewport_size({"width": width, "height": 900})
                assert page.evaluate(
                    "document.documentElement.scrollWidth <= window.innerWidth"
                )
            page.screenshot(path=str(output / "showcase-mobile.png"), full_page=True)
            assert not errors, errors
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)

    print("Showcase browser PASS: 3 flows, keyboard focus, 1440/390 layout, no JS errors.")


if __name__ == "__main__":
    main()

