
import argparse
from PIL import Image
import sys


def load_palette(palette_file):
    """
    Load palette from file.
    Format: <char> <hex_color>
    Example:
        0 #000000
        1 #FFD700
        9 #8B4513
    
    Returns dict mapping hex colors to characters.
    """
    palette = {}
    
    try:
        with open(palette_file, 'r') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                
                parts = line.split()
                if len(parts) != 2:
                    print(f"Warning: Invalid line {line_num}: {line}", file=sys.stderr)
                    continue
                
                char, hex_color = parts
                hex_color = hex_color.lstrip('#')
                
                if len(hex_color) != 6:
                    print(f"Warning: Invalid hex color on line {line_num}: {hex_color}", file=sys.stderr)
                    continue
                
                # Convert hex to RGB tuple
                r = int(hex_color[0:2], 16)
                g = int(hex_color[2:4], 16)
                b = int(hex_color[4:6], 16)
                
                palette[(r, g, b)] = char
        
        if not palette:
            print("Error: Palette is empty!", file=sys.stderr)
            sys.exit(1)
        
        return palette
    
    except FileNotFoundError:
        print(f"Error: Palette file '{palette_file}' not found!", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error loading palette: {e}", file=sys.stderr)
        sys.exit(1)


def color_distance(c1, c2):
    """Calculate Euclidean distance between two RGB colors."""
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5


def find_closest_color(rgb, palette):
    """Find the closest color in the palette to the given RGB value."""
    closest_color = min(palette.keys(), key=lambda c: color_distance(rgb, c))
    return palette[closest_color]


def image_to_sprite(image_path, palette, width=None, height=None):
    """
    Convert an image to a character sprite based on the palette.
    
    Args:
        image_path: Path to input image
        palette: Dict mapping RGB tuples to characters
        width: Target width (None = use original)
        height: Target height (None = use original)
    
    Returns:
        List of strings representing the sprite
    """
    try:
        img = Image.open(image_path)
        
        # Convert to RGB if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Resize if dimensions specified
        if width or height:
            orig_width, orig_height = img.size
            
            if width and not height:
                height = int(orig_height * (width / orig_width))
            elif height and not width:
                width = int(orig_width * (height / orig_height))
            
            img = img.resize((width, height), Image.Resampling.LANCZOS)
        
        sprite = []
        w, h = img.size
        
        print(f"[debug] Converting {w}x{h} image...", file=sys.stderr)
        
        for y in range(h):
            row = ""
            for x in range(w):
                pixel = img.getpixel((x, y))
                char = find_closest_color(pixel, palette)
                row += char
            sprite.append(row)
            
            # Show progress every 10 rows or at the end
            if (y + 1) % 10 == 0 or y == h - 1:
                progress = ((y + 1) / h) * 100
                print(f"[debug] Processing row {y + 1}/{h} ({progress:.1f}%)", file=sys.stderr)
        
        return sprite
    
    except FileNotFoundError:
        print(f"Error: Image file '{image_path}' not found!", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error processing image: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Convert images to character sprites using a color palette',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s photo.jpg palette.txt sprite.txt
  %(prog)s photo.jpg palette.txt output.txt -w 64 -y 64
  %(prog)s photo.jpg palette.txt output.txt -w 128 --preserve-aspect
        """
    )
    
    parser.add_argument('image', help='Input image file')
    parser.add_argument('palette', help='Palette file (format: "char #hexcolor")')
    parser.add_argument('output', help='Output sprite file')
    parser.add_argument('-w', '--width', type=int, help='Target width in characters')
    parser.add_argument('-y', '--height', type=int, help='Target height in characters')
    parser.add_argument('--preserve-aspect', action='store_true',
                        help='Preserve aspect ratio when resizing')
    
    args = parser.parse_args()
    
    # Load palette
    palette = load_palette(args.palette)
    print(f"[debug] Loaded palette with {len(palette)} colors", file=sys.stderr)
    
    # Handle preserve aspect ratio
    width = args.width
    height = args.height
    
    if args.preserve_aspect and (width and height):
        print("[debug] Warning: --preserve-aspect ignored when both width and height are specified", 
              file=sys.stderr)
    elif args.preserve_aspect:
        # Set the other dimension to None to preserve aspect ratio
        if not width:
            width = None
        if not height:
            height = None
    
    # Convert image to sprite
    sprite = image_to_sprite(args.image, palette, width, height)
    
    # Output sprite
    try:
        with open(args.output, 'w') as f:
            for line in sprite:
                f.write(line + '\n')
        print(f"[debug] Sprite saved to {args.output}", file=sys.stderr)
        print(f"[debug] Dimensions: {len(sprite[0])}x{len(sprite)}", file=sys.stderr)
    except Exception as e:
        print(f"Error writing output: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
