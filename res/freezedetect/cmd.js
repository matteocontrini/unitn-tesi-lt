const fs = require('fs');
const lines = fs.readFileSync('out.txt').toString().split('\n');

let filePath = 'C:\\Users\\mcont\\Downloads\\pvr.mp4';
let part1 = 'ffmpeg -y';
let part2 = '';
let index = 0;

for (let line of lines) {
    let match = line.match(/lavfi\.freezedetect\.freeze_start=([0-9]+\.[0-9]+)$/);
    
    if (match) {
        part1 += ` -ss ${match[1]} -i ${filePath}`;
        part2 += ` -map ${index}:v -frames:v 1 out${index}.png`;
        index += 1;
    }
}

fs.writeFileSync('cmd.bat', part1 + part2);
