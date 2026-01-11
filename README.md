# Sprite-BMP Tools

A pure bash/Python toolkit for bidirectional conversion between character-based sprites and BMP images. Generate images from code, convert photos to ASCII art, create pixel art—all with a simple palette-based workflow.

## Philosophy

Images are just data. This toolkit treats them that way:

- **Sprites are text files**: Edit them like code 
- **BMPs are generated programmatically**: No image editors needed
- **Palettes define your colors**: One source of truth for your color scheme
- **Native tools**: Bash for BMP generation, Python for jpeg to sprite-file conversion

Perfect for pixel art, procedural generation, game assets, ASCII art, and educational purposes.

## What's Included

### Core Tools

1. **`sprite_to_bmp`** - Convert text sprites to BMP images (bash)
2. **`img-to-sprite.py`** - Convert any image to character sprites (Python)
3. **`gradient`** - Generate gradient images programmatically (bash)
4. **`simple_bmp`** - Minimal BMP example for learning (bash)
5. **`progress-bar`** - Standalone progress visualization demo (bash)

### Libraries

- **`lib/bmp`** - Pure bash BMP file format implementation
- **`lib/progress-bar-mod`** - Terminal progress visualization (production)
- **`lib/progress-bar`** - Progress bar reference implementation (educational)

## Directory Structure

```
sprite-bmp-tools/
├── src/                    # Main source files
│   ├── gradient           # Gradient generator
│   ├── img-to-sprite.py   # Image → sprite converter
│   ├── simple_bmp         # Minimal BMP example
│   ├── sprite_to_bmp      # Sprite → BMP converter
│   ├── progress-bar       # Progress bar demo
│   ├── output             # Placeholder for binary output
│   └── lib/               # Shared libraries
│       ├── bmp            # BMP format library
│       ├── progress-bar-mod  # Progress library (production)
│       └── progress-bar   # Progress library (reference)
├── palette/               # Color palette definitions
│   ├── palette.txt        # Standard palette
│   ├── palette-subtle.txt # Muted colors
│   └── palette-deep.txt   # Rich, deep colors
├── sprite/                # Example sprite files
│   ├── smiley.txt
│   ├── something_cooked_by_chatgpt.txt
│   └── something_cooked_by_claude.txt
├── image/                 # Source images for conversion
│   └── College_Of_Engineering_Logo.jpeg
├── pics/                  # Generated BMP outputs
│   ├── grad1.bmp
│   ├── gradient2.bmp
│   ├── smiley-1.bmp
│   ├── smiley-2.bmp
│   └── smiley-3.bmp
└── README.md
```

## Installation

```bash
# Clone the repository
git clone https://github.com/DeathBlade-01/Image-Sprite-BMP-Tools.git
cd sprite-bmp-tools

# Make scripts executable
chmod +x src/gradient src/simple_bmp src/sprite_to_bmp src/progress-bar

# For Python tools (requires PIL/Pillow)
pip install Pillow
```

## Quick Start

### Try the Examples First

```bash
# 1. Generate a simple 2x2 test image
cd src
./simple_bmp > ../pics/test.bmp

# 2. Create a gradient
./gradient -w 400 -h 400 -o ../pics/my-gradient.bmp

# 3. Convert an existing sprite to BMP
./sprite_to_bmp -p ../palette/palette.txt -o ../pics/smiley-output.bmp < ../sprite/smiley.txt

# 4. Convert an image to sprite
cd ..
python3 src/img-to-sprite.py image/College_Of_Engineering_Logo.jpeg palette/palette.txt logo-output.txt -w 80 --preserve-aspect

# 5. Convert the sprite back to BMP
cd src
./sprite_to_bmp -p ../palette/palette.txt -o ../pics/logo-reconstructed.bmp < ../logo-output.txt
```

### See Progress Bar in Action

```bash
cd src
./progress-bar  # Watch the demo
```

## The Palette System

All sprite-to-BMP conversions use a simple palette format that maps characters to colors.

### Included Palettes

**`palette/palette.txt`** - Standard palette with basic colors:
```
0 #000000
1 #FFFFFF
2 #FF0000
3 #00FF00
4 #0000FF
5 #FFFF00
6 #FF00FF
7 #00FFFF
8 #C0C0C0
9 #808080
```

