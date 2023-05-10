const countWords = require('../src/statsWords.js')
const fs = require('fs');
const path = require('path')
const Tokenizer = require('tokenize-text');
const tokenize = new Tokenizer();

const testDir = path.resolve(__dirname, './word.txt')
const targetDir = path.resolve(__dirname, './target.json')
const textWords = fs.readFileSync(testDir, { encoding: 'utf-8' })
fs.writeFileSync(targetDir, JSON.stringify(tokenize.words()(textWords)))