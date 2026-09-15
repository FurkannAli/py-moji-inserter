import subprocess

def paste_character(text: str):
    try:
        # Copy char to the wayland clipboard
        subprocess.run(["wl-copy", text], check=True)

        # simulate ctrl+v
        subprocess.run(["dotool"], input=b"key ctrl+v", check=True)
    except FileNotFoundError as e:
        print(f"[Error] Required tool missing: {e}")
    except subprocess.CalledProcessError as e:
        print(f"[Error] Insertation failed: {e}")