**`palette/palette-subtle.txt`** - Muted, pastel colors

**`palette/palette-deep.txt`** - Rich, saturated colors

### Creating Your Own Palette

```bash
cat > palette/my-palette.txt << 'EOF'
. #000000
* #FFFFFF
@ #FF6B6B
# #4ECDC4
$ #45B7D1
EOF
```

Format: `<single-character> <hex-color>`

**Rules:**
- One character per line
- Character can be anything except whitespace or quotes
- Hex colors with or without `#` prefix
- Use any number of colors

### Why Character-Based?

1. **Human-readable**: Draw sprites in any text editor
2. **Version control friendly**: Git diffs show actual changes
3. **Compact**: One character per pixel
4. **Flexible**: Use any character you want (numbers, letters, symbols)

## Complete Workflow Examples

### Example 1: Photo to Pixel Art

```bash
# 1. Convert the college logo to a sprite (80 chars wide)
python3 src/img-to-sprite.py \
    image/College_Of_Engineering_Logo.jpeg \
    palette/palette.txt \
    logo-sprite.txt \
    -w 80 --preserve-aspect

# 2. Review the sprite
cat logo-sprite.txt

# 3. Edit the sprite if desired (optional)
nano logo-sprite.txt

# 4. Generate final BMP
cd src
./sprite_to_bmp -p ../palette/palette.txt -o ../pics/logo-final.bmp < ../logo-sprite.txt
```

### Example 2: Create Sprite Art from Scratch

```bash
# Create a simple heart sprite
cat > sprite/heart.txt << 'EOF'
.11.11.
1221221
1222221
.12221.
..121..
...1...
EOF

# Create a palette for it
cat > palette/heart-palette.txt << 'EOF'
. #000000
1 #FF69B4
2 #FF1493
EOF

# Generate the BMP
cd src
./sprite_to_bmp -p ../palette/heart-palette.txt -o ../pics/heart.bmp < ../sprite/heart.txt
```

### Example 3: Compare AI-Generated Sprites

```bash
# The sprite/ directory includes AI-generated examples!

# Convert ChatGPT's creation
cd src
./sprite_to_bmp -p ../palette/palette.txt -o ../pics/chatgpt-art.bmp \
    < ../sprite/something_cooked_by_chatgpt.txt

# Convert Claude's creation
./sprite_to_bmp -p ../palette/palette.txt -o ../pics/claude-art.bmp \
    < ../sprite/something_cooked_by_claude.txt
```

### Example 4: Gradient Variations

```bash
cd src

# Small gradient for thumbnails
./gradient -w 100 -h 100 -o ../pics/gradient-thumb.bmp

# Wide banner
./gradient -w 800 -h 200 -o ../pics/gradient-banner.bmp

# HD wallpaper
./gradient -w 1920 -h 1080 -o ../pics/gradient-hd.bmp
```

## Tool Reference

### `sprite_to_bmp`

Converts character sprites to BMP images using a color palette.

**Usage:**
```bash
./sprite_to_bmp [OPTIONS] < sprite.txt

Options:
  -p <file>    Palette file (required)
  -o <file>    Output filename (default: img.bmp)
```

**Input:** Reads sprite from stdin (one line per row of pixels)

**Output:** 24-bit BMP image file

**Examples:**
```bash
# From file
./sprite_to_bmp -p ../palette/palette.txt -o output.bmp < ../sprite/smiley.txt

# From pipe
cat ../sprite/smiley.txt | ./sprite_to_bmp -p ../palette/palette.txt -o art.bmp

# Using different palettes
./sprite_to_bmp -p ../palette/palette-subtle.txt -o subtle.bmp < ../sprite/smiley.txt
./sprite_to_bmp -p ../palette/palette-deep.txt -o deep.bmp < ../sprite/smiley.txt
```

**How it works:**
1. Loads palette mapping characters to RGB values
2. Reads sprite line-by-line from stdin
3. Maps each character to its RGB color
4. Writes BMP file bottom-to-top (BMP format requirement)
5. Shows progress bar during generation

