# 👋 HoverPoint - Hand Gesture Control System

A Python-based computer vision project that enables **touchless control** of system volume and mouse using hand gestures. Built with MediaPipe for hand tracking and OpenCV for real-time computer vision processing.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Latest-orange.svg)

## ✨ Features

- **👋 Hand Tracking Module**: Real-time hand detection and landmark tracking using MediaPipe
- **🔊 Volume Control**: Control system volume by adjusting the distance between thumb and index finger
- **🖱️ Mouse Control**: Control mouse cursor using hand gestures (in development)
- **📹 Visual Feedback**: Real-time visualization of hand landmarks and connections
- **⚡ FPS Display**: Performance monitoring with frames per second counter
- **✋ Multi-hand Support**: Ability to track up to 2 hands simultaneously

## 🛠️ Technologies Used

- **Language**: Python 3.x
- **Computer Vision**: OpenCV (cv2)
- **Hand Tracking**: MediaPipe
- **Audio Control**: pycaw (Python Core Audio Windows Library)
- **Additional Libraries**: numpy, comtypes, ctypes

## 📁 Project Structure

```
HoverPoint/
├── HandTrackingModule.py    # Core hand detection and tracking module
├── Volume Controller.py      # Volume control using hand gestures
├── Mouse Controller.py       # Mouse control (in development)
└── README.md                 # Project documentation
```

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- Webcam
- Windows OS (for audio control functionality)

### Setup Instructions

```bash
# Clone the repository
git clone https://github.com/Muhammad-Usama294/HoverPoint.git
cd HoverPoint

# Install required packages
pip install opencv-python
pip install mediapipe
pip install numpy
pip install pycaw
pip install comtypes
```

## 🚀 Usage Guide

### Volume Controller 🔊

Run the volume controller to control your system volume with hand gestures:

```bash
python "Volume Controller.py"
```

**How to use:**
1. Show your hand to the camera
2. Control volume by adjusting the distance between your thumb (landmark 4) and index finger (landmark 8)
   - **Closer fingers** = Lower volume
   - **Further apart** = Higher volume
3. Visual feedback with volume bar and percentage display
4. Green circle indicator appears when fingers are very close (minimum volume)

### Mouse Controller 🖱️

```bash
python "Mouse Controller.py"
```

**Note**: Currently in development. Future features will include:
- Move mouse cursor with index finger
- Click with finger gestures
- Drag and drop functionality

### HandTrackingModule 📦

Reusable module that can be imported into other projects:

```python
import HandTrackingModule as htm

# Create detector instance
detector = htm.handDetector(detectionCon=0.7)

# Use in your project
img = detector.findHands(img)
lmList = detector.findPositions(img)
```

**Features:**
- Custom detection confidence and tracking confidence parameters
- Returns landmark positions in pixel coordinates
- Draws hand connections and landmarks on frames

## 🔍 How It Works

### Hand Tracking Module

The `HandTrackingModule.py` uses MediaPipe's hand tracking solution:

1. **Detection**: Uses MediaPipe Hands solution to detect 21 hand landmarks
2. **Processing**: Converts BGR camera feed to RGB for processing
3. **Tracking**: Returns landmark positions in pixel coordinates
4. **Visualization**: Draws hand connections and landmarks on the frame

**Key landmarks:**
- Landmark 4: Thumb tip
- Landmark 8: Index finger tip
- Landmark 12: Middle finger tip

### Volume Control

The `Volume Controller.py` implements gesture-based volume control:

1. **Hand Detection**: Detects thumb tip (landmark 4) and index finger tip (landmark 8)
2. **Distance Calculation**: Calculates Euclidean distance between the two points
3. **Mapping**: Maps hand gesture range (50-300 pixels) to system volume range (-65 to 0 dB)
4. **Audio Control**: Uses pycaw library to control Windows audio
5. **Feedback**: Displays volume bar and percentage on screen

**Formula:**
```python
distance = math.hypot(x2-x1, y2-y1)
volume = numpy.interp(distance, [50, 300], [minVol, maxVol])
```

## 💻 System Requirements

- **Operating System**: Windows (for pycaw audio control)
- **Python Version**: 3.7 or higher
- **Hardware**: Webcam required for hand tracking
- **Camera Index**: Default is 1 (change to 0 if needed in the code)

## ⚙️ Configuration

You can adjust these parameters in the code to customize behavior:

### HandTrackingModule Configuration

```python
detector = handDetector(
    mode=False,           # Static image mode (False for video)
    maxHands=2,          # Maximum number of hands to track
    detectionCon=0.5,    # Minimum detection confidence (0.0-1.0)
    trackCon=0.5         # Minimum tracking confidence (0.0-1.0)
)
```

### Volume Controller Configuration

```python
wCam, hCam = 640, 480    # Camera resolution
detectionCon = 0.7        # Detection confidence

# Hand gesture range (in pixels)
handRange = [50, 300]     # Min and max distance

# Volume range (in decibels)
volRange = [-65, 0]       # Min and max volume
```

### Camera Settings

If your default camera is not working, change the camera index:
```python
cap = cv2.VideoCapture(0)  # Change from 1 to 0
```

## ⚠️ Known Issues & Future Enhancements

### Current Issues

- **Mouse Controller Incomplete**: The mouse controller has commented code sections and is not fully functional
- **Bug in HandTrackingModule**: `self.results` not assigned before use in `findHands()` method (line 19)
- **Fixed Camera Index**: Camera index is hardcoded (may need adjustment for different systems)
- **Missing pTime Initialization**: `pTime` variable not initialized before use in Volume Controller

### Planned Features

- ✅ Complete mouse control implementation
- ✅ Click and drag functionality
- ✅ Support for macOS and Linux audio control
- ✅ Gesture recognition for custom actions
- ✅ GUI for configuration settings
- ✅ Multi-gesture command system
- ✅ Improved error handling and debugging
- ✅ Recording and playback of gesture sequences

## 🐛 Troubleshooting

### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| **Camera not found** | Change camera index from 1 to 0 in the code: `cap = cv2.VideoCapture(0)` |
| **ModuleNotFoundError** | Install missing packages: `pip install <package-name>` |
| **Audio control not working** | Ensure pycaw is installed. Note: Only works on Windows |
| **Low FPS / Performance** | Reduce camera resolution or lower detection confidence |
| **Hand not detected** | Ensure good lighting and camera quality. Lower `detectionCon` value |
| **Unstable tracking** | Increase `trackCon` value for more stable tracking |

### Debug Mode

To enable debug output in HandTrackingModule, the landmark positions are printed by default. To disable:
```python
# Comment out or remove line 37 in HandTrackingModule.py
# print(id, cx, cy)
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Areas for Contribution

1. **Fix Bugs**: 
   - Fix the `self.results` bug in HandTrackingModule
   - Add proper variable initialization in Volume Controller

2. **Complete Features**:
   - Implement the Mouse Controller functionality
   - Add click and drag gestures

3. **Enhance Functionality**:
   - Add support for macOS and Linux audio control
   - Implement new gesture controls
   - Add configuration GUI

4. **Improve Documentation**:
   - Add video tutorials
   - Create usage examples
   - Translate documentation

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **MediaPipe** by Google for the excellent hand tracking solution
- **OpenCV** for comprehensive computer vision capabilities
- **pycaw** for Windows audio control functionality
- All contributors and users of this project

## 📧 Contact

For questions, suggestions, or issues, please open an issue on GitHub or contact the repository owner.

---

**Made with ❤️ using Python, OpenCV, and MediaPipe**
