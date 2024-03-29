import { ipcRenderer } from 'electron'
import moment from 'moment'

ipcRenderer.on('get:json:result', (event, { main, renderer }) => {
    const mainTime = moment(main.time || 0).startOf('minute').fromNow()
    const rendererTime = moment(renderer.time || 0).startOf('minute').fromNow()

    document.getElementById("main").innerHTML = mainTime;
    document.getElementById("renderer").innerHTML = rendererTime;
})

ipcRenderer.send('get:json')

setTimeout(() => {
    ipcRenderer.send('get:json')
}, 3000);

document.querySelector('#btnMain').addEventListener('click', () => {
    ipcRenderer.send('reload:main')
})

document.querySelector('#btnRend').addEventListener('click', () => {
    ipcRenderer.send('reload:renderer')
})