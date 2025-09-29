# Matplotlib4TD

A TouchDesigner project that enables real-time plotting of CHOP (Channel Operator) data using matplotlib. This project creates dynamic plots from TouchDesigner's audio and data channels and exports them as PNG images.

## 📋 Overview

This project allows TouchDesigner users to:
- Plot live CHOP data in real-time
- Export plots as PNG images
- Integrate matplotlib visualizations directly into TouchDesigner workflows
- Handle multiple channels with automatic legend generation

![TouchDesigner Interface](images/touchdesigner-interface.png)
*The TouchDesigner interface showing the matplotlib plotting system in action - CHOP data from the 'source' node is processed through the plotting system and displayed in the 'plot_in' Movie File In TOP*

## 🔧 Prerequisites

- **TouchDesigner 2025** (build 30770 or compatible)
- **macOS** (project configured for macOS paths)
- **Python 3.11** (bundled with TouchDesigner)

## ⚙️ Installation

### 1. Check TouchDesigner's Python Version

First, verify which Python version your TouchDesigner installation uses:

```bash
ls "/Applications/TouchDesigner-2025-30770.app/Contents/Frameworks/Python.framework/Versions/"
```

If you see `3.11`, proceed with the installation steps below.

### 2. Install/Upgrade pip in TouchDesigner's Python

```bash
"/Applications/TouchDesigner-2025-30770.app/Contents/Frameworks/Python.framework/Versions/3.11/bin/python3.11" -m ensurepip --upgrade
```

### 3. Upgrade Build Tools

```bash
"/Applications/TouchDesigner-2025-30770.app/Contents/Frameworks/Python.framework/Versions/3.11/bin/python3.11" -m pip install --upgrade pip setuptools wheel
```

### 4. Install Required Python Packages

```bash
"/Applications/TouchDesigner-2025-30770.app/Contents/Frameworks/Python.framework/Versions/3.11/bin/python3.11" -m pip install matplotlib numpy pillow
```

## 🚀 Usage

1. **Open the TouchDesigner Project**
   - Load `2025-09-28-Plot.toe` in TouchDesigner

2. **Configure Data Source**
   - Point the `source` operator to your CHOP containing the data you want to plot
   - The system will automatically detect channels and plot them

3. **Run the Plot**
   - The plot generation runs automatically on each frame when the timeline is playing
   - Plots are saved to the `plots/` directory as `plot.png`
   - The plot is also fed back into TouchDesigner via the `plot_in` Movie File In TOP

## 📁 Project Structure

```
Matplotlib4TD/
├── README.md                    # This file
├── setup.MD                     # Installation instructions
└── 2025-09-28-Plot/
    ├── 2025-09-28-Plot.toe      # Main TouchDesigner project file
    ├── execute/
    │   ├── execute_plotdraw.py  # Frame execution script
    │   └── plot_update_default.txt # Main plotting logic
    ├── plots/
    │   └── plot.png            # Generated plot output
    ├── Backup/                 # Project backups
    ├── Audio/                  # Audio assets
    ├── Chan/                   # Channel data
    ├── Geo/                    # Geometry data
    ├── Image/                  # Image assets
    ├── Movie/                  # Movie assets
    └── MovieOuts/              # Rendered movie outputs
```

## 🔧 Technical Details

### Plot Generation Process

1. **Data Extraction**: The system reads CHOP data from the specified source operator
2. **Time Base**: Uses sample rate to create time-based X-axis, falls back to sample index if rate unavailable
3. **Multi-Channel Support**: Automatically handles multiple channels with individual labeling
4. **Plot Styling**: Creates 6x3 inch plots at 100 DPI with automatic legend placement
5. **TouchDesigner Integration**: Feeds generated plots back into TD via Movie File In TOP

### Key Features

- **Robust Channel Access**: Compatible across different TouchDesigner builds
- **Automatic Scaling**: Time-based or sample-based X-axis depending on available data
- **Real-time Updates**: Plots update every frame when timeline is active
- **Error Handling**: Graceful handling of missing or empty data sources

## 🛠️ Customization

### Modifying Plot Appearance

Edit the plotting parameters in `execute/plot_update_default.txt`:

```python
plt.figure(figsize=(6, 3), dpi=100)  # Adjust size and resolution
plt.title("Live CHOP plot")          # Change plot title
```

### Changing Output Location

Modify the `OUT_PATH` variable in `plot_update_default.txt`:

```python
OUT_PATH = os.path.join(PLOTS_DIR, "your_plot_name.png")
```

### Adding Plot Styles

Customize the plot appearance by modifying the plotting loop:

```python
for y, label in zip(ys, labels):
    plt.plot(x, y, label=label, linewidth=2, alpha=0.8)
```

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure matplotlib is installed in TouchDesigner's Python environment
2. **No Plot Generated**: Check that the `source` operator contains valid CHOP data
3. **Plot Not Updating**: Verify the timeline is playing and the Execute DAT is enabled

### Debug Tips

- Check the TouchDesigner textport for Python error messages
- Verify the `plots/` directory has write permissions
- Test the `make_plot()` function manually by running the text DAT

## 📄 License

This project is open source. Please refer to the project's license file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## 📧 Support

For TouchDesigner-specific questions, consult the [TouchDesigner documentation](https://docs.derivative.ca/).
For matplotlib usage, refer to the [matplotlib documentation](https://matplotlib.org/stable/contents.html).