# a script to read world id in photos taken in VRChat and Open web page to join the worlds
import sys
import webbrowser

# to read xml in the photos
import pyexiv2


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_files = sys.argv[1:]

    for input_file in input_files:
        # read world id from input_file
        world_id: str | None = read_world_id(input_file)

        # open web page to join the world
        if world_id is not None:
            open_world_page(world_id)
        else:
            print(f"Failed to read world id from {input_file}")


def read_world_id(input_file: str) -> str | None:
    # read world id from input_file
    # return world id or None if failed
    xmp = None
    try:
        with pyexiv2.Image(input_file) as image:
            xmp = image.read_xmp()
    except Exception as e:
        print(f"Failed to read XMP metadata from {input_file}: {e}")
        return None

    if xmp is None:
        return None

    world_id = xmp.get("Xmp.vrc.WorldID")
    if world_id is None:
        return None

    return world_id


def open_world_page(world_id: str) -> None:
    # open web page to join the world
    url = f"https://vrchat.com/home/world/{world_id}"
    print(f"Opening {url}")
    webbrowser.open(url)


if __name__ == "__main__":
    main()
