import PyInstaller.__main__

PyInstaller.__main__.run([
    './src/logo.py',
    '--distpath', './dist',
    '--onefile',
    '--windowed',
    '--add-data', './src/logoS.png;.'
])