# [yolo v4](https://github.com/AlexeyAB/darknet#how-to-compile-on-windows-using-cmake)

### How to compile on Windows (using `CMake`)

Requires:

* MSVC: https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community
* CMake GUI: `Windows win64-x64 Installer`https://cmake.org/download/
* Download Darknet zip-archive with the latest commit and uncompress it: [master.zip](https://github.com/AlexeyAB/darknet/archive/master.zip)

In Windows:

* Start (button) -> All programs -> CMake -> CMake (gui) ->

* [look at image](https://habrastorage.org/webt/pz/s1/uu/pzs1uu4heb7vflfcjqn-lxy-aqu.jpeg) In CMake: Enter input path to the darknet Source, and output path to the Binaries -> Configure (button) -> Optional platform for generator: `x64`  -> Finish -> Generate -> Open Project ->

* in MS Visual Studio: Select: x64 and Release -> Build -> Build solution

* find the executable file `darknet.exe` in the output path to the binaries you specified

![x64 and Release](https://habrastorage.org/webt/ay/ty/f-/aytyf-8bufe7q-16yoecommlwys.jpeg)


### How to compile on Windows (using `vcpkg`)

This is the recommended approach to build Darknet on Windows.

1. Install Visual Studio 2017 or 2019. In case you need to download it, please go here: [Visual Studio Community](http://visualstudio.com). Remember to install English language pack, this is mandatory for vcpkg!

2. Install CUDA (at least v10.0) enabling VS Integration during installation.

3. Open Powershell (Start -> All programs -> Windows Powershell) and type these commands:

```PowerShell
PS Code/>              git clone https://github.com/AlexeyAB/darknet
PS Code/>              cd darknet
PS Code/darknet>       .\build.ps1 -UseVCPKG -EnableOPENCV -EnableCUDA -EnableCUDNN
```

(add option `-EnableOPENCV_CUDA` if you want to build OpenCV with CUDA support - very slow to build! - or remove options like `-EnableCUDA` or `-EnableCUDNN` if you are not interested in them). If you open the `build.ps1` script at the beginning you will find all available switches.
