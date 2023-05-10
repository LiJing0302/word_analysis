module.exports = function countWords(text) {
    // 去除标点符号和换行符
    text = text.replace(/[^\w\s]|[\d_]/g, '').replace(/\n/g, ' ').toLowerCase();
    // 将字符串按空格分割为单词数组
    let words = text.split(' ');
    // 定义一个对象用于存储单词和数量
    let wordCount = {};
    // 遍历单词数组
    for (let i = 0; i < words.length; i++) {
        let word = words[i];
        // 如果该单词已经存在于对象中，则数量加1
        if (wordCount[word]) {
            wordCount[word]++;
        } else { // 否则将该单词添加到对象中，数量为1
            wordCount[word] = 1;
        }
    }
    // 返回单词数量对象
    return wordCount
}