**Technical details:**
- Outputs binary data to stdout (redirect to file)
- Progress bar goes to stderr (won't corrupt output)
- Handles arbitrary sprite dimensions
- Automatically calculates BMP padding for 4-byte alignment

### `img-to-sprite.py`

Converts images (JPEG, PNG, etc.) to character sprites using palette matching.

**Usage:**
```bash
python3 img-to-sprite.py <image> <palette> <output> [OPTIONS]

Arguments:
  image        Input image file (JPEG, PNG, GIF, BMP, etc.)
  palette      Palette file mapping characters to colors
  output       Output sprite text file

Options:
  -w, --width <n>         Resize to width (in characters)
  -y, --height <n>        Resize to height (in characters)
  --preserve-aspect       Maintain aspect ratio when resizing
```

**Examples:**
```bash
# Convert at original size
python3 src/img-to-sprite.py image/College_Of_Engineering_Logo.jpeg palette/palette.txt logo.txt

# Resize to 64 characters wide, preserve aspect ratio
python3 src/img-to-sprite.py image/College_Of_Engineering_Logo.jpeg palette/palette.txt logo-small.txt -w 64 --preserve-aspect

# Force specific dimensions
python3 src/img-to-sprite.py image/College_Of_Engineering_Logo.jpeg palette/palette.txt logo-square.txt -w 100 -y 100

# Just specify height
python3 src/img-to-sprite.py image/College_Of_Engineering_Logo.jpeg palette/palette.txt logo-tall.txt -y 120 --preserve-aspect
```

**How it works:**
1. Loads palette mapping RGB colors to characters
2. Opens and converts image to RGB
3. Resizes if dimensions specified
4. For each pixel, finds closest palette color using Euclidean distance
5. Maps to corresponding character
6. Writes sprite to text file

**Color matching algorithm:**
- Uses Euclidean distance in RGB color space
- Formula: `sqrt((r1-r2)² + (g1-g2)² + (b1-b2)²)`
- Automatically picks best match from your palette

### `gradient`

Generates gradient images programmatically (great for testing).

**Usage:**
```bash
./gradient [OPTIONS]

Options:
  -w <n>    Width in pixels (default: 400)
  -h <n>    Height in pixels (default: 400)
  -o <f>    Output filename (default: img.bmp)
```

**Examples:**
```bash
cd src

# Default 400x400
./gradient -o ../pics/grad.bmp

# Custom size
./gradient -w 800 -h 600 -o ../pics/wide-grad.bmp

# Square variants
./gradient -w 256 -h 256 -o ../pics/small.bmp
./gradient -w 1024 -h 1024 -o ../pics/large.bmp
```

**Gradient formula:**
- Red channel: `x * 255 / width`
- Green channel: `y * 255 / height`
- Blue channel: 0
- Creates smooth red-green gradient

### `simple_bmp`

Minimal 2x2 BMP generator for learning the format.

**Usage:**
```bash
./simple_bmp > output.bmp
```

**What it generates:**
- 2x2 pixel image
- Bottom row: Black, White
- Top row: Red, Green

**Purpose:** Educational reference for understanding BMP structure

**Example:**
```bash
cd src
./simple_bmp > ../pics/tiny.bmp
file ../pics/tiny.bmp  # Shows: PC bitmap, Windows 3.x format, 2 x 2 x 24
```

### `progress-bar`

Standalone demonstration of the progress bar library.

**Usage:**
```bash
./progress-bar
```

**What it does:**
- Counts from 0 to 500
- Shows live progress bar at terminal bottom
- Demonstrates terminal manipulation techniques

**Purpose:** Educational demo and testing

## Library Reference

### `lib/bmp`

Pure bash implementation of BMP file format writing.

**Functions:**

**`bmp-header <width> <height>`**
- Generates BMP file header and info header
- Sets `$REPLY` to padding bytes needed per row
- Outputs binary header data to stdout

**`bmp-rgb <r> <g> <b>`**
- Outputs a single pixel in BMP format (BGR order)
- Parameters: red, green, blue (0-255)

**`bmp-pad <padding>`**
- Outputs padding null bytes
- BMP rows must align to 4-byte boundaries

**Helper functions:**

**`u32le <value>`** - Output 32-bit little-endian integer
**`u16le <value>`** - Output 16-bit little-endian integer

**Example usage:**
```bash
#!/usr/bin/bash
. ./lib/bmp

width=100
height=100

bmp-header "$width" "$height"
padding=$REPLY

for ((y=0; y<height; y++)); do
    for ((x=0; x<width; x++)); do
        bmp-rgb 255 0 0  # Red pixel
    done
    bmp-pad "$padding"
done
```

**Technical notes:**
- Generates 24-bit uncompressed BMPs
- Windows 3.x format (BITMAPINFOHEADER)
- Bottom-to-top scanline order
- BGR pixel order (BMP standard)

### `lib/progress-bar-mod`

Production-ready progress bar library (see full documentation in `progress-bar-only/README.md`).

**Quick reference:**

```bash
. ./lib/progress-bar-mod

init_term          # Initialize terminal
progress-bar 50 100  # Show progress (50%)
deinit_term        # Restore terminal
```

**Key features:**
- Direct `/dev/tty` communication
- No dependency on `$LINES`/`$COLUMNS`
- Graceful degradation when piped
- Progress to stderr, program output to stdout

### `lib/progress-bar`

Reference implementation for educational purposes.

**Differences from `progress-bar-mod`:**
- Uses `$LINES`/`$COLUMNS` variables
- Simpler implementation
- Includes demo `main()` function
- Best for learning concepts

## Technical Deep Dive

### How BMP Generation Works

The `lib/bmp` library implements the BMP format from scratch in pure bash:

**1. File Structure:**
```
[BMP Header - 14 bytes]
[DIB Header - 40 bytes]
[Pixel Data - bottom to top, left to right]
```

**2. Coordinate System:**
- BMP stores pixels bottom-to-top
- `sprite_to_bmp` reverses sprite line order during conversion
- Formula: `line = sprite[height - y - 1]`

**3. Padding:**
- Each row must be multiple of 4 bytes
- 24-bit color = 3 bytes per pixel
- Row size = `width * 3`
- Padding = `(4 - (row_size % 4)) % 4`

**4. Binary Output:**
- Uses `printf '%b'` with `\xNN` escape sequences
- Outputs directly to stdout
- No temporary files needed

### Why Bash for BMP Generation?

1. **No dependencies**: Works on any Unix system
2. **Bit manipulation**: Bash can handle it with `((  ))` arithmetic
3. **Binary output**: `printf` supports `\xNN` sequences
4. **Pipes**: Natural workflow for stdin → stdout
5. **Learning**: Understanding binary formats builds skills

### Color Matching Algorithm

The `img-to-sprite.py` uses Euclidean distance in RGB space:

```python
def color_distance(c1, c2):
    return sqrt((r1-r2)² + (g1-g2)² + (b1-b2)²)
```

**Why Euclidean:**
- Simple and fast
- Perceptually reasonable for small palettes
- No external dependencies

**Alternative algorithms** (not implemented):
- CIE76 (perceptually uniform)
- CIE94/CIE2000 (better perceptual accuracy)
- Would require color space conversion

### Progress Bar Architecture

**The scroll region trick:**

```bash
# Reserve bottom line
printf '\e[%d;%dr' 0 "$((LINES-1))"

# Jump to bottom, draw progress, jump back
printf '\e[%d;%dH' "$LINES" 0  # Move to bottom
printf '[||||||||...]'          # Draw progress
printf '\e8'                     # Restore cursor

# Output scrolls in restricted region above
```

**Why `/dev/tty`:**
- Program output goes to stdout (can be redirected)
- Progress UI goes to stderr → `/dev/tty` (always terminal)
- Clean separation of data and UI

## Use Cases

### Pixel Art Creation

```bash
# Draw sprite in text editor
# Convert to image
# Iterate until perfect
```

### Procedural Generation

```bash
# Generate sprites with scripts
# Batch convert to images
# Use in games/projects
```

### Image Analysis

```bash
# Convert image to sprite
# Analyze character distribution
# Understand image composition
```

### ASCII Art

```bash
# Photo → sprite with custom palette
# Use ASCII characters as palette
# Print to terminal or save
```

### Educational

```bash
# Learn BMP format with simple_bmp
# Understand binary file formats
# Practice bash programming
```

### Logo Conversion

```bash
# Convert company logos to text
# Version control in git
# Generate different sizes easily
```

## Troubleshooting

### BMP Output is Corrupted

**Problem:** Image won't open or displays incorrectly

**Causes:**
1. Progress bar output mixed with image data
2. Incorrect palette character mapping
3. Sprite has inconsistent line widths

**Solutions:**
```bash
# Ensure output redirection
./sprite_to_bmp -p palette.txt -o output.bmp < sprite.txt  # ✓ Correct
./sprite_to_bmp -p palette.txt < sprite.txt                 # ✗ Wrong (prints to terminal)

# Check sprite line lengths
awk '{print length}' sprite.txt | sort -u  # Should show one number

# Verify palette has all characters
grep -o . sprite.txt | sort -u  # List all characters used
```

### Image-to-Sprite Colors Look Wrong

**Problem:** Colors don't match original image

**Cause:** Limited palette doesn't cover image's color range

**Solutions:**
```bash
# Use more colors in palette
# Try different palette styles
python3 src/img-to-sprite.py image.jpg palette/palette-deep.txt out.txt -w 64

# Reduce image size for better color matching
python3 src/img-to-sprite.py image.jpg palette/palette.txt out.txt -w 32
```

### Progress Bar Doesn't Show

**Problem:** No progress bar appears

**Causes:**
1. Output is redirected (by design)
2. Not a TTY environment
3. Forgot to call `init_term`

**Check:**
```bash
# Is it a TTY?
tty  # Should show /dev/pts/X or /dev/ttyX

# Is stderr redirected?
./sprite_to_bmp 2>/dev/null  # This would hide progress bar
```

### Permission Denied

**Problem:** `bash: ./gradient: Permission denied`

**Solution:**
```bash
chmod +x src/gradient src/simple_bmp src/sprite_to_bmp src/progress-bar
```

### Python Module Not Found

**Problem:** `ModuleNotFoundError: No module named 'PIL'`

**Solution:**
```bash
pip install Pillow
# or
pip3 install Pillow
```

## Performance Notes

### BMP Generation Speed

- **Simple patterns**: 1000x1000 in ~2 seconds
- **Complex sprites**: Limited by bash string operations
- **Bottleneck**: Character-by-character palette lookup

**Optimization tips:**
```bash
# For large sprites, reduce progress-bar calls
if ((y % 10 == 0)); then
    progress-bar "$y" "$height"
done
```

### Image-to-Sprite Speed

- **Modern Python**: Fast enough for most images
- **Large images**: Consider resizing first
- **Typical**: 1024x768 → 100x75 sprite in <1 second

### File Sizes

**BMP files:**
- Uncompressed: Width × Height × 3 bytes + 54 byte header
- 400×400: ~480KB
- 1920×1080: ~6MB

**Sprite files:**
- Text: Width × Height bytes + newlines
- 400×400: ~400KB
- Much smaller when compressed (gzip)

## Examples Gallery

The repository includes several example outputs in `pics/`:

- **`smiley-1.bmp`** - Basic smiley face sprite
- **`smiley-2.bmp`** - Smiley with different palette
- **`smiley-3.bmp`** - Another smiley variation
- **`grad1.bmp`** - Gradient example
- **`gradient2.bmp`** - Another gradient

And example sprites in `sprite/`:

- **`smiley.txt`** - Hand-crafted smiley
- **`something_cooked_by_chatgpt.txt`** - AI-generated art
- **`something_cooked_by_claude.txt`** - AI-generated art

Try converting these with different palettes to see the effects!

## Contributing

Contributions welcome! This toolkit is designed to be:

- **Educational**: Clear, readable code
- **Minimal**: No unnecessary dependencies
- **Portable**: Works on any Unix system
- **Documented**: Explain the why, not just the what

**Ideas for contributions:**
- More palette examples
- Additional sprite examples
- Performance optimizations
- Color matching algorithms
- Documentation improvements
- Additional output formats

## Credits

Created with a focus on understanding file formats, binary data manipulation, and the power of text-based workflows.

**Technologies:**
- Pure bash (no bashisms where avoidable)
- Python 3 with Pillow
- ANSI escape sequences
- BMP file format (Windows 3.x)

**Philosophy inspired by:**
- Unix philosophy (do one thing well)
- Plain text workflows
- Literate programming
- Learning by implementing

## License

MIT License

---

**Happy sprite making!** 🎨

Got questions? Found a bug? Want to show off your creations? Open an issue!
