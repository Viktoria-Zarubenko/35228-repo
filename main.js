const {app, BrowserWindow} = require('electron')
const path = require('path')

let mainWindow = null
let devtools = null

require('electron-reload') (__dirname, {
  electron: require(`${__dirname}/node_modules/electron`)
});

function createWindow () {

  mainWindow = new BrowserWindow({
    title: "Planer",
    width: 700,
    height: 600,
    show: false,
    resizable: false,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: true,
      devTools: true
    }
  })

  mainWindow.loadURL('http://localhost:8000/index.html');
  mainWindow.setMenuBarVisibility(false)

}

app.whenReady().then(() => {
    let splash = new BrowserWindow({
      width: 700,
      height: 600,
      transparent: true,
      frame: false,
      alwaysOnTop: true
  })

  splash.loadFile('splash.html')

  setTimeout(function () {
    splash.close();
    mainWindow.show()
  }, 100)

  createWindow()
})

app.on('activate', function () {
  if (mainWindow === null) createWindow()
})

app.on('closed', function () {
  mainWindow = null
  app.destroy()
})