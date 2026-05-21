import requests
import time
from src.config import SERVER_HOST, SERVER_PORT
from rich.console import console
import typer

API_URL = f"http://{SERVER_HOST}:{SERVER_PORT}/chat"
SERVER_URL = f"http://{SERVER_HOST}:{SERVER_PORT}/"


app=typer.Typer(
    no_args_is_help=True
    name:bot
)

@app.command()
def onboard():
    from src.config import get_config_path, load_config, save_config
    from src.config import Config

    config_path = get_config_path()

    if config_path.exists():
        console.print(f"[yellow]Config already exists at {config_path}[/yellow]")
        console.print("  [bold]y[/bold] = overwrite with defaults (existing values will be lost)")
        console.print("  [bold]N[/bold] = refresh config, keeping existing values and adding new fields")
        if typer.confirm("Overwrite?"):
            config = Config()
            save_config(config)
            console.print(f"[green]✓[/green] Config reset to defaults at {config_path}")
        else:
            config = load_config()
            save_config(config)
            console.print(f"[green]✓[/green] Config refreshed at {config_path} (existing values preserved)")
    else:
        save_config(Config())
        console.print(f"[green]✓[/green] Created config at {config_path}")

    console.print("[dim]Config template now uses `maxTokens` + `contextWindowTokens`; `memoryWindow` is no longer a runtime setting.[/dim]")


    # Create workspace
    workspace = get_workspace_path()

    if not workspace.exists():
        workspace.mkdir(parents=True, exist_ok=True)
        console.print(f"[green]✓[/green] Created workspace at {workspace}")


    console.print("\nNext steps:")
    console.print("  1. Add your API key to [cyan]~/.src/config.json[/cyan]")
    console.print("     Get one at: https://openrouter.ai/keys")
    console.print("  2. Chat: [cyan]src agent -m \"Hello!\"[/cyan]")
    console.print("\n[dim]Want Telegram/WhatsApp? See: https://github.com/HKUDS/src#-chat-apps[/dim]")


def check_server(max_retries: int = 3, retry_delay: int = 2) -> bool:
    """检查服务器是否已启动"""
    for i in range(max_retries):
        try:
            requests.get(SERVER_URL, timeout=2)
            return True
        except requests.exceptions.ConnectionError:
            if i < max_retries - 1:
                print(f"正在等待服务器启动... ({i + 1}/{max_retries})")
                time.sleep(retry_delay)
    return False


def main():
    """命令行客户端主函数"""
    print("正在检查服务器状态...")
    if not check_server():
        print("服务器未启动！请先运行: python run_server.py")
        return

    print("服务器已连接！")
    print("您现在已进入对话，输入 exit 可以退出")
    print("-" * 40)

    while True:
        user_input = input("用户：")
        if user_input.lower() == "exit":
            print("bot：要走了吗(┬┬﹏┬┬)，再见 ༼◕_◕ ༽つ")
            break

        try:
            response = requests.post(
                API_URL, json={"user_input": user_input}, timeout=30
            )
            reply = response.json()["reply"]
            print("bot：", reply)
        except requests.exceptions.ConnectionError:
            print("连接失败，服务器可能已关闭")
            break
        except Exception as e:
            raise RuntimeError(f"出错{e}") from e


if __name__ == "__main__":
    main()
