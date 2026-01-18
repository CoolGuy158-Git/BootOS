if __name__ == "__main__":
    print("Booting BootOS...")
    try:
        from core.boot import *
    except ImportError as e:
        print(f"Import error. {e}")
    except Exception as e:
        print(f"Error: {e}")
