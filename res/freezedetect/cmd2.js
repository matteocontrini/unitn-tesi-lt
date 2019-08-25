const fs = require('fs');
const lines = fs.readFileSync('out.txt').toString().split('\n');

let filePath = 'C:\\Users\\mcont\\Downloads\\pvr.mp4';
let cmd = `ffmpeg -i ${filePath} -vf "select='`;
let frame;

for (let line of lines) {
    let match = line.match(/frame:(\d+)/);
    
    if (match) {
        frame = match[1];
    }
    
    match = line.match(/lavfi\.freezedetect\.freeze_start=([0-9]+\.[0-9]+)$/);
    
    if (match) {
        cmd += `eq(n,${frame})+`;
    }
}

cmd = cmd.slice(0, - 1); // remove last +
cmd += `'" -vsync 0 %%d.png -y`;

fs.writeFileSync('cmd2.bat', cmd);